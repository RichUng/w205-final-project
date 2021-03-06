# Purge Redshift of old table and create new data_feed table

drop table if exists data_feed;
create table data_feed(
	route_id varchar(255) not null distkey sortkey,
	service_id varchar(255),
	trip_id varchar(255),
	trip_headsign varchar(255),
	direction_id varchar(255),
	block_id varchar(255),
	shape_id varchar(255),
	trip_short_name varchar(255),
	bikes_allowed varchar(255),
	wheelchair_accessible varchar(255),
	agency varchar(255)
	);
