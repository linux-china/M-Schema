import os
from schema_engine import SchemaEngine
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select, text

db_name= 'aan_1'
db_path = f'./{db_name}.sqlite'
abs_path = os.path.abspath(db_path)
assert os.path.exists(abs_path)
db_engine = create_engine(f'sqlite:///{abs_path}')
schema_engine = SchemaEngine(engine=db_engine, db_name=db_name)
mschema = schema_engine.mschema
print(mschema.to_mschema())
mschema.save(f'./{db_name}.json')

