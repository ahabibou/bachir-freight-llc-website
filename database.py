from sqlalchemy import create_engine, text
import os

dbconnectionstring = os.environ['DB_CONNECTION_STRING']

engine = create_engine(dbconnectionstring,
     connect_args={
         "ssl": {
             "ca": ""
         }
     }
  )

with engine.connect() as conn:
  result = conn.execute(text("select * from customer"))
  print(result.all())
