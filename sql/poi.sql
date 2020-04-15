create table poi
(
	gid serial,
	name varchar(100),
	p_name VARCHAR(50),
	c_name VARCHAR(50),
	d_name VARCHAR(50),
	d_code VARCHAR(10),
	tel VARCHAR(50),
	address VARCHAR(200),
	area VARCHAR(50),
	b_c VARCHAR(50),
	s_c VARCHAR(50),
	poi_x DECIMAL(10,6),
	poi_y DECIMAL(10,6)
);
alter table poi add primary key (gid);


create table poi
(
	gid serial,
	code varchar(10),
	name varchar(100),
	poi_x DECIMAL(10,6),
	poi_y DECIMAL(10,6),
	address VARCHAR(200)
);

alter table poi add primary key (gid);

select addgeometrycolumn('','poi', 'geom', '4326', 'POINT', 2);