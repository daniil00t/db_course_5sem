from connector import *
from faker import Faker
import random

fake = Faker()

header = ['id', 'name', 'section_outer_id', 'level']
independent_data = []

def commit_independent():
  for i in range(500):
    row = (fake.word(), None, 1)
    independent_data.append(row)
    cur.execute('insert into sections (name, section_outer_id, level) values (%s, %s, %s);', row)

  conn.commit()

def commit_dependent():
  for i in range(2, 5):
    for j in range(500):
      row = (fake.word(), random.randint(500 * (i - 2) + 1, 500 * (i - 1)), i)
      independent_data.append(row)
      cur.execute('insert into sections (name, section_outer_id, level) values (%s, %s, %s);', row)

  conn.commit()

commit_independent()
commit_dependent()