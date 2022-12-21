-- вывести примереное время скачивания всех индексируемых статей, созданных 
-- позже 8 декабаря 2022 из секции, уровень вложенности которых равный 3

-- средняя скорость скачивания 2Мбит/с

select
  article_id as id,
  byte_length,
  sum(byte_length) / 512 as time_in_seconds
from translations
inner join articles on articles.id = translations.article_id
inner join history on history.translation_id = translations.id
inner join sections on articles.section = sections.id
where 
  change_at > '2022-12-8' and
  sections.level = 3
group by article_id, byte_length