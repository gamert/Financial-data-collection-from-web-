import baostock as bs

import pandas as pd

# 通过BaoStock获取业绩预报，
#### 登陆系统 ####

lg = bs.login()

# 显示登陆返回信息

print('login respond error_code:'+lg.error_code)

print('login respond  error_msg:'+lg.error_msg)

#### 获取公司业绩预告 ####

rs_forecast = bs.query_forecast_report("sz.300001", start_date="2020-01-01", end_date="2020-04-11")

print('query_forecast_reprot respond error_code:'+rs_forecast.error_code)

print('query_forecast_reprot respond  error_msg:'+rs_forecast.error_msg)

rs_forecast_list = []

while (rs_forecast.error_code == '0') & rs_forecast.next():

    # 分页查询，将每页信息合并在一起

    rs_forecast_list.append(rs_forecast.get_row_data())

result_forecast = pd.DataFrame(rs_forecast_list, columns=rs_forecast.fields)

#### 结果集输出到csv文件 ####

result_forecast.to_csv("G:\\forecast_report.csv", encoding="gbk", index=False)

print(result_forecast)

#### 登出系统 ####

bs.logout()

# 参数含义：
#
# · code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
#
# · start_date：开始日期，发布日期或更新日期在这个范围内；
#
# · end_date：结束日期，发布日期或更新日期在这个范围内。