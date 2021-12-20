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

    wlist_sp = [("yksi", "uno"), ("kaksi", "dos"),
                ("kolme", "tres"), ("neljä", "cuatro")]
    wlist_en = [("yksi", "one"), ("kaksi", "two"),
                ("kolme", "tree"), ("neljä", "four")]
    data = ""
    for i in wlist_sp:
        data += i[0]+","+i[1]+"\n"

    query = "INSERT INTO lists(name, language,creator,data) VALUES (?, ?, ?, ?)"
    cursor.execute(query, ("Numerot-Espanja", "Espanja", "Admin", data))

    data = ""
    for i in wlist_en:
        data += i[0]+","+i[1]+"\n"

    query = "INSERT INTO lists(name, language,creator,data) VALUES (?, ?, ?, ?)"
    cursor.execute(query, ("Numerot-Englanti", "Englanti", "Admin", data))

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
