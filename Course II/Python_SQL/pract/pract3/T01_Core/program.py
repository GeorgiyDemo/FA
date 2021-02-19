import sqlalchemy
from sqlalchemy.sql import select
import pandas as pd
from datetime import datetime
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    create_engine,
)
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint

engine = create_engine("sqlite:///listings_program.db")
metadata = MetaData()

# 1-2

listing = Table(
    "listing",
    metadata,
    Column("listing_id", Integer(), primary_key=True),
    Column("listing_name", String(50), index=True),
    Column("listing_url", String(255)),
    Column("host_id", Integer()),
    Column("neighbourhood_id", Integer()),
    Column("amenities", String(300)),
    Column("property_type_id", Integer()),
    Column("room_type_id", Integer()),
    Column("bedrooms", Integer()),
    Column("beds", Integer()),
    Column("price", Numeric(7, 2)),
    CheckConstraint("price >= 0.00", name="listing_price_positive"),
    extend_existing=True,
)

# 1-3
user = Table(
    "user",
    metadata,
    Column("user_id", Integer(), primary_key=True),
    Column("user_name", String(15), nullable=False, unique=True),
    Column("email_address", String(255), nullable=False),
    Column("phone", String(20), nullable=False),
    Column("password", String(25), nullable=False),
    Column("created_on", DateTime(), default=datetime.now),
    Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now),
)

# 1-4

order = Table(
    "order",
    metadata,
    Column("order_id", Integer(), primary_key=True),
    Column("user_id", ForeignKey("user.user_id")),
    Column("confirmed", Boolean(), default=False),
    Column("order_price", Integer()),
    extend_existing=True,
)

# 1-5

line_item = Table(
    "line_item",
    metadata,
    Column("line_item_id", Integer(), primary_key=True),
    Column("order_id", ForeignKey("order.order_id")),
    Column("listing_id", ForeignKey("listing.listing_id")),
    Column("item_start_date", DateTime()),
    Column("item_end_date", DateTime()),
    Column("item_price", Integer()),
    extend_existing=True,
)

# 1-6

neighbourhood = Table(
    "neighbourhood",
    metadata,
    Column("neighbourhood_id", Integer(), primary_key=True),
    Column("neighbourhood_name", String(30)),
)

# 1-7

property_type = Table(
    "property_type",
    metadata,
    Column("property_type_id", Integer(), primary_key=True),
    Column("property_type_name", String(30)),
)

# 1-8

room_type = Table(
    "room_type",
    metadata,
    Column("room_type_id", Integer(), primary_key=True),
    Column("property_type_name", String(30)),
)

# Создаем структуру
metadata.create_all(engine)

# Данные, которые вставляем в таблицу
am = pd.read_csv("ListingsAmsterdam.csv", sep=";")
# Вставка данных
ins = listing.insert().values(
    listing_id=20168,
    listing_name="Studio with private bathroom in the centre 1",
    listing_url="https://www.airbnb.com/rooms/20168",
    host_id=59484,
    neighbourhood_id=4,
    property_type_id=35,
    room_type_id=3,
    amenities=am.loc[0, "amenities"][:300],
    bedrooms=1,
    beds=1,
    price=236,
)

ins.compile().params
connection = engine.connect()
result = connection.execute(ins)
print(result.inserted_primary_key)

#SELECT *
s = select([listing])
rp = connection.execute(s)
results = rp.fetchall()
print(results)

#SELECT WHERE
selected_listingid = sqlalchemy.sql.column('listing_id')
where_query = sqlalchemy.sql.select([listing]).where(selected_listingid == 20168)
rp = connection.execute(where_query)
results = rp.fetchall()
print(results)