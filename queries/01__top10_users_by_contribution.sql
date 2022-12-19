-- Вывести топ 10 пользователей по количеству вкладов индексируемых статей

select 
  display_name,
  login,
  email,
  sum(contribution) as contribution_sum
from users 
inner join history on users.id = history.change_by
inner join translations on history.translation_id = translations.id
inner join articles on translations.article_id = articles.id
where search_indexed = true
group by users.id
order by contribution_sum desc
LIMIT 10;