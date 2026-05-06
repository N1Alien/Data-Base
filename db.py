# ex_02_create_tables.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_games_developer(conn, game_developers):
   """
   Create a new developer into the game_developers table
   :param conn:
   :param game_developers:
   :return: developer id
   """
   sql = '''INSERT INTO game_developers(name, country, start_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, game_developers)
   conn.commit()
   return cur.lastrowid

def add_game(conn, game):
   """
   Create a new game into the games table
   :param conn:
   :param game:
   :return: game id
   """
   sql = '''INSERT INTO games(developer_id, name, genre, platform, release_date, rating)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, game)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":

   create_game_developers_sql = """
   -- game developers table
   CREATE TABLE IF NOT EXISTS game_developers (
      id integer PRIMARY KEY,
      name text NOT NULL,
      country text,
      start_date text
   );
   """

   create_games_sql = """
   -- games table
   CREATE TABLE IF NOT EXISTS games (
      id integer PRIMARY KEY,
      developer_id integer NOT NULL,
      name VARCHAR(250) NOT NULL,
      genre VARCHAR(100),
      platform VARCHAR(100),
      release_date text,
      rating REAL,
      FOREIGN KEY (developer_id) REFERENCES game_developers (id)
   );
   """

#    db_file = "database.db"

#    conn = create_connection(db_file)

#    if conn is not None:
#        execute_sql(conn, create_game_developers_sql)
#        execute_sql(conn, create_games_sql)
#        conn.close()


   game_developers = ("CD Projekt", "Poland", "1994-05-11")
   game=( 1, "Cyberpunk 2077", "RPG", "PC, PS4, Xbox One", "2020-12-10", 7.5)
   game_developers2 = ("Rockstar Games", "USA", "1998-12-01")
   game2 = (2, "Red Dead Redemption 2", "Action-adventure", "PC, PS4, Xbox One", "2018-10-26", 9.8)


#    if conn is not None:
#        add_games_developer(conn, game_developers)
#        add_games_developer(conn, game_developers2)
    #    add_game(conn, game)
    #    add_game(conn, game2)
#        conn.close()


def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows


def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows


def update(conn, table, id, **kwargs):
   """
   update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)



def delete_table(conn, table):
    """
    Delete all rows from the table
    :param conn: the Connection object
    :param table: table name
    :return:
    """
    sql = f''' DELETE FROM {table}'''
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)


def delete_from_table_where(conn, table, **query):
    """
    Delete rows from table with data from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    sql = f''' DELETE FROM {table} WHERE {q}'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)


conn = create_connection("database.db")
# print(select_all(conn, "games"))
# print(select_where(conn, "game_developers", id=1))
# delete_table(conn, "games")
# delete_table(conn, "game_developers")

# update(conn, "games", 1, id=2)

# conn.close()