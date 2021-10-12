from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from fishbowl.database import Base, session
from fishbowl.database.baseclass import BaseType
from fishbowl.database.account import Account
from fishbowl.database.inventory import LocationGroup


class AddressType(BaseType):
    """Represents an Account Type."""
    __tablename__ = 'addresstype'

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default AddressTypes."""
        data =  [
            cls(id=10, name='Ship To'),
            cls(id=20, name='Bill To'),
            cls(id=30, name='Remit To'),
            cls(id=40, name='Home'),
            cls(id=50, name='Main Office')
        ]
        session.add_all(data)
        session.commit()

class Country(Base):
    """Represents a Country."""
    __tablename__ = 'countryconst'
    
    id = Column(Integer, primary_key=True)
    abbreviation = Column(String(10), nullable=False)
    name = Column(String(50), nullable=False)
    ups = Column(Boolean, nullable=False, default=True)

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default Countries."""
        data =  [
            cls(abbreviation="Unknown", name="Unknown", ups=False),
            cls(abbreviation="US", name="UNITED STATES"),
            cls(abbreviation="CA", name="CANADA"),
            cls(abbreviation="GB", name="UNITED KINGDOM"),
            cls(abbreviation="RU", name="RUSSIAN FEDERATION"),
            cls(abbreviation="CN", name="CHINA"),
            cls(abbreviation="JP", name="JAPAN"),
            cls(abbreviation="KR", name="KOREA, REPUBLIC OF"),
            cls(abbreviation="KP", name="KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),
            cls(abbreviation="MX", name="MEXICO"),
            cls(abbreviation="DE", name="GERMANY"),
            cls(abbreviation="ES", name="SPAIN"),
            cls(abbreviation="FR", name="FRANCE"),
            cls(abbreviation="FI", name="FINLAND"),
            cls(abbreviation="IS", name="ICELAND"),
            cls(abbreviation="AU", name="AUSTRALIA"),
            cls(abbreviation="AF", name="AFGHANISTAN"),
            cls(abbreviation="AX", name="ALAND ISLANDS"),
            cls(abbreviation="AL", name="ALBANIA"),
            cls(abbreviation="DZ", name="ALGERIA"),
            cls(abbreviation="AS", name="AMERICAN SAMOA"),
            cls(abbreviation="AD", name="ANDORRA"),
            cls(abbreviation="AO", name="ANGOLA"),
            cls(abbreviation="AI", name="ANGUILLA"),
            cls(abbreviation="AQ", name="ANTARCTICA"),
            cls(abbreviation="AG", name="ANTIGUA AND BARBUDA"),
            cls(abbreviation="AR", name="ARGENTINA"),
            cls(abbreviation="AM", name="ARMENIA"),
            cls(abbreviation="AW", name="ARUBA"),
            cls(abbreviation="AT", name="AUSTRIA"),
            cls(abbreviation="AZ", name="AZERBAIJAN"),
            cls(abbreviation="BS", name="BAHAMAS"),
            cls(abbreviation="BH", name="BAHRAIN"),
            cls(abbreviation="BD", name="BANGLADESH"),
            cls(abbreviation="BB", name="BARBADOS"),
            cls(abbreviation="BY", name="BELARUS"),
            cls(abbreviation="BE", name="BELGIUM"),
            cls(abbreviation="BZ", name="BELIZE"),
            cls(abbreviation="BJ", name="BENIN"),
            cls(abbreviation="BM", name="BERMUDA"),
            cls(abbreviation="BT", name="BHUTAN"),
            cls(abbreviation="BO", name="BOLIVIA"),
            cls(abbreviation="BA", name="BOSNIA AND HERZEGOVINA"),
            cls(abbreviation="BW", name="BOTSWANA"),
            cls(abbreviation="BV", name="BOUVET ISLAND"),
            cls(abbreviation="BR", name="BRAZIL"),
            cls(abbreviation="IO", name="BRITISH INDIAN OCEAN TERRITORY"),
            cls(abbreviation="BN", name="BRUNEI DARUSSALAM"),
            cls(abbreviation="BG", name="BULGARIA"),
            cls(abbreviation="BF", name="BURKINA FASO"),
            cls(abbreviation="BI", name="BURUNDI"),
            cls(abbreviation="KH", name="CAMBODIA"),
            cls(abbreviation="CM", name="CAMEROON"),
            cls(abbreviation="CV", name="CAPE VERDE"),
            cls(abbreviation="KY", name="CAYMAN ISLANDS"),
            cls(abbreviation="CF", name="CENTRAL AFRICAN REPUBLIC"),
            cls(abbreviation="TD", name="CHAD"),
            cls(abbreviation="CL", name="CHILE"),
            cls(abbreviation="CX", name="CHRISTMAS ISLAND"),
            cls(abbreviation="CC", name="COCOS (KEELING) ISLANDS"),
            cls(abbreviation="CO", name="COLOMBIA"),
            cls(abbreviation="KM", name="COMOROS"),
            cls(abbreviation="CG", name="CONGO"),
            cls(abbreviation="CD", name="CONGO, THE DEMOCRATIC REPUBLIC OF THE"),
            cls(abbreviation="CK", name="COOK ISLANDS"),
            cls(abbreviation="CR", name="COSTA RICA"),
            cls(abbreviation="CI", name="COTE D'IVOIRE"),
            cls(abbreviation="HR", name="CROATIA"),
            cls(abbreviation="CU", name="CUBA"),
            cls(abbreviation="CY", name="CYPRUS"),
            cls(abbreviation="CZ", name="CZECH REPUBLIC"),
            cls(abbreviation="DK", name="DENMARK"),
            cls(abbreviation="DJ", name="DJIBOUTI"),
            cls(abbreviation="DM", name="DOMINICA"),
            cls(abbreviation="DO", name="DOMINICAN REPUBLIC"),
            cls(abbreviation="EC", name="ECUADOR"),
            cls(abbreviation="EG", name="EGYPT"),
            cls(abbreviation="SV", name="EL SALVADOR"),
            cls(abbreviation="GQ", name="EQUATORIAL GUINEA"),
            cls(abbreviation="ER", name="ERITREA"),
            cls(abbreviation="EE", name="ESTONIA"),
            cls(abbreviation="ET", name="ETHIOPIA"),
            cls(abbreviation="FK", name="FALKLAND ISLANDS (MALVINAS)"),
            cls(abbreviation="FO", name="FAROE ISLANDS"),
            cls(abbreviation="FJ", name="FIJI"),
            cls(abbreviation="GF", name="FRENCH GUIANA"),
            cls(abbreviation="PF", name="FRENCH POLYNESIA"),
            cls(abbreviation="TF", name="FRENCH SOUTHERN TERRITORIES"),
            cls(abbreviation="GA", name="GABON"),
            cls(abbreviation="GM", name="GAMBIA"),
            cls(abbreviation="GE", name="GEORGIA"),
            cls(abbreviation="GH", name="GHANA"),
            cls(abbreviation="GI", name="GIBRALTAR"),
            cls(abbreviation="GR", name="GREECE"),
            cls(abbreviation="GL", name="GREENLAND"),
            cls(abbreviation="GD", name="GRENADA"),
            cls(abbreviation="GP", name="GUADELOUPE"),
            cls(abbreviation="GU", name="GUAM"),
            cls(abbreviation="GT", name="GUATEMALA"),
            cls(abbreviation="GG", name="GUERNSEY"),
            cls(abbreviation="GN", name="GUINEA"),
            cls(abbreviation="GW", name="GUINEA-BISSAU"),
            cls(abbreviation="GY", name="GUYANA"),
            cls(abbreviation="HT", name="HAITI"),
            cls(abbreviation="HM", name="HEARD ISLAND AND MCDONALD ISLANDS"),
            cls(abbreviation="VA", name="HOLY SEE (VATICAN CITY STATE)"),
            cls(abbreviation="HN", name="HONDURAS"),
            cls(abbreviation="HK", name="HONG KONG"),
            cls(abbreviation="HU", name="HUNGARY"),
            cls(abbreviation="IN", name="INDIA"),
            cls(abbreviation="ID", name="INDONESIA"),
            cls(abbreviation="IR", name="IRAN, ISLAMIC REPUBLIC OF"),
            cls(abbreviation="IQ", name="IRAQ"),
            cls(abbreviation="IE", name="IRELAND"),
            cls(abbreviation="IM", name="ISLE OF MAN"),
            cls(abbreviation="IL", name="ISRAEL"),
            cls(abbreviation="IT", name="ITALY"),
            cls(abbreviation="JM", name="JAMAICA"),
            cls(abbreviation="JE", name="JERSEY"),
            cls(abbreviation="JO", name="JORDAN"),
            cls(abbreviation="KZ", name="KAZAKHSTAN"),
            cls(abbreviation="KE", name="KENYA"),
            cls(abbreviation="KI", name="KIRIBATI"),
            cls(abbreviation="KW", name="KUWAIT"),
            cls(abbreviation="KG", name="KYRGYZSTAN"),
            cls(abbreviation="LA", name="LAO PEOPLE'S DEMOCRATIC REPUBLIC"),
            cls(abbreviation="LV", name="LATVIA"),
            cls(abbreviation="LB", name="LEBANON"),
            cls(abbreviation="LS", name="LESOTHO"),
            cls(abbreviation="LR", name="LIBERIA"),
            cls(abbreviation="LY", name="LIBYAN ARAB JAMAHIRIYA"),
            cls(abbreviation="LI", name="LIECHTENSTEIN"),
            cls(abbreviation="LT", name="LITHUANIA"),
            cls(abbreviation="LU", name="LUXEMBOURG"),
            cls(abbreviation="MO", name="MACAO"),
            cls(abbreviation="MK", name="MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF"),
            cls(abbreviation="MG", name="MADAGASCAR"),
            cls(abbreviation="MW", name="MALAWI"),
            cls(abbreviation="MY", name="MALAYSIA"),
            cls(abbreviation="MV", name="MALDIVES"),
            cls(abbreviation="ML", name="MALI"),
            cls(abbreviation="MT", name="MALTA"),
            cls(abbreviation="MH", name="MARSHALL ISLANDS"),
            cls(abbreviation="MQ", name="MARTINIQUE"),
            cls(abbreviation="MR", name="MAURITANIA"),
            cls(abbreviation="MU", name="MAURITIUS"),
            cls(abbreviation="YT", name="MAYOTTE"),
            cls(abbreviation="FM", name="MICRONESIA, FEDERATED STATES OF"),
            cls(abbreviation="MD", name="MOLDOVA, REPUBLIC OF"),
            cls(abbreviation="MC", name="MONACO"),
            cls(abbreviation="MN", name="MONGOLIA"),
            cls(abbreviation="MS", name="MONTSERRAT"),
            cls(abbreviation="MA", name="MOROCCO"),
            cls(abbreviation="MZ", name="MOZAMBIQUE"),
            cls(abbreviation="MM", name="MYANMAR"),
            cls(abbreviation="NA", name="NAMIBIA"),
            cls(abbreviation="NR", name="NAURU"),
            cls(abbreviation="NP", name="NEPAL"),
            cls(abbreviation="NL", name="NETHERLANDS"),
            cls(abbreviation="AN", name="NETHERLANDS ANTILLES"),
            cls(abbreviation="NC", name="NEW CALEDONIA"),
            cls(abbreviation="NZ", name="NEW ZEALAND"),
            cls(abbreviation="NI", name="NICARAGUA"),
            cls(abbreviation="NE", name="NIGER"),
            cls(abbreviation="NG", name="NIGERIA"),
            cls(abbreviation="NU", name="NIUE"),
            cls(abbreviation="NF", name="NORFOLK ISLAND"),
            cls(abbreviation="MP", name="NORTHERN MARIANA ISLANDS"),
            cls(abbreviation="NO", name="NORWAY"),
            cls(abbreviation="OM", name="OMAN"),
            cls(abbreviation="PK", name="PAKISTAN"),
            cls(abbreviation="PW", name="PALAU"),
            cls(abbreviation="PS", name="PALESTINIAN TERRITORY, OCCUPIED"),
            cls(abbreviation="PA", name="PANAMA"),
            cls(abbreviation="PG", name="PAPUA NEW GUINEA"),
            cls(abbreviation="PY", name="PARAGUAY"),
            cls(abbreviation="PE", name="PERU"),
            cls(abbreviation="PH", name="PHILIPPINES"),
            cls(abbreviation="PN", name="PITCAIRN"),
            cls(abbreviation="PL", name="POLAND"),
            cls(abbreviation="PT", name="PORTUGAL"),
            cls(abbreviation="PR", name="PUERTO RICO"),
            cls(abbreviation="QA", name="QATAR"),
            cls(abbreviation="RE", name="REUNION"),
            cls(abbreviation="RO", name="ROMANIA"),
            cls(abbreviation="RW", name="RWANDA"),
            cls(abbreviation="SH", name="SAINT HELENA"),
            cls(abbreviation="KN", name="SAINT KITTS AND NEVIS"),
            cls(abbreviation="LC", name="SAINT LUCIA"),
            cls(abbreviation="PM", name="SAINT PIERRE AND MIQUELON"),
            cls(abbreviation="VC", name="SAINT VINCENT AND THE GRENADINES"),
            cls(abbreviation="WS", name="SAMOA"),
            cls(abbreviation="SM", name="SAN MARINO"),
            cls(abbreviation="ST", name="SAO TOME AND PRINCIPE"),
            cls(abbreviation="SA", name="SAUDI ARABIA"),
            cls(abbreviation="SN", name="SENEGAL"),
            cls(abbreviation="RS", name="SERBIA AND MONTENEGRO"),
            cls(abbreviation="SC", name="SEYCHELLES"),
            cls(abbreviation="SL", name="SIERRA LEONE"),
            cls(abbreviation="SG", name="SINGAPORE"),
            cls(abbreviation="SK", name="SLOVAKIA"),
            cls(abbreviation="SI", name="SLOVENIA"),
            cls(abbreviation="SB", name="SOLOMON ISLANDS"),
            cls(abbreviation="SO", name="SOMALIA"),
            cls(abbreviation="ZA", name="SOUTH AFRICA"),
            cls(abbreviation="GS", name="SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS"),
            cls(abbreviation="LK", name="SRI LANKA"),
            cls(abbreviation="SD", name="SUDAN"),
            cls(abbreviation="SR", name="SURINAME"),
            cls(abbreviation="SJ", name="SVALBARD AND JAN MAYEN"),
            cls(abbreviation="SZ", name="SWAZILAND"),
            cls(abbreviation="SE", name="SWEDEN"),
            cls(abbreviation="CH", name="SWITZERLAND"),
            cls(abbreviation="SY", name="SYRIAN ARAB REPUBLIC"),
            cls(abbreviation="TW", name="TAIWAN, PROVINCE OF CHINA"),
            cls(abbreviation="TJ", name="TAJIKISTAN"),
            cls(abbreviation="TZ", name="TANZANIA, UNITED REPUBLIC OF"),
            cls(abbreviation="TH", name="THAILAND"),
            cls(abbreviation="TL", name="TIMOR-LESTE"),
            cls(abbreviation="TG", name="TOGO"),
            cls(abbreviation="TK", name="TOKELAU"),
            cls(abbreviation="TO", name="TONGA"),
            cls(abbreviation="TT", name="TRINIDAD AND TOBAGO"),
            cls(abbreviation="TN", name="TUNISIA"),
            cls(abbreviation="TR", name="TURKEY"),
            cls(abbreviation="TM", name="TURKMENISTAN"),
            cls(abbreviation="TC", name="TURKS AND CAICOS ISLANDS"),
            cls(abbreviation="TV", name="TUVALU"),
            cls(abbreviation="UG", name="UGANDA"),
            cls(abbreviation="UA", name="UKRAINE"),
            cls(abbreviation="AE", name="UNITED ARAB EMIRATES"),
            cls(abbreviation="UM", name="UNITED STATES MINOR OUTLYING ISLANDS"),
            cls(abbreviation="UY", name="URUGUAY"),
            cls(abbreviation="UZ", name="UZBEKISTAN"),
            cls(abbreviation="VU", name="VANUATU"),
            cls(abbreviation="VE", name="VENEZUELA"),
            cls(abbreviation="VN", name="VIET NAM"),
            cls(abbreviation="VG", name="VIRGIN ISLANDS, BRITISH"),
            cls(abbreviation="VI", name="VIRGIN ISLANDS, U.S."),
            cls(abbreviation="WF", name="WALLIS AND FUTUNA"),
            cls(abbreviation="EH", name="WESTERN SAHARA"),
            cls(abbreviation="YE", name="YEMEN"),
            cls(abbreviation="ZM", name="ZAMBIA"),
            cls(abbreviation="ZW", name="ZIMBABWE"),
            cls(abbreviation="SS", name="SOUTH SUDAN")
        ]
        session.add_all(data)
        session.commit()


class State(Base):
    """Represents a State in a Country."""
    __tablename__ = 'stateconst'
    id = Column(Integer, primary_key=True)
    code = Column(String(10), nullable=False)
    countryConstID = Column(Integer, ForeignKey('countryconst.id'), nullable=False)
    countryConstObj = relationship('Country', backref=backref('states', lazy='dynamic')) # type: Country
    name = Column(String(100), nullable=False)

    @classmethod
    def create_default_data(cls):
        """This function is used to create all default States."""
        data = [
            cls(code="ZZ", countryConstObj=Country.query.filter_by(name="Unknown").first(), name="Unknown"),
            cls(code="AL", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Alabama"),
            cls(code="AK", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Alaska"),
            cls(code="AZ", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Arizona"),
            cls(code="AR", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Arkansas"),
            cls(code="CA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="California"),
            cls(code="CO", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Colorado"),
            cls(code="CT", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Connecticut"),
            cls(code="DE", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Delaware"),
            cls(code="DC", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="District of Columbia"),
            cls(code="FL", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Florida"),
            cls(code="GA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Georgia"),
            cls(code="GU", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Guam"),
            cls(code="HI", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Hawaii"),
            cls(code="ID", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Idaho"),
            cls(code="IL", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Illinois"),
            cls(code="IN", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Indiana"),
            cls(code="IA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Iowa"),
            cls(code="KS", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Kansas"),
            cls(code="KY", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Kentucky"),
            cls(code="LA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Louisiana"),
            cls(code="ME", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Maine"),
            cls(code="MD", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Maryland"),
            cls(code="MA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Massachusetts"),
            cls(code="MI", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Michigan"),
            cls(code="MN", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Minnesota"),
            cls(code="MS", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Mississippi"),
            cls(code="MO", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Missouri"),
            cls(code="MT", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Montana"),
            cls(code="NE", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Nebraska"),
            cls(code="NV", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Nevada"),
            cls(code="NH", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="New Hampshire"),
            cls(code="NJ", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="New Jersey"),
            cls(code="NM", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="New Mexico"),
            cls(code="NY", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="New York"),
            cls(code="NC", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="North Carolina"),
            cls(code="ND", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="North Dakota"),
            cls(code="MP", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Northern Marina Islands"),
            cls(code="OH", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Ohio"),
            cls(code="OK", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Oklahoma"),
            cls(code="OR", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Oregon"),
            cls(code="PA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Pennsylvania"),
            cls(code="RI", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Rhode Island"),
            cls(code="SC", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="South Carolina"),
            cls(code="SD", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="South Dakota"),
            cls(code="TN", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Tennessee"),
            cls(code="TX", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Texas"),
            cls(code="UT", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Utah"),
            cls(code="VT", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Vermont"),
            cls(code="VA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Virginia"),
            cls(code="VI", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Virgin Islands, U.S."),
            cls(code="WA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Washington"),
            cls(code="WV", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="West Virginia"),
            cls(code="WI", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Wisconsin"),
            cls(code="WY", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Wyoming"),
            cls(code="xx", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="Unknown State"),
            cls(code="AA", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="U.S. Armed Forces - Americas"),
            cls(code="AE", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="U.S. Armed Forces - Europe"),
            cls(code="AP", countryConstObj=Country.query.filter_by(name="UNITED STATES").first(), name="U.S. Armed Forces - Pacific"),
            cls(code="AB", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Alberta"),
            cls(code="BC", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="British Columbia"),
            cls(code="MB", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Manitoba"),
            cls(code="NB", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="New Brunswick"),
            cls(code="NL", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Newfoundland"),
            cls(code="NT", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Northwest Territories"),
            cls(code="NS", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Nova Scotia"),
            cls(code="NU", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Nunavut"),
            cls(code="ON", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Ontario"),
            cls(code="PE", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Prince Edward Island"),
            cls(code="QC", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Quebec"),
            cls(code="SK", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Saskatchewan"),
            cls(code="YT", countryConstObj=Country.query.filter_by(name="CANADA").first(), name="Yukon"),
            cls(code="ACT", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="Australian Capital Territory"),
            cls(code="NSW", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="New South Wales"),
            cls(code="NT", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="Northern Territory"),
            cls(code="QLD", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="Queensland"),
            cls(code="SA", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="South Australia"),
            cls(code="TAS", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="Tasmania"),
            cls(code="VIC", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="Victoria"),
            cls(code="WA", countryConstObj=Country.query.filter_by(name="AUSTRALIA").first(), name="Western Australia"),
            cls(code="SH", countryConstObj=Country.query.filter_by(name="CHINA").first(), name="SHENZHEN"),
            cls(code="TW", countryConstObj=Country.query.filter_by(name="Unknown").first(), name="Taiwan"),
            cls(code="TW", countryConstObj=Country.query.filter_by(name="CHINA").first(), name="Taiwan"),
            cls(code="TST", countryConstObj=Country.query.filter_by(name="CHINA").first(), name="Tsim Sha Tsui"),
            cls(code="IN", countryConstObj=Country.query.filter_by(name="Unknown").first(), name="Indiana")
        ]
        session.add_all(data)
        session.commit()


class Address(Base):
    """Represents an Address."""
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    accountId = Column(Integer, ForeignKey('account.id'))
    accountObj = relationship('Account', backref=backref('addressObj_account', lazy=True)) # type: Account
    name = Column(String(255))
    city = Column(String(255))
    countryId = Column(Integer, ForeignKey('countryconst.id'))
    countryObj = relationship('Country', backref=backref('addressObj_country', lazy=True)) # type: Country
    defaultFlag = Column(Boolean)
    locationGroupId = Column(Integer, ForeignKey('locationgroup.id'))
    locationGroupObj = relationship('LocationGroup', backref=backref('addressObj_locationGroup', lazy=True)) # type: LocationGroup
    addressName = Column(String(255))
    residentialFlag = Column(Boolean)
    stateId = Column(Integer, ForeignKey('stateconst.id'))
    stateObj = relationship('State', backref=backref('addressObj_state', lazy=True)) # type: State
    address = Column(String(255))
    typeId = Column(Integer, ForeignKey('addresstype.id'))
    typeObj = relationship('AddressType', backref=backref('addressObj_type', lazy=True)) # type: AddressType
    zip = Column(String(255))