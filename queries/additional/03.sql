-- Задача: Сделать merged поиск для дата-колонок переводов

-- Пояснение: пусть пользователь задал регулярку
-- ему нужно отдать все строки, в колонках которых есть хотя бы один матч

-- пусть пользователь задал регулярку %(C|c)ould%

-- OR
with const as (
  select '%(C|c)ould%' as regexp
)
select
  id,
  data,
  title,
  short_description
from translations
inner join const on 1 = 1
where
  title similar to const.regexp or
  short_description similar to const.regexp or
  data similar to const.regexp;


-- AND
with const as (
  select '%(C|c)ould%' as regexp
)
select
  id,
  data,
  title,
  short_description
from translations
inner join const on 1 = 1
where
  title similar to const.regexp and
  short_description similar to const.regexp and
  data similar to const.regexp;