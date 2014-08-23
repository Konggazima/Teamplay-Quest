from datetime import datetime, timedelta

def kstime(hours):
    tm = datetime.now()
    fulldate = datetime(tm.year, tm.month, tm.day, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + timedelta(hours=hours)
    return fulldate