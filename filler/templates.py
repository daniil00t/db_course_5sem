from connector import *
from faker import Faker
import random

fake = Faker()

#  Column |  Type   | Collation | Nullable |                    Default                    
# --------+---------+-----------+----------+-----------------------------------------------
#  id     | integer |           | not null | nextval('templates_id_seq'::regclass)
#  name   | text    |           | not null | 
#  data   | text    |           | not null | '<DefaultTemplate>$0</DefaultTemplate>'::text

def main():
  for i in range(100):
    name = "_".join(fake.words(nb=3))
    row = (name, f"<{name}>$0</{name}>")
    cur.execute('insert into templates (name, data) values (%s, %s);', row)

  conn.commit()

main()