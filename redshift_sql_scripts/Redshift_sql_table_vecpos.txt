# Purge Redshift of old table and create new vehicle_position table

drop table if exists vehicle_position;
create table vehicle_position(
	vehicle_id varchar(255) not null distkey sortkey,
	t_stamp varchar(255),
	position_latitude varchar(255),
	position_longitude varchar(255),
	trip_id varchar(255),
	agency varchar(255)
	);	
