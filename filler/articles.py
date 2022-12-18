from connector import *
from faker import Faker
import random

fake = Faker()

header = ['id', 'type', 'section', 'search_indexed', 'views']
types = ['default', 'official', 'private', 'internal']

def main():
  for i in range(10000):
    row = (types[random.randint(0, 3)], random.randint(1, 2000), random.random() > 0.5, random.randint(1, 10000))
    cur.execute('insert into articles (type, section, search_indexed, views) values (%s, %s, %s, %s);', row)

  conn.commit()

main()