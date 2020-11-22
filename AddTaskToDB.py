import psycopg2
from DBConnect import connect


def adicionaTask():
    conn = connect()

    cur = conn.cursor()

    # Table -> data, task e priority

    # Get information about he task to save in database
    data = float(input("Data de entrega: "))

    task = input("Tarefa: ")

    priority = input("Prioridade: ")

    # Insert data into database
    cur.execute("INSERT INTO TodoTask (data, task, priority) VALUES (%s, %s, %s)",
                (data, task, priority))

    # Commit the addition
    conn.commit()

    # Finish the transaction
    cur.close()
    conn.close()


def main():
    adicionaTask()


if __name__ == "__main__":
    main()
