from db_access import SQLiteDBAccess
from settings import DB_FILEPATH
import datetime

db_ephemeris = SQLiteDBAccess(DB_FILEPATH)


# Create a handler for our get (GET) event


def get(day):
    """
    This function responds to a request for /api/ephemeris
    with the complete list of ephemeris

    :return:        list of ephemeris
    """

    # Create the list of people from our data

    try:
        date = datetime.datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        return 'Format date is incorrect. Example: AAAA-MM-DD', 400, {'x-error': 'Bad Request'}

    day_event = db_ephemeris.select('event', 'ephemeris', "day='%s' and month='%s'" %
                                    (date.strftime("%d"),
                                     date.strftime("%m")))
    month_ephemeris = db_ephemeris.select('day, event', 'ephemeris', "month='%s'" % (date.strftime("%m")))
    if len(day_event) == 0:
        day_event = None
    else:
        day_event = day_event[0][0]




    mes = {month_data[0]: month_data[1] for month_data in month_ephemeris}
    sorted(mes, key=mes.get)
    result = dict(hoy=day_event,
                  mes=mes)
    print(result)

    return result