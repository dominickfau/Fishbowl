import math
import datetime
import pandas
from typing import List
from fishbowl.database import session
from fishbowl.database.models import SalesOrderItem, BomItem, BomItemType


def get_nested_bomItems(bom_items: List['BomItem']):
    """Recursively get all nested bom items"""
    for bom_item in bom_items:
        if bom_item.partObj.defaultBomObj:
            nested_bom_items = session.query(BomItem).filter(BomItem.bomId == bom_item.partObj.defaultBomObj.id).filter(BomItem.typeId == raw_bom_type_id).all()
            bom_items.extend(get_nested_bomItems(nested_bom_items))
    
    return bom_items


t_start = datetime.datetime.now()

raw_bom_type_id = session.query(BomItemType).filter(BomItemType.name == "Raw Good").first().id

open_sales_order_items = session.query(SalesOrderItem).filter(SalesOrderItem.statusId <= 30).all()

data = []
for sales_order_item in open_sales_order_items:
    bom_id = None
    product = sales_order_item.productObj
    if product:
        part = product.partObj
        if part:
            defaultBomObj = part.defaultBomObj
            if defaultBomObj:
                bom_id = defaultBomObj.id
    
    if bom_id:
        # bom_items = get_nested_bomItems(session.query(BomItem).filter(BomItem.bomId == bom_id).filter(BomItem.typeId == raw_bom_type_id).all())
        bom_items = session.query(BomItem).filter(BomItem.bomId == bom_id).filter(BomItem.typeId == raw_bom_type_id).all()

        for sales_order_item_bom_item in bom_items:
            part = sales_order_item_bom_item.partObj
            key = part.id
            qty_needed = sales_order_item.qtyLeftToFulfill * sales_order_item_bom_item.quantity
            qty_needed = math.ceil(qty_needed) if part.uomObj.code == "ea" else qty_needed
            data.append([sales_order_item.dateScheduledFulfillment, sales_order_item.soObj.num, part.num, part.description, qty_needed, part.uomObj.code])

headers = ['Due Date', 'SO Number', 'Part Number', 'Description', 'Quantity', 'UOM']

# Create a Pandas dataframe from the data.
df = pandas.DataFrame.from_records(data, columns=headers)
df.to_csv('part.csv', index=False)

# Group by week of Due Date and Part Number and sum the Quantity.
df = df.groupby([pandas.Grouper(key='Due Date', freq='W-MON'), 'Part Number', 'Description', 'UOM'])['Quantity'].sum().reset_index()

df = df.sort_values(['Due Date'])

# Save the dataframe to a excel file.
# df.to_excel('parts_needed.xlsx', index=False)

# Save the dataframe to a csv file.
df.to_csv('parts_needed.csv', index=False)

t_end = datetime.datetime.now()
total_time = t_end - t_start
print(total_time.total_seconds())