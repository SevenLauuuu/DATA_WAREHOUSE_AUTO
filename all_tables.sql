--来源
drop table check.connection_info;
create table check.connection_info
(
cid string -- 数据库来源编号
,cname string  --数据来源名称
,cenvi    string -- DI/UAT/PRD环境
,ctype   string  --类型 MYSQL/KUDU/HIVE 
,cip string 
,cport string  
,cdb string  --数据库名
,cuser string  --用户名
,status string    --有效状态
,updated_time string 
,updated_user string 
)comment '数据仓库-ods层-连接表信息' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' ;

drop table check.dw_ods_table;
create table check.dw_ods_table(
fid string 
,fsrc_id string   --来源ID 
,fdest_id string  --去向ID
,status string    --有效状态
,updated_time string 
,updated_user string
,version    string  -- 版本信息
)comment '数据仓库-dwd层-实体表' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' ;


drop table check.dw_dwd_table;
create table check.dw_dwd_table(
fid string 
,cols string --字段
,tbl string --表名
,tbl_desc string --备注
,db string --数据库
,where_rules string --规则1
,group_rules string --规则2
,having_rules string --规则3
,status string    --有效状态
,updated_time string 
,updated_user string
,version    string  -- 版本信息
)comment '数据仓库-dwd层-实体表' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' ;


alter table check.dwd_amc_tbl_relations add columns (updated_time string comment  "变更时间",updated_user string comment "变更人");
drop table check.dwd_amc_tbl_relations;
create table check.dwd_amc_tbl_relations(
target_tbl string --目的表 
,target_cols string--目的列
,fid string 
,tbl_alias string --表别名 
,join_type string --连接类型,
,join_on string --连接关系
,status string    --有效状态
,updated_time string 
,updated_user string 
)comment '数据仓库-dwd层-dwd表的连接关系' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' ;

--指标输出表
drop table check.ads_table;
create table check.ads_table
(
tid string   --表编号
,tsource string  --表来源 connection_info -> cid
,tname string --表名称 
,tdesc string -- 表备注
,ttags string -- 表的标签、类别
,tfid string  -- 表的列
,tcomment string --列的对应注释
,status string    --有效状态
,updated_time string 
,updated_user string 
)comment '数据仓库-ads层-ads表' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' ;

--指标表 基础指标 父指标
drop table check.f_simple_quotas;
create table check.f_simple_quotas
(
qid string   --
,qname string 
,qsource string  --来源
,qtime_range string --时间段 
,qchange_list string   --可替换参数列表
,qchild_list  string   --子指标列表
,version    string  -- 版本信息
,status string    --有效状态
,updated_time string 
,updated_user string 
)comment '数据仓库-基础指标表' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' ;


--指标表 复杂指标
drop table check.f_complex_quotas;
create table check.f_complex_quotas
(
ccid string  
,data_caliber  string --数据统计口径
,effect_id string    -- 被影响的指标
,version    string  -- 版本信息
,status string    --有效状态
,updated_time string 
,updated_user string 
)comment '数据仓库-第二次加工指标表' ROW FORMAT DELIMITED FIELDS TERMINATED BY '\001'  LINES TERMINATED BY '\n' ;
