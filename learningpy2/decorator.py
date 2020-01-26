#-*- coding:utf-8 -*-

import re
import json






"""
   geneate count sql
"""
def page_interceptor(func):

    def geneator_count_sql(params,*args,**kwargs):
        func(params,*args, **kwargs)
        sql=params["sql"]
        if sql is not None and not str(sql).strip() == "" and  not str(sql).strip().startswith("select"):
            raise Exception("not found sql string")
        sql=re.sub("from","from",sql,flags=re.I|re.M)
        count_sql="select count(*) as counts from %s"%(sql[sql.find("from")+4:])
        params["count_sql"]=count_sql
        params["pageCount"]=2000
        params["totalSize"]=20000
        return params
    return geneator_count_sql



@page_interceptor
def exec_sql(params,**kwargs):
    params["sql"]="select * from adsa a left join (select * from (select aa from b) a where a>10)b on a.1=b.2 where a>10 group by aa "
    params["data"]=(1,2,3,4,5,6)
    print "execute sql ok"







if __name__ == '__main__':
    params = {
        "pageSize":0,
        "pageCount":0,
        "totalCount":0,
        "currentPage":1,
        "a":1,
        "b":2,
        "c":3
    }
    print  json.dumps(exec_sql(params))


