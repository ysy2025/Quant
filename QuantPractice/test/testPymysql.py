import pandas as pd
import os
import sqlalchemy

def ali_connect_db():
    engine = 1
    return engine


if __name__ == '__main__':
    ali_engine = ali_connect_db()
    test = pd.read_sql("show tables", ali_engine)
    test.head()

    os.environ.add