# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  DataFormat.py    
@Desc   :  
@Author :  byfan
@Time   :  2022/3/3 23:06 
'''

class DateFormat:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        print(f"输入的时间为{self.year}年，{self.month}月，{self.day}日")

    @classmethod
    def json_format(cls, js_data):
        """
        输入一个字典格式的数据信息，返回一个元组
        """
        # 使用[key]访问键对应的值
        year, month, day = js_data['year'], js_data['month'], js_data['day']
        return cls(year, month, day)


json_data = {'year': 2021, 'month': 12, 'day': 7}
# 使用json格式化，生成想要的日期格式，返回一个DataFormat的实例
demo = DateFormat.json_format(json_data)
demo.out_date()
demo.year = "2022"
demo.out_date()
print(type(demo))



# if __name__ == "__main__":
#     print("Hello Word!")
