import psycopg2
from Database.DBConnect import connect


def queryByDate(date):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM TodoTask WHERE data = (%s)", (date, ))

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results


def queryByPriority(priority):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM TodoTask WHERE priority = (%s)", (priority, ))

    results = cur.fetchall()
    cur.close()
    conn.close()

    return results


def queryAll():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM TodoTask;")

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results
