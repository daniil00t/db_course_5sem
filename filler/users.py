from connector import *
from faker import Faker
import hashlib
import random
from datetime import datetime

fake = Faker()

#     Column     |  Type   | Collation | Nullable |              Default              
# ---------------+---------+-----------+----------+-----------------------------------
#  id            | integer |           | not null | nextval('users_id_seq'::regclass)
#  display_name  | text    |           | not null | 
#  email         | text    |           | not null | 
#  login         | text    |           | not null | 
#  password_hash | text    |           | not null | 
#  group_id      | integer |           | not null | 
#  created_at    | date    |           | not null | 
#  updated_at    | date    |           | not null | 

def main():
  for i in range(10000):
    email = fake.free_email()

    password = hashlib.sha256(email.encode('utf-8')).hexdigest()

    default = datetime.strptime('2022-12-02T00:00:00', '%Y-%m-%dT%H:%M:%S')
    now = datetime.now()
    created_at = fake.date_time_between(default, now)
    updated_at = fake.date_time_between(created_at, now)

    row = (fake.name(), email, f"{fake.word()}.{email}", password, random.randint(1, 65), created_at, updated_at)
    cur.execute('insert into users (display_name, email, login, password_hash, group_id, created_at, updated_at) values (%s, %s, %s, %s, %s, %s, %s);', row)

  conn.commit()

main()