-- вывести одну случайную из 100 статей, ранжируемых по количеству просмотров
-- принадлежащих секциям, уровень вложенности которых больше 2

select
  title,
  short_description,
  level,
  translations.views
from translations
inner join articles on articles.id = translations.article_id
inner join sections on sections.id = articles.section
where level > 2
ORDER BY translations.views DESC
limit 100