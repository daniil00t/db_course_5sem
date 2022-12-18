from connector import *
from faker import Faker
import random

fake = Faker()

#     Column     |  Type   | Collation | Nullable |              Default               
# ---------------+---------+-----------+----------+------------------------------------
#  id            | integer |           | not null | nextval('groups_id_seq'::regclass)
#  name          | text    |           | not null | 
#  section       | integer |           | not null | 
#  all_sections  | boolean |           | not null | false
#  right_create  | boolean |           | not null | false
#  right_read    | boolean |           | not null | false
#  right_update  | boolean |           | not null | false
#  right_delete  | boolean |           | not null | false
#  right_publish | boolean |           | not null | false
#  right_review  | boolean |           | not null | false

def addFill(binary, n):
  if(len(binary) == n):
    return binary
  return '0' * (n - len(binary)) + binary

def main():
  n = 6
  for i in range(2 ** n):
    binary = addFill(bin(i)[2:], n)
    (right_create, right_read, right_update, right_delete, right_publish, right_review) = binary
    row = (fake.word(), None, False, bool(int(right_create)), bool(int(right_read)), bool(int(right_update)), bool(int(right_delete)), bool(int(right_publish)), bool(int(right_review)))
    cur.execute('insert into groups (name, section, all_sections, right_create, right_read, right_update, right_delete, right_publish, right_review) values (%s, %s, %s, %s, %s, %s, %s, %s, %s);', row)

  conn.commit()

main()