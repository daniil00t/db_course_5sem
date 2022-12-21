-- Задача: Найти всех пользователей, которые ТОЛЬКО редактировали статьи

-- здесь просто можно выделить всех пользователей, которые удаляли и создавали статьи
-- а потом просто написать except, потом заджоинить их с табличкой пользововатей

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
  id,
  display_name,
  login,
  email
from users
inner join only_update on only_update.change_by = users.id
order by id