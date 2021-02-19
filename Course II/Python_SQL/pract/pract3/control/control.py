import sqlalchemy
from typing import List, Tuple
from datetime import datetime
from faker import Faker
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
from sqlalchemy.sql import select
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint


class Generator:
    """Генерация данных для сущностей"""

    #TODO
    CUSTOMER_ID = 1

    def __init__(self):
        self.fake = Faker("ru_RU")

    def gen_customer(self) -> List:
        """Генерация клиента"""
        result_list = []

        # Текущий ID
        customer_id = Generator.CUSTOMER_ID
        Generator.CUSTOMER_ID += 1

        last_name = "Иванов"
        first_name = "Иван"
        middle_name = "Иванович"
        street = "Ул 8 марта"
        city = self.fake.city()
        state = self.fake.city()
        zip = "4386438906"
        phone = self.fake.phone_number()
        email = self.fake.email()
        return [
            customer_id,
            last_name,
            first_name,
            middle_name,
            street,
            city,
            state,
            zip,
            phone,
            email,
        ]

    #TODO
    def gen_account_types(self):
        """Генерация типов аккаунтов"""
        pass

    #TODO
    def gen_transactions(self):
        """Генерация операций"""
        pass

    #TODO
    def gen_customers_accounts(self, customer_id: int, account_id: int):
        """Генерация промежуточной таблицы"""
        pass


class DatabaseProcessing:
    def __init__(self, sql_connection: str) -> None:
        engine = create_engine("sqlite:///Demenchuk_bank.db")
        self.connection = engine.connect()
        self.engine = engine
        self.metadata = MetaData()

        # Словарь с хранением таблиц
        self.tables_dict = {}

        self.generate_table()

    def generate_table(self):
        """Создание таблиц"""

        metadata = self.metadata
        customers = Table(
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
        self.tables_dict["customers"] = {}
        self.tables_dict["customers"]["table"] = customers
        self.tables_dict["customers"]["fields"] = [
            "customer_id",
            "last_name",
            "first_name",
            "middle_name",
            "street",
            "city",
            "state",
            "zip",
            "phone",
            "email",
        ]

        account_types = Table(
            "account_types",
            metadata,
            Column("type_id", Integer(), primary_key=True),
            Column("name", String(255), nullable=False),
            Column("description", String(255), nullable=True),
            extend_existing=True,
        )
        self.tables_dict["account_types"] = {}
        self.tables_dict["account_types"]["table"] = account_types
        self.tables_dict["account_types"]["fields"] = ["type_id", "name", "description"]

        accounts = Table(
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
        self.tables_dict["accounts"] = {}
        self.tables_dict["accounts"]["table"] = accounts
        self.tables_dict["accounts"]["fields"] = [
            "account_id",
            "type",
            "description",
            "balance",
            "credit_line",
            "begin_balance",
            "begin_balance_timestamp",
        ]

        transactions = Table(
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
        self.tables_dict["transactions"] = {}
        self.tables_dict["transactions"]["table"] = accounts
        self.tables_dict["transactions"]["fields"] = [
            "transaction_id",
            "account_id",
            "timestamp",
            "amount",
            "balance",
            "begin_balance",
            "description",
        ]

        # Связь многие ко многим для таблиц customers и accounts
        customers_accounts = Table(
            "customers_accounts",
            metadata,
            Column("customer_id", ForeignKey("customers.customer_id")),
            Column("account_id", ForeignKey("accounts.account_id")),
            extend_existing=True,
        )
        self.tables_dict["customers_accounts"] = {}
        self.tables_dict["customers_accounts"]["table"] = customers_accounts
        self.tables_dict["customers_accounts"]["fields"] = ["customer_id", "account_id"]

        # Создали все данные
        metadata.create_all(self.engine)

    def insert(self, table_name: str, values: List) -> int:
        """Вставка данных в таблицу table_name"""

        if table_name not in self.tables_dict:
            raise ValueError(f"Переданной таблицы {table_name} не существует!")

        current_table = self.tables_dict[table_name]["table"]
        fields_list = self.tables_dict[table_name]["fields"]

        ins = current_table.insert().values(**dict(zip(fields_list, values)))
        result = self.connection.execute(ins)
        return result.inserted_primary_key[0]

    def select(self, table_name: str) -> List[Tuple]:
        """Выборка данных из таблицы table_name"""

        # Фильтрация данных
        if table_name not in self.tables_dict:
            raise ValueError(f"Переданной таблицы {table_name} не существует!")

        # Текущая таблица
        current_table = self.tables_dict[table_name]["table"]

        # Команда для выбора
        s = select([current_table])

        # Применяем команду для соединения
        rp = self.connection.execute(s)
        return rp.fetchall()


def main():

    # Вставка данных

    database_processing = DatabaseProcessing("sqlite:///Demenchuk_bank.db")
    generator = Generator()
    for i in range(100):
        values = generator.gen_customer()
        pk = database_processing.insert("customers", values)
        print(f"Записали данные с первичным ключом {pk}")
    result = database_processing.select("customers")
    print(result)


if __name__ == "__main__":
    main()
