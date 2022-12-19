from connector import *
from faker import Faker
import random

fake = Faker()

#       Column       |  Type   | Collation | Nullable | Default 
# -------------------+---------+-----------+----------+---------
#  article_id        | integer |           | not null | 
#  title             | text    |           | not null | 
#  short_description | text    |           | not null | 
#  data              | text    |           | not null | 
#  lang              | integer |           | not null | 
#  byte_length       | integer |           | not null | 
#  first_source      | boolean |           | not null | false

def main():
  # сначала заполняем для каждой целевой статьи, чтобы у нее был как минимум один перевод
  for i in range(1, 10000):
    title = fake.sentence(nb_words=6, variable_nb_words=False)
    short_description = fake.paragraph(nb_sentences=5)
    data = f"<DefaultTemplate>{fake.paragraph(nb_sentences=30)}</DefaultTemplate>"
    lang = random.randint(1, 249)
    byte_length = len(data) * 8
    first_source = True
    views = random.randint(1, 100000)
    row = (i, title, short_description, data, lang, byte_length, first_source, views)
    
    cur.execute('insert into translations (article_id, title, short_description, data, lang, byte_length, first_source, views) values (%s, %s, %s, %s, %s, %s, %s, %s);', row)


  for i in range(90000):
    title = fake.sentence(nb_words=6, variable_nb_words=False)
    short_description = fake.paragraph(nb_sentences=5)
    data = f"<DefaultTemplate>{fake.paragraph(nb_sentences=30)}</DefaultTemplate>"
    lang = random.randint(1, 249)
    byte_length = len(data) * 8
    first_source = False
    views = random.randint(1, 100000)
    row = (random.randint(1, 10000), title, short_description, data, lang, byte_length, first_source, views)
    
    cur.execute('insert into translations (article_id, title, short_description, data, lang, byte_length, first_source, views) values (%s, %s, %s, %s, %s, %s, %s, %s);', row)

  conn.commit()

main()