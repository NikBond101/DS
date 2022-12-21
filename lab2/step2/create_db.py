import sqlite3


def _create_database_companies(name: str) -> None:
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies
        ([код компании] INTEGER PRIMARY KEY,
        [название] VARCHAR(100) NOT NULL,
        [дата основания] DATE,
        [количество сотрудников] INTEGER,
        [представительства] INTEGER,
        [генеральный директор] VARCHAR(100) NOT NULL,
        [котировка] DECIMAL,
        [биржа] VARCHAR(100))
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products
        ([код продукта] INTEGER PRIMARY KEY,
        [имя организации] VARCHAR(100) NOT NULL,
        [продукция] VARCHAR(100) NOT NULL,
        [ежегодный объем] INTEGER,
        [страна производитель] VARCHAR(100),
        [пик продаж] DATE,
        [средняя цена] DECIMAL,
        FOREIGN KEY ('имя организации') REFERENCES companies(название))
        ''')

    # insert data into table companies
    cursor.execute('''
        INSERT INTO companies VALUES (1, 'APPLE', '01.04.1976', 154000, 65, 'Timothy Donald Cook', 144.56, 'NASDAQ')
    ''')
    cursor.execute('''
        INSERT INTO companies VALUES (2, 'TESLA', '01.07.2003', 110000, 34, 'Elon Musk', 168.68, 'NASDAQ')
    ''')

    # insert data into table products

    cursor.execute('''
        INSERT INTO products VALUES (1, 'APPLE', 'iphone', 234000000, "Китай", '22.08.2015', 1552)
    ''')

    cursor.execute('''
            INSERT INTO products VALUES (2, 'APPLE', 'VR', 12300000, "Китай", '14.11.2021', 2330)
        ''')

    cursor.execute('''
            INSERT INTO products VALUES (3, 'TESLA', 'car', 5230000, "Китай", '11.02.2019', 54000)
        ''')

    cursor.execute('''
            INSERT INTO products VALUES (4, 'TESLA', 'electro battery', 13500000, "США", '13.02.2017', 4300)
        ''')

    # records = cursor.fetchall()

    conn.commit()


def _test_database(name:str) -> None:
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM companies
        ''')
    companies_records = cursor.fetchall()
    cursor.execute('''
        SELECT * FROM products
        ''')
    products_records = cursor.fetchall()

    print("RECORDS FROM COMPANIES")
    for company_record in companies_records:
        print(company_record)

    print("\n")
    print("RECORDS FROM PRODUCTS")
    for product_record in products_records:
        print(product_record)

    conn.commit()


if __name__ == "__main__":
    _create_database_companies("companies")
    _test_database("companies")