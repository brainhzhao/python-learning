#-*- coding:utf8 -*-

__author__="zhaoheng"
__version__="20191023"
__doc__="propose handle excel"

import xlrd

class HandleExcel(object):
    solution_sql_template = """insert into tbl_alarm_solution(uuid,dsc,judgment,solution,hardening,score,heat,type,is_inner,uncheck) values('%s','%s','%s','%s','%s',0,0,1,true,'%s');\n"""
    ruleid_solution_sql_template = """insert into tbl_ruleid_solution(rule_id,sol_id) values ('%s','%s');\n"""
    tbl_eventrule_sql_template="""
        update tbl_eventrule
        set judgment = '%s',
             solution='%s',
             hardening='%s'
        where uuid = '%s';
    """

    """
       handle excel
    """
    def __init__(self,fileName,*args,**kwargs):
        self.fileName = fileName
        if kwargs.get("solution_sql_file") is not None:
            try:
                self.solution_sql_file = open(kwargs.get("solution_sql_file"),"w+",encoding="utf-8",newline="\n")
            except IOError as err:
                print("solution_sql_file file not found")
        if kwargs.get("ruleid_solution_sql_file") is not None:
            try:
                self.ruleid_solution_sql_file = open(kwargs.get("ruleid_solution_sql_file"),"w+",encoding="utf-8",newline="\n")
            except IOError as err:
                print("ruleid_solution_sql_file file not found")

    """
       读取excel文件，使用xlrd库
    """
    def read_xls(self):
        excelObj = xlrd.open_workbook(self.fileName)
        sheets =excelObj.sheet_names()
        for i in range(len(sheets)):
            sheet = excelObj.sheet_by_name(sheets[i])
            sheet_row_count = sheet.nrows
            sheet_col_count = sheet.ncols
            print("begin generate sql for sheet name is %s,sheet rows' count is %d ,sheet cols count is %d" % (sheets[i],sheet_row_count,sheet_col_count))
            for row_index in range(sheet_row_count):
                if row_index == 0 :
                    continue
                row_values= sheet.row_values(row_index)
                values = (int(row_values[0]),row_values[2],row_values[3],row_values[4],row_values[5],row_values[6])
                self.solution_sql_file.write( self.solution_sql_template % values )
                self.ruleid_solution_sql_file.write(self.tbl_eventrule_sql_template % (row_values[3],row_values[4],row_values[5],int(row_values[0])))
        self.solution_sql_file.close()
        self.ruleid_solution_sql_file.close()