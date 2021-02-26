import random
import sqlalchemy
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
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.sql import select
from sqlalchemy.sql.elements import Null
from typing import List, Tuple, Dict


class Util:
    """Класс утилит с доп методами"""

    @staticmethod
    def gen_name(fake: Faker):
        """Генерация имени пользователя"""
        exit_flag = False
        while not exit_flag:
            try:
                first_name, middle_name, last_name = fake.name().split(" ")
                exit_flag = True
            except ValueError:
                continue

        return first_name, middle_name, last_name

    @staticmethod
    def get_number_range(n) -> str:
        """Отдает n рандомных цифр"""
        result = ""
        for _ in range(n):
            result += str(random.choice(range(10)))
        return result


class Generator:
    """Генерация данных для таблиц"""

    CUSTOMER_ID = 1
    ACCOUNT_ID = 1
    TYPE_ID = 1
    TRANSACTION_ID = 1
    ACCOUNT_ID = 1

    def __init__(self):
        self.fake = Faker("ru_RU")

    def gen_customer(self) -> Dict:
        """Генерация клиента"""

        # Текущий ID
        customer_id = Generator.CUSTOMER_ID
        Generator.CUSTOMER_ID += 1
        first_name, middle_name, last_name = Util.gen_name(self.fake)
        street = self.fake.address()
        city = self.fake.city()
        state = self.fake.city()
        zip = Util.get_number_range(6)
        phone = self.fake.phone_number()
        email = self.fake.email()
        return {
            "customer_id": customer_id,
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "street": street,
            "city": city,
            "state": state,
            "zip": zip,
            "phone": phone,
            "email": email,
        }

    def gen_accounts(self) -> Dict:
        account_id = Generator.ACCOUNT_ID
        Generator.ACCOUNT_ID += 1
        type = random.randint(0, 1)
        description = "-"
        balance = random.uniform(1000.5, 10000.9)
        credit_line = 100000
        begin_balance = round(random.uniform(1000.0, 30000.0), 2)
        begin_balance_timestamp = self.fake.date_time_between(
            start_date="-2y", end_date="now"
        )

        return {
            "account_id": account_id,
            "type": type,
            "description": description,
            "balance": balance,
            "credit_line": credit_line,
            "begin_balance": begin_balance,
            "begin_balance_timestamp": begin_balance_timestamp,
        }

    def gen_account_types(self) -> Dict:
        """Генерация типов аккаунтов"""
        type_id = Generator.TYPE_ID
        Generator.TYPE_ID += 1
        if type_id == 1:
            name = "Обычный"
            description = "Обычный аккаунт со стандартным пакетом обслуживания"
        elif type_id == 2:
            name = "Премиальный"
            description = "Аккаунт с премиальным обслуживанием и повышенным кешбеком"
        else:
            raise ValueError("типов аккаунтов должно быть не более 2!")
        return {"type_id": type_id, "name": name, "description": description}

    def gen_transactions(self) -> Dict:
        """Генерация операций"""

        transaction_id = Generator.TRANSACTION_ID
        Generator.TRANSACTION_ID += 1

        account_id = Generator.ACCOUNT_ID
        Generator.ACCOUNT_ID += 1

        timestamp = self.fake.date_time_between(start_date="-2y", end_date="now")
        amount = random.uniform(1000.5, 10000.9)
        balance = random.uniform(1000.5, 10000.9)
        description = "-"

        return {
            "transaction_id": transaction_id,
            "account_id": account_id,
            "timestamp": timestamp,
            "amount": amount,
            "balance": balance,
            "description": description,
        }

    def gen_customers_accounts(self, customer_id: int, account_id: int) -> Dict:
        """Генерация промежуточной таблицы"""
        return {
            "customer_id": customer_id,
            "account_id": account_id,
        }


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
        self.tables_dict["customers"] = customers

        account_types = Table(
            "account_types",
            metadata,
            Column("type_id", Integer(), primary_key=True),
            Column("name", String(255), nullable=False),
            Column("description", String(255), nullable=True),
            extend_existing=True,
        )
        self.tables_dict["account_types"] = account_types
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
        self.tables_dict["accounts"] = accounts

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
        self.tables_dict["transactions"] = transactions

        # Связь многие ко многим для таблиц customers и accounts
        customers_accounts = Table(
            "customers_accounts",
            metadata,
            Column("customer_id", ForeignKey("customers.customer_id")),
            Column("account_id", ForeignKey("accounts.account_id")),
            extend_existing=True,
        )
        self.tables_dict["customers_accounts"] = customers_accounts

        # Создали все данные
        metadata.create_all(self.engine)

    def insert(self, table_name: str, values: Dict) -> int:
        """Вставка данных в таблицу table_name"""

        if table_name not in self.tables_dict:
            raise ValueError(f"Переданной таблицы {table_name} не существует!")

        current_table = self.tables_dict[table_name]

        ins = current_table.insert().values(**values)
        result = self.connection.execute(ins)

        if len(result.inserted_primary_key) != 0:
            return result.inserted_primary_key[0]

    def select(self, table_name: str) -> List[Tuple]:
        """Выборка данных из таблицы table_name"""

        # Фильтрация данных
        if table_name not in self.tables_dict:
            raise ValueError(f"Переданной таблицы {table_name} не существует!")

        # Текущая таблица
        current_table = self.tables_dict[table_name]

        # Команда для выбора
        s = select([current_table])

        # Применяем команду для соединения
        rp = self.connection.execute(s)
        return rp.fetchall()


def main():
    # Вставка данных

    database_processing = DatabaseProcessing("sqlite:///Demenchuk_bank.db")
    generator = Generator()

    # Генерируем виды аккаунтов
    for i in range(2):
        account_type = generator.gen_account_types()
        pk = database_processing.insert("account_types", account_type)
        print(f"Записали тип аккаунта с первичным ключом {pk}")

    # Генерируем пользователей
    for i in range(100):
        customer = generator.gen_customer()
        pk = database_processing.insert("customers", customer)
        print(f"Записали пользователя с первичным ключом {pk}")
        # Генерируем аккаунты пользователей
        for j in range(10):
            account = generator.gen_accounts()
            pk = database_processing.insert("accounts", account)
            print(f"Cоздали аккаунт {pk}")

            # Связываем аккаунты с пользователями
            customer_id, account_id = customer["customer_id"], account["account_id"]
            customers_accounts = generator.gen_customers_accounts(
                customer_id, account_id
            )
            database_processing.insert("customers_accounts", customers_accounts)
            print(f"Связали аккаунт {account_id} с пользователем {customer_id}")

            # Генерируем транзакции по аккаунтам пользователей
            for k in range(100):
                tx = generator.gen_transactions()
                tx_id = tx["transaction_id"]
                database_processing.insert("transactions", tx)
                print(
                    f"Создали транзакацию {tx_id} для аккаунта {account_id} пользователя {customer_id}"
                )

    # Выбираем всех клиентов из БД (пример SELECT'а)
    result = database_processing.select("customers")
    for item in result:
        print(item)


if __name__ == "__main__":
    main()
