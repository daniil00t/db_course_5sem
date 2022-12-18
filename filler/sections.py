from connector import *
from faker import Faker
import random

fake = Faker()

#       Column      |  Type   | Collation | Nullable |               Default                
# ------------------+---------+-----------+----------+--------------------------------------
#  id               | integer |           | not null | nextval('sections_id_seq'::regclass)
#  name             | text    |           | not null | 'no_name'::text
#  section_outer_id | integer |           |          | 
#  level            | integer |           | not null | 1


def commit_independent():
  for i in range(500):
    row = (fake.word(), None, 1)
    cur.execute('insert into sections (name, section_outer_id, level) values (%s, %s, %s);', row)

  conn.commit()

def commit_dependent():
  for i in range(2, 5):
    for j in range(500):
      row = (fake.word(), random.randint(500 * (i - 2) + 1, 500 * (i - 1)), i)
      cur.execute('insert into sections (name, section_outer_id, level) values (%s, %s, %s);', row)

  conn.commit()

commit_independent()
commit_dependent()