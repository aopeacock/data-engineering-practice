import psycopg2
import os
import csv


def load_accounts(conn, file_name):
    cursor = conn.cursor()

    with open(f'./data/{file_name}', 'r') as accounts_file:
        reader = csv.reader(accounts_file)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )
    conn.commit()
    cursor.close()


def load_products(conn, file_name):
    cursor = conn.cursor()

    with open(f'./data/{file_name}', 'r') as products_file:
        reader = csv.reader(products_file)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO products VALUES (%s, %s, %s)",
                row
            )
    conn.commit()
    cursor.close()


def load_transactions(conn, file_name):
    cursor = conn.cursor()

    with open(f'./data/{file_name}', 'r') as transactions_file:
        reader = csv.reader(transactions_file)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO transactions VALUES (%s, %s, %s, %s, %s, %s, %s)",
                row
            )
    conn.commit()
    cursor.close()


def main():
    host = 'postgres'
    database = 'postgres'
    user = 'postgres'
    pas = 'postgres'
    conn = psycopg2.connect(host=host, database=database,
                            user=user, password=pas)

    load_accounts(conn, 'accounts.csv')
    load_products(conn, 'products.csv')
    load_transactions(conn, 'transactions.csv')


if __name__ == '__main__':
    main()
