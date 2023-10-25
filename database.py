from sqlalchemy import create_engine, text

dbconnectionstring = "mysql+pymysql://uvh0v5szkepar1pmg04w:pscale_pw_1YA3KF4u9UoaEK5l0prkuOdoZyKrCAMjXP2EobP3La7@aws.connect.psdb.cloud/bachirfreight?charset=utf8mb4"

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
