-- Вывести всех пользователей, которые создали хотя бы 1 статью
-- хотя бы с половиной от среднго числа всех переводов позже 8 декабря 2022

with counts as (
  select
    article_id,
    count(1) as total_count_translations
  from translations
  group by article_id
),
calculations as (
  select avg(total_count_translations) as avg_total_count_translations from counts
),
sorted_translations as (
  select
    article_id
  from translations
  inner join calculations on 1=1
  inner join history on history.translation_id = translations.id
  where change_at > '2022-12-08'
  group by article_id, avg_total_count_translations
  having count(article_id) > avg_total_count_translations / 2
)
select 
  distinct sorted_translations.article_id, display_name, login, title
from users
inner join history on history.change_by = users.id
inner join translations on history.translation_id = translations.id
inner join sorted_translations on sorted_translations.article_id = translations.article_id
where 
  history.type = 'create'
