-- вывести промежуток вермени между 
-- созданием и последним изменением статьи, если изменение есть, если же нет, 
-- вывести в соотвествующей ячейках нулл

-- select 
--   translation_id,
--   min(change_at) as created_at,
--   max(change_at) as last_updated_at,
--   (case when tstzrange(min(change_at), max(change_at)) = 'empty' then null
--       else max(change_at) - min(change_at)
--       end) as interval_u_c
-- from history
-- where type in ('create', 'update')
-- group by translation_id
-- limit 100;

-- далее посчитать минимальную, максимальную и среднию
-- длину интервала для предыдущего запроса

with intervals as (
  select 
    translation_id,
    min(change_at) as created_at,
    max(change_at) as last_updated_at,
    (case when tstzrange(min(change_at), max(change_at)) = 'empty' then null
        else max(change_at) - min(change_at)
        end) as interval_u_c
  from history
  where type in ('create', 'update')
  group by translation_id
  limit 100
)
select 
  min(interval_u_c),
  max(interval_u_c),
  avg(interval_u_c)
from intervals;