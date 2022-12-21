-- вывести топ 10 пользователей по количеству подписок на статьи, 
-- просмотры которых превышают средний показатель всех просмотров статей

with counts as (
  select 
    avg(views) as avg_views
  from translations
)
select 
  display_name,
  email,
  count(watchers.article_id)
from users
inner join watchers on watchers.user_id = users.id
inner join translations on watchers.article_id = translations.id
inner join counts on 1 = 1
where views > avg_views
group by display_name, email
order by count(watchers.article_id) desc
limit 10