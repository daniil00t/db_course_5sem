from connector import *
from faker import Faker
import pycountry

fake = Faker()

#  Column |  Type   | Collation | Nullable |                Default                
# --------+---------+-----------+----------+---------------------------------------
#  id     | integer |           | not null | nextval('languages_id_seq'::regclass)
#  name   | text    |           | not null | 

def main():
  for i in [country.alpha_2 for country in pycountry.countries]:
    cur.execute('insert into languages (name) values (%s);', [i])

  conn.commit()

main()