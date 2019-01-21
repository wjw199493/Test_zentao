from xlutils.copy import copy
import xlrd
import xlwt

import time
class Excel_dx():

    def du (self,h,l):
        #path = 'F:/untitled/我的坚果云/git/zentao/comm/case.xls'
        path = 'case.xls'
        workbook = xlrd.open_workbook(path)
        data_sheet = workbook.sheets()[0]
        ss =data_sheet.cell_value(h,l)#将字符串转为字典
        return ss

    def bt(self,a):
        name = ['ID','用例名称','API地址','是否执行','请求类型','请求头','测试类型','是否需要登陆',
                '依赖caseid','请求参数','状态码','返回结果','执行结果','断言','执行时间']

        line = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        meter = dict(zip(name,line))
        #print (meter)
        A = a

        return meter[A]
    def xg(self,h,l,vale):

        #style = xlwt.XFStyle()
        read_file = xlrd.open_workbook('case.xls', formatting_info=True)
        # 参数注释：
        # file_path：文件路径，包含文件的全名称
        # formatting_info=True：保留Excel的原格式

        # 将文件复制到内存
        write_data = copy(read_file)

        # 读取复制后文件的sheet1
        write_save = write_data.get_sheet(0)

        # 写入数据
        style = xlwt.easyxf('align: wrap on')#自动换行
        write_save.write(h,l,vale,style)
        # 参数注释：
        # x,y:写入目标格的位置坐标
        # value：写入数据

        # 保存写入数据后的文件到原文件路径
        write_data.save('case.xls')

if __name__=="__main__":
    a = Excel_dx()
    self = "pass"
    aa = a.bt(1)
    print (aa)