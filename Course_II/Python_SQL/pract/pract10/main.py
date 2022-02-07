# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, ForeignKey, Index, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Hosts(Base):
    __tablename__ = 'host'
    host_id = Column(Integer, primary_key=True)
    host_name = Column(String(30))


class ListingLyon(Base):
    __tablename__ = 'listing_lyon'
    __table_args__ = (
        CheckConstraint('price >= 0.00'),
    )

    listing_id = Column(Integer, primary_key=True)
    listing_name = Column(String(50), index=True)
    listing_url = Column(String(255))
    host_id = Column(Integer)
    neighbourhood_id = Column(Integer)
    amenities = Column(String(300))
    property_type_id = Column(Integer)
    room_type_id = Column(Integer)
    bedrooms = Column(Integer)
    beds = Column(Integer)
    price = Column(Numeric(7, 2))


class Neighbourhoods(Base):
    __tablename__ = 'neighbourhood'

    neighbourhood_id = Column(Integer, primary_key=True)
    neighbourhood_name = Column(String(30))


class Property_types(Base):
    __tablename__ = 'property_type'

    property_type_id = Column(Integer, primary_key=True)
    property_type_name = Column(String(30))


class Room_types(Base):
    __tablename__ = 'room_type'

    room_type_id = Column(Integer, primary_key=True)
    room_type_name = Column(String(30))


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime)
    updated_on = Column(DateTime)


class Listing(Base):
    __tablename__ = 'listing'
    __table_args__ = (
        CheckConstraint('price >= 0.00'),
        Index('ix_am_price', 'amenities', 'price')
    )
    listing_id = Column(Integer, primary_key=True)
    listing_name = Column(String(50), index=True)
    listing_url = Column(String(255))
    host_id = Column(ForeignKey('host.host_id'))
    neighbourhood_id = Column(ForeignKey('neighbourhood.neighbourhood_id'))
    amenities = Column(String(300))
    property_type_id = Column(ForeignKey('property_type.property_type_id'))
    room_type_id = Column(ForeignKey('room_type.room_type_id'))
    bedrooms = Column(Integer)
    beds = Column(Integer)
    price = Column(Numeric(7, 2))
    host = relationship('Host')
    neighbourhood = relationship('Neighbourhood')
    property_type = relationship('PropertyType')
    room_type = relationship('RoomType')


class Orders(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.user_id'))
    confirmed = Column(Boolean)
    order_price = Column(Integer)
    user = relationship('User')


class Line_items(Base):
    __tablename__ = 'line_item'

    line_item_id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.order_id'))
    listing_id = Column(ForeignKey('listing.listing_id'))
    item_start_date = Column(DateTime)
    item_end_date = Column(DateTime)
    item_price = Column(Integer)

    listing = relationship('Listing')
    order = relationship('Order')