# DATA_WAREHOUSE_AUTO
自动生成DWD表，主要运用的是详表

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
整体处理思路
1. 判断组成表的etl_time时间是否在T+1更改过规则或者表提示信息，
      若有则走规则步骤２；
      若无则执行本地保存好的SQL文件；
        　执行成功完后返回信息；
         若本地文件被破坏，则走步骤２；
      
2. 生成重新运行生成DWD表的SQL，先保存到本地，然后运行，成功后返回成功信息；

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
--table	属性	comments
fid	string	编号
cols	string	字段
tbl	string	表名
tbl_desc	string	备注
db	string	数据库
where_rules	string	规则1
group_rules	string	规则2
having_rules	string	规则3
etl_time string    时间
etl_users  string 


－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
--tbl_relations	属性	comments
target_tbl	string	目的表
target_cols	string	目的列
fid	string	
tbl_alias	string	表别名
join_type	string	连接类型,1：left join
join_on	string	连接关系
etl_time string    时间
etl_users  string 

