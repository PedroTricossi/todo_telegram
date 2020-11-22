import datetime
from DBConnect import connect


def deleteTask():
    conn = connect()

    cur = conn.cursor()

    today = datetime.date.today().strftime("%d.%m")

    delete_date = float(today) - 2

    cur.execute("DELETE FROM TodoTask WHERE data = (%s)",
                (delete_date, ))

    # Commit the addition
    conn.commit()

    # Finish the transaction
    cur.close()
    conn.close()
