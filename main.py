from fishbowl.database import session
from fishbowl.database.models import Part



parts = session.query(Part).filter(Part.description.like('%ga wire%')).all()

for part in parts:
    print(part.num, part.description, part.uomObj.code)