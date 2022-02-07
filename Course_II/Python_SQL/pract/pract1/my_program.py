import sqlalchemy
from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, Boolean, ForeignKey, create_engine)
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
engine = create_engine('sqlite:///listings.db')
metadata = MetaData()


listing=Table('listing',metadata,
               Column('listing_id',Integer(),primary_key=True),
               Column('listing_name',String(50),index=True),
               Column('listing_url',String(255)),
               Column('host_id',Integer()),
               Column('neighbourhood_id',Integer()),
               Column('amenities',String(255)),
               Column('property_type_id',Integer()),
               Column('room_type_id',Integer()),
               Column('bedrooms',Integer()),
               Column('beds',Integer()),
               Column('normal_price',Numeric(7,2)),
               extend_existing=True
            )

user=Table('user',metadata,
            Column('user_id',Integer(),primary_key=True),
            Column('user_name',String(15),nullable=False,unique=True),
            Column('email_address',String(255),nullable=False),
            Column('phone',String(20),nullable=False),
            Column('password',String(25),nullable=False),
            Column('created_on',DateTime(),default=datetime.now),
            Column('updated_on',DateTime(),default=datetime.now,onupdate=datetime.now),
            extend_existing=True
           )

order = Table('order', metadata,
               Column('order_id', Integer(),primary_key=True),
               Column('user_id', ForeignKey('user.user_id')),
               Column('confirmed', Boolean(),default=False),
               Column('order_price', Integer()),
               extend_existing=True
            )
              
line_item = Table('line_item', metadata,
                   Column('line_item_id', Integer(), primary_key=True),
                   Column('order_id', ForeignKey('order.order_id')),
                   Column('listing_id', ForeignKey('listing.listing_id')),
                   Column('item_start_date', DateTime()),
                   Column('item_end_date', DateTime()),
                   Column('item_price', Integer()),
                   extend_existing=True
                )

metadata.create_all(engine)