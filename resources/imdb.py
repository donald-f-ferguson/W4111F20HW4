from orm.imdb_orm import NameBasicsFixed as NameBasicsFixed
from sqlalchemy.orm import sessionmaker
import json

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://dbuser:dbuserdbuser@localhost:3306/aaaimdbf20fixed')
Session = sessionmaker(bind=engine)
session = Session()

def t1():
    res = session.query(NameBasicsFixed).filter_by(primary_name='Tom Hanks')
    for r in res:
        print("res = ", r)
        print("Professions = ")
        for p in r.professions:
            print("\t", p)


t1()