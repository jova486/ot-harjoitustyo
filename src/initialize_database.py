from database.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists lists;
    ''')

    cursor.execute('''
        drop table if exists stat;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text,
            teacher INTEGER
        );
    ''')

    cursor.execute('''
        create table lists (
            name text primary key,
            language text,
            creator text,
            data VARCHAR

        );
    ''')

    cursor.execute('''
        create table stat (
            user text,
            name text,
            date timestamp,
            value real

        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
