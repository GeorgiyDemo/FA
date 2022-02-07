import sqlalchemy
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
    Float,
)
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint

engine = create_engine("sqlite:///Demenchuk_bank.db")
metadata = MetaData()


customer = Table(
    "customers",
    metadata,
    Column("customer_id", Integer(), primary_key=True),
    Column("last_name", String(255), nullable=False),
    Column("first_name", String(255), nullable=False),
    Column("middle_name", String(255), nullable=True),
    Column("street", String(255), nullable=False),
    Column("city", String(255), nullable=False),
    Column("state", String(255), nullable=False),
    Column("zip", String(15), nullable=False),
    Column("phone", String(11), unique=True, nullable=False),
    Column("email", String(255), unique=True, nullable=False),
    extend_existing=True,
)

account_types = Table(
    "account_types",
    metadata,
    Column("type_id", Integer(), primary_key=True),
    Column("name", String(255), nullable=False),
    Column("description", String(255), nullable=True),
    extend_existing=True,
)

account = Table(
    "accounts",
    metadata,
    Column("account_id", Integer(), primary_key=True),
    Column("type", ForeignKey("account_types.type_id")),
    Column("description", String(255), nullable=True),
    Column("balance", Float(), nullable=False),
    Column("credit_line", Float(), nullable=False),
    Column("begin_balance", Float(), default=0.0),
    Column("begin_balance_timestamp", DateTime(), default=datetime.now),
    extend_existing=True,
)

tx = Table(
    "transactions",
    metadata,
    Column("transaction_id", Integer(), primary_key=True),
    Column("account_id", ForeignKey("accounts.account_id"), nullable=False),
    Column("timestamp", DateTime(), default=datetime.now),
    Column("amount", Float(), nullable=False),
    Column("balance", Float(), nullable=False),
    Column("description", String(255), nullable=True),
    extend_existing=True,
)

# Связь многие ко многим для таблиц customers и accounts
customers_accounts = Table(
    "customers_accounts",
    metadata,
    Column("customer_id", ForeignKey("customers.customer_id")),
    Column("account_id", ForeignKey("accounts.account_id")),
    extend_existing=True,
)

metadata.create_all(engine)
