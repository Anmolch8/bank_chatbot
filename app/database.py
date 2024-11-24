from sqlalchemy import create_engine,orm
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from env import setVariables
import urllib,os,pyodbc

setVariables()
params = urllib.parse.quote_plus(f"DRIVER={os.environ.get('DBDriver')};"
                                 f"SERVER={os.environ.get('SERVER')};"
                                 f"DATABASE={os.environ.get('DATABASE')};"
                                  "Trusted_Connection=yes;")
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
mapper_registry = orm.registry()

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)
    mapper_registry.metadata.create_all(engine)


if __name__=='__main__':
   init_db()
 