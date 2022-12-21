-- 1: Найти всех пользователей, которые ТОЛЬКО редактировали статьи
-- Задача: среди этих пользоватей найти тех, кто редактировал ровно одну статью


with only_update as (
  select 
    change_by
  from history
  except
  select
    change_by
  from history
  where type in ('create', 'delete')
)
select 
  users.id as id,
  display_name,
  login,
  email
from history
inner join only_update on history.change_by = only_update.change_by
inner join users on users.id = history.change_by
group by history.change_by, users.id
having count(distinct translation_id) = 1
order by history.change_by