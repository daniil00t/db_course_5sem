from connector import *
from faker import Faker
import random
from datetime import datetime

fake = Faker()

#     Column    |            Type             | Collation | Nullable |               Default               
# --------------+-----------------------------+-----------+----------+-------------------------------------
#  id           | integer                     |           | not null | nextval('history_id_seq'::regclass)
#  change_at    | timestamp without time zone |           | not null | 
#  change_by    | integer                     |           | not null | 
#  type         | text                        |           | not null | 
#  article_id   | integer                     |           | not null | 
#  contribution | integer                     |           | not null | 0

types = ['create', 'update', 'delete']

def main():
  for i in range(100000):
    default = datetime.strptime('2022-12-02T00:00:00', '%Y-%m-%dT%H:%M:%S')
    now = datetime.now()
    change_at = fake.date_time_between(default, now)

    row = (change_at, random.randint(1, 10000), types[random.randint(0, 2)], random.randint(1, 10000), random.randint(1, 150))
    cur.execute('insert into history (change_at, change_by, type, article_id, contribution) values (%s, %s, %s, %s, %s);', row)

  conn.commit()

main()