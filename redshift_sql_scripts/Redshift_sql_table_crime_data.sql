drop table if exists crime_data;
create table crime_data(
   sid varchar(255) not null distkey sortkey,
   id varchar(255),
   pozition varchar(255),
   created_at varchar(255),
   created_meta varchar(255),
   updated_at varchar(255),
   updated_meta varchar(255),
   meta varchar(255),
   incidentnum varchar(255),
   category varchar(255),
   descript varchar(255),
   dayofweek varchar(255),
   dayte varchar(255),
   tyme varchar(255),
   pddistrict varchar(255),
   resolution varchar(255),
   address varchar(255),
   x varchar(255),
   y varchar(255),
   location varchar(255),
   pdid varchar(255)
); 