#!/usr/bin/python
# -*- coding: utf-8 -*-
#author:ytliu 
#date:2019-03-07
#**
# ////////////////////////////////////////////////////////////////////
# //                          _ooOoo_                               //
# //                         o8888888o                              //
# //                         88" . "88                              //
# //                         (| ^_^ |)                              //
# //                         O\  =  /O                              //
# //                      ____/`---'\____                           //
# //                    .'  \\|     |//  `.                         //
# //                   /  \\|||  :  |||//  \                        //
# //                  /  _||||| -:- |||||-  \                       //
# //                  |   | \\\  -  /// |   |                       //
# //                  | \_|  ''\---/''  |   |                       //
# //                  \  .-\__  `-`  ___/-. /                       //
# //                ___`. .'  /--.--\  `. . ___                     //
# //              ."" '<  `.___\_<|>_/___.'  >'"".                  //
# //            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 //
# //            \  \ `-.   \_ __\ /__ _/   .-` /  /                 //
# //      ========`-.____`-.___\_____/___.-`____.-'========         //
# //                           `=---='                              //
# //      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        //
# //         佛祖保佑         再无Bug                   //
# ////////////////////////////////////////////////////////////////////
# User:ytliu
# Date:2019-03-07
#/

import os 
import sys
import loadsJson
import rh_hive_conn 

####################################################################################################################
if __name__ == '__main__':

	error = 0
	param=sys.argv[1]
	print param

  	oracle_host,oracle_port,oracle_servicename,oracle_user,oracle_password,oracle_database,oracle_table,hive_host,hive_port,hive_user,hive_password,hive_database,dest_table,add_param,day_interval,p1,p2,p3,task_name,run_serial_no,inc_start,inc_end,hive_queue=loadsJson.JsonPythonInstance(param)

  	print dest_table 
  	src_host = oracle_host 
  	src_port = oracle_port
  	authMechanism = "PLAIN"
  	src_user = oracle_user
  	src_passwd = oracle_password
  	src_db = oracle_database

  	hive_instance = rh_hive_conn.HiveClient(src_host,src_port,authMechanism,src_user,src_passwd,src_db)


  	drop_create_tbl_sql = "drop table %s.%s"%(hive_database,dest_table)
  	hive_instance.execute_hive_sql_no_return(drop_create_tbl_sql)


  	exe_create_tbl_sql = "\
	select  \
	concat(\" create table %s.%s as select  \",concat_ws(\",\",collect_set(target_cols)),\" from \",concat_ws(\" left join \",collect_set(concat(dat.alias_name,\" \", datr.tbl_alias ,\" \",case when datr.join_type != \"0\" then concat(\" on \",datr.join_on) else \" \"  end)))) \
	from \
	(\
	    SELECT * FROM check.dwd_amc_tbl_relations  where target_tbl = \"%s.%s\"  ORDER BY cast(substring(tbl_alias,2,length(tbl_alias)-1) as int)  \
	)datr left join \
	(\
		select \
		concat(\"( select \",cols,\" from \",\
		tbl\
		,case when where_rules != \"1=1\" then concat(\" where \", where_rules ) else \" \" end  \
		,case when group_rules != \"1=1\" then concat(\" group by \",group_rules) else \" \" end,\" ) \",\" \" ) alias_name ,\
		fid,\
		tbl\
		from check.dwd_amcs_table\
	)dat on datr.fid = dat.fid "%(hive_database,dest_table,hive_database,dest_table)

	print exe_create_tbl_sql
	file_path = '/data/etlscript/CMRH_ODS/SCRIPT/%s_%s.sql'%(hive_database,dest_table)
	try:
		f=open(file_path)
		f.write(exe_create_tbl_sql)
	except:
		pass

	
	tbl_componet_sql = hive_instance.get_hive_all_result(exe_create_tbl_sql)

	print "生成 %s.%s 表的创建语句"%(hive_database,dest_table)
	print tbl_componet_sql


	hive_instance.execute_hive_sql_no_return(tbl_componet_sql[0][0])
	print "完成执行 %s.%s 表的创建语句"%(hive_database,dest_table)

	hive_instance.close()

