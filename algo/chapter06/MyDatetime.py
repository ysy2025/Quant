from datetime import datetime, timedelta

if __name__ == '__main__':
    now = datetime.now()
    print(now)

    dt = datetime(2023, 1, 1, 00, 00)
    print(dt)

    now_dt = datetime.timestamp(now)
    print(now_dt)

    a_dt = datetime.fromtimestamp(1111111111.0)
    print(a_dt)

    str_time = datetime.strptime("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    print(str_time)

    time_str = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
    print(time_str)