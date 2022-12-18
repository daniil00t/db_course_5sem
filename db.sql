create table sections (
	id serial primary key,
	name text not null default 'no_name' check (length(name) < 200),
	section_outer_id integer default null,
	level integer not null default 1 check (level > 0)
);


create table articles (
	id serial primary key,
	type text not null check (type in ('default', 'official', 'private', 'internal')),
	section integer not null,
	search_indexed boolean not null,
	views integer not null check (views > 0),
	constraint "articles_to_section" 
		foreign key ("section") 
		references "sections"("id")
);

create table "groups" (
	id serial primary key,
	name text not null check (length(name) < 200),
	section integer,
	all_sections boolean not null default false,
	right_create boolean not null default false,
	right_read boolean not null default false,
	right_update boolean not null default false,
	right_delete boolean not null default false,
	right_publish boolean not null default false,
	right_review boolean not null default false,
	constraint "groups_to_section" 
		foreign key ("section") 
		references "sections"("id")
);


create table users (
	id serial primary key,
	display_name text not null check(length(display_name) < 200),
	email text not null check(length(email) < 1000),
	login text not null check(length(login) < 1000),
	password_hash text not null check(length(password_hash) < 100),
	group_id integer not null,
	created_at timestamp not null check(created_at > '2022-12-01'),
	updated_at timestamp not null check(updated_at > '2022-12-01'),
	constraint "users_to_group" 
		foreign key ("group_id") 
		references "groups"("id")
);



create table history (
	id serial primary key,
	change_at timestamp not null check(change_at > '2022-12-01'),
	change_by integer not null,
	type text not null check (type in ('create', 'update', 'delete')),
	article_id integer not null,
	contribution integer not null default 0 check (contribution >= 0),
	constraint "history_to_users" 
		foreign key ("change_by") 
		references "users"("id"),
	constraint "history_to_article" 
		foreign key ("article_id") 
		references "articles"("id")
);



create table languages (
	id serial primary key,
	name text not null check (length(name) < 100)
);


create table watchers (
	user_id integer not null,
	article_id integer not null,
	start_watch_date timestamp not null check (start_watch_date > '2022-12-01'),
	constraint "watchers_to_user" 
		foreign key ("user_id") 
		references "users"("id"),
	constraint "watchers_to_article" 
		foreign key ("article_id") 
		references "translations"("id")
);



create table translations (
	id serial primary key,
	article_id integer not null,
	title text not null check (length(title) < 500),
	short_description text not null check (length(short_description) < 2000),
	data text not null check (length(data) < 100000),
	lang integer not null,
	byte_length integer not null,
	first_source boolean not null default false,
	constraint "translatations_to_article" 
		foreign key ("article_id") 
		references "articles"("id"),
	constraint "translatations_language" 
		foreign key ("lang") 
		references "languages"("id")
);



create table templates (
	id serial primary key,
	name text not null check (length(name) < 100),
	data text not null default '<DefaultTemplate>$0</DefaultTemplate>' check (length(data) < 100000)
);