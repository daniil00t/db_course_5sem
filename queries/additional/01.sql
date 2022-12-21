-- вывести всех пользоватей, которые только только редактировали статьи

select
  users.id
from history
inner join users on users.id = history.change_by
group by users.id
having type = 'upadte' and type not in ('create', 'delete')
limit 200;