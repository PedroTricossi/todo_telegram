import datetime
from Database import QueryTask


def ReturnTask(message):
    if message == 'All':
        results = QueryTask.queryAll()

    elif message == 'Hoje':
        today = datetime.date.today()
        d1 = today.strftime("%d.%m")
        date = float(d1)

        results = QueryTask.queryByDate(date)

    elif message == 'Ontem':
        today = datetime.date.today()
        d1 = today.strftime("%d.%m")
        date = float(d1) - 1

        results = QueryTask.queryByDate(date)

    elif message == 'Amanhã':
        today = datetime.date.today()
        d1 = today.strftime("%d.%m")
        date = float(d1) + 1

        results = QueryTask.queryByDate(date)

    else:
        try:
            date = float(message)

            results = QueryTask.queryByDate(date)

        except:
            priority = message

            results = QueryTask.queryByPriority(priority)

    return results
