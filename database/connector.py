import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
import json

DB_URI = 'postgresql://postgres:253768491@127.0.0.1:5432/proyectodbp'

class Manager:
    Base = declarative_base()
    session = None

    def create_engine(self):
        engine = sqlalchemy.create_engine(DB_URI)
        self.Base.metadata.create_all(engine)
        return engine

    def get_session(self, engine):
        if self.session == None:
            Session = sessionmaker(bind=engine)
            session = Session()
        return session

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None

            return fields

        return json.JSONEncoder.default(self, obj)
