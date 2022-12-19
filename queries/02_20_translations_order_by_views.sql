-- Вывести 20 последних переводов статей ранжируемых по количеству просмотров 
-- и измененных позже 12 декабря 2022 года пользователем, имеющим права на изменине 
-- всех разделов

select 
  translations.id, 
  title, 
  short_description, 
  updated_at, 
  views
from translations
inner join history on history.translation_id = translations.id
inner join users on users.id = history.change_by
inner join groups on groups.id = users.group_id
where 
  history.change_at > '2022-12-12' and
  all_sections = true
order by views desc, updated_at desc
limit 20
