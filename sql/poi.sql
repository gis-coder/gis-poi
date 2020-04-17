-- 1、建表时表名以tb_开头，字段以f_开头
-- 2、每个表的字段都需注明注释，部分字段需要注明取值范围


-- 兴趣点表存储兴趣点数据
create table tb_poi
(
	f_gid serial,
	f_name varchar(100),
	f_pname VARCHAR(50),
	f_cname VARCHAR(50),
	f_dname VARCHAR(50),
	f_dcode VARCHAR(10),
	f_tel VARCHAR(50),
	f_address VARCHAR(200),
	f_area VARCHAR(50),
	f_b VARCHAR(50),
	f_s VARCHAR(50),
	f_x DECIMAL(10,6),
	f_y DECIMAL(10,6)
);

COMMENT ON COLUMN "public"."tb_poi"."f_gid" IS '主键';
COMMENT ON COLUMN "public"."tb_poi"."f_name" IS '名称';
COMMENT ON COLUMN "public"."tb_poi"."f_pname" IS '省';
COMMENT ON COLUMN "public"."tb_poi"."f_cname" IS '市';
COMMENT ON COLUMN "public"."tb_poi"."f_dname" IS '县';
COMMENT ON COLUMN "public"."tb_poi"."f_dcode" IS '编码';
COMMENT ON COLUMN "public"."tb_poi"."f_tel" IS '电话';
COMMENT ON COLUMN "public"."tb_poi"."f_address" IS '地址';
COMMENT ON COLUMN "public"."tb_poi"."f_area" IS '区域';
COMMENT ON COLUMN "public"."tb_poi"."f_b" IS '大分类';
COMMENT ON COLUMN "public"."tb_poi"."f_s" IS '小分类';
COMMENT ON COLUMN "public"."tb_poi"."f_x" IS '经度';
COMMENT ON COLUMN "public"."tb_poi"."f_y" IS '纬度';

alter table tb_poi add primary key (f_gid);

-- select addgeometrycolumn('','poi', 'geom', '4326', 'POINT', 2);


-- 行政区数据存储信息
create table tb_region
(
	f_gid serial,
	f_name varchar(100),
	f_level integer,
	f_code varchar(10),
	f_pcode varchar(10),
	f_east DECIMAL(10,6),
	f_west DECIMAL(10,6),
	f_north DECIMAL(10,6),
	f_south DECIMAL(10,6)
);

COMMENT ON COLUMN "public"."tb_region"."f_gid" IS '主键';
COMMENT ON COLUMN "public"."tb_region"."f_name" IS '名称';
COMMENT ON COLUMN "public"."tb_region"."f_level" IS '等级';
COMMENT ON COLUMN "public"."tb_region"."f_code" IS '编码';
COMMENT ON COLUMN "public"."tb_region"."f_pcode" IS '父级编码';
COMMENT ON COLUMN "public"."tb_region"."f_east" IS '东';
COMMENT ON COLUMN "public"."tb_region"."f_west" IS '西';
COMMENT ON COLUMN "public"."tb_region"."f_north" IS '北';
COMMENT ON COLUMN "public"."tb_region"."f_south" IS '南';

alter table tb_region add primary key (f_gid);

select addgeometrycolumn('','tb_region', 'geom', '4326', 'MULTIPOLYGON', 2);