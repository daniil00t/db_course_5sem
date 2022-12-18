from connector import *
from faker import Faker
import random
from datetime import datetime

fake = Faker()

#       Column      |            Type             | Collation | Nullable | Default 
# ------------------+-----------------------------+-----------+----------+---------
#  user_id          | integer                     |           | not null | 
#  article_id       | integer                     |           | not null | 
#  start_watch_date | timestamp without time zone |           | not null | 

def main():
  for i in range(5000):
    default = datetime.strptime('2022-12-02T00:00:00', '%Y-%m-%dT%H:%M:%S')
    now = datetime.now()
    start_watch_date = fake.date_time_between(default, now)

    row = (random.randint(1, 10000), random.randint(1, 100000), start_watch_date)

    cur.execute('insert into watchers (user_id, article_id, start_watch_date) values (%s, %s, %s);', row)

  conn.commit()

main()