# Purge Redshift of old table and create new operator_list table

drop table if exists operator_list;
create table operator_list(
	Id varchar(255) not null distkey sortkey,
	LastGenerated varchar(255),
	Name varchar(255)
	);
