import matplotlib.pyplot as plt

import matplotlib as mpl

from pandas.core.frame import DataFrame

import time

#import Chinese as fnt

import pandas as pd

import numpy as np

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from pylab import *

stock_code = '603118'
base_path = './数据-下载/'

# 1、基本面数据下载

tables = pd.read_html("http://quotes.money.163.com/f10/zycwzb_" + stock_code + ",year.html")

i = 0

for table in tables:

    if i == 4:

        df_tmp = DataFrame(table)

        df_tmp.insert(0, '分类',

                      ['报告日期', '基本每股收益(元)', '每股净资产(元)', '每股经营活动产生的现金流量净额(元)', '主营业务收入(万元)', '主营业务利润(万元)', '营业利润(万元)',
                       '投资收益(万元)', '营业外收支净额(万元)', '利润总额(万元)', '净利润(万元)', '净利润(扣除非经常性损益后)(万元)', '经营活动产生的现金流量净额(万元)',
                       '现金及现金等价物净增加额(万元)', '总资产(万元)', '流动资产(万元)', '总负债(万元)', '流动负债(万元)', '股东权益不含少数股东权益(万元)',
                       '净资产收益率加权(%)'])

        df_tmp.to_excel(base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-年度.xlsx')

    elif i == 5:

        DataFrame(table).to_excel(

            base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-盈利能力.xlsx')

    elif i == 6:

        DataFrame(table).to_excel(

            base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-偿还能力.xlsx')

    elif i == 7:

        DataFrame(table).to_excel(

            base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-成长能力.xlsx')

    elif i == 8:

        DataFrame(table).to_excel(

            base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-营运能力.xlsx')

    elif i == 1:

        DataFrame(table).to_excel(

            base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-基本资料.xlsx')

    i += 1

# 2、数据可视化分析

'''

项目及索引值

0 报告日期

1 基本每股收益(元)

2 每股净资产(元)

3 每股经营活动产生的现金流量净额(元)

4 主营业务收入(万元)

5 主营业务利润(万元)

6 营业利润(万元)

7 投资收益(万元)

8 营业外收支净额(万元)

9 利润总额(万元)

10 净利润(万元)

11 净利润(扣除非经常性损益后)(万元)

12 经营活动产生的现金流量净额(万元)

13 现金及现金等价物净增加额(万元)

14 总资产(万元)

15 流动资产(万元)

16 总负债(万元)

17 流动负债(万元)

18 股东权益不含少数股东权益(万元)

19 净资产收益率加权(%)

'''

# 设置绘图全局变量

mpl.rcParams['axes.titlesize'] = 10

mpl.rcParams['xtick.labelsize'] = 9

mpl.rcParams['ytick.labelsize'] = 9

mpl.rcParams['axes.labelsize'] = 9

mpl.rcParams['xtick.major.size'] = 0

mpl.rcParams['ytick.major.size'] = 0

mpl.rcParams['lines.linewidth'] = 0.5

mpl.rcParams['lines.markersize'] = 5

#fnt.set_ch('YH', 12)

stock_name = \
 \
pd.read_excel(base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-基本资料.xlsx').ix[

    0, 0].replace(' ', '')

df_jbcwzb = pd.read_excel(

    base_path + stock_code + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-年度.xlsx')

data_reportDate = df_jbcwzb.ix[0, 1:].sort_index(ascending=False)

plt.figure(figsize=(18, 11))

# plt.tight_layout()

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, hspace=0.8, wspace=0.6)

# 1、图一：基本每股收益

ax = plt.subplot2grid((3, 1), (0, 0))

data_jbmgsy = df_jbcwzb.ix[1, 1:].replace('--', '0').sort_index(ascending=False)

data_mgjzc = df_jbcwzb.ix[2, 1:].replace('--', '0').sort_index(ascending=False)

data_mgxjl = df_jbcwzb.ix[3, 1:].replace('--', '0').sort_index(ascending=False)

plt.plot(data_reportDate, data_jbmgsy.astype(float), '-+r', label='每股收益')

plt.plot(data_reportDate, data_mgjzc.astype(float), '--om', label='每股净资产')

plt.plot(data_reportDate, data_mgxjl.astype(float), '-.*b', label='每股现金流')

plt.legend()

plt.xticks(data_reportDate, rotation=90)

plt.grid()

# plt.xlabel('年报日期')

plt.ylabel('每 股 指 标')

plt.title(stock_name + '-每股指标')

# 2、图二：扣非净利润

ax2 = plt.subplot2grid((3, 1), (1, 0))

data_kfjlr = df_jbcwzb.ix[11, 1:].replace('--', '0').sort_index(ascending=False)

data_jlr = df_jbcwzb.ix[10, 1:].replace('--', '0').sort_index(ascending=False)

data_zyywsr = df_jbcwzb.ix[4, 1:].replace('--', '0').sort_index(ascending=False)

data_zyywlr = df_jbcwzb.ix[5, 1:].replace('--', '0').sort_index(ascending=False)

plt.plot(data_reportDate, data_zyywsr.astype(float), '-+m', label='主营收入')

plt.plot(data_reportDate, data_zyywlr.astype(float), '--*g', label='主营利润')

plt.plot(data_reportDate, data_jlr.astype(float), '-.+b', label='净利润')

plt.plot(data_reportDate, data_kfjlr.astype(float), ':or', label='扣非净利润')

plt.legend()

plt.xticks(data_reportDate, rotation=90)

# plt.xlabel('年报日期')

plt.ylabel('营 收 利 润')

plt.title(stock_name + '-营收利润')

plt.grid()

# 3、图二：总资产

ax3 = plt.subplot2grid((3, 1), (2, 0))

data_zzc = df_jbcwzb.ix[14, 1:].replace('--', '0').sort_index(ascending=False)

data_zfz = df_jbcwzb.ix[16, 1:].replace('--', '0').sort_index(ascending=False)

plt.plot(data_reportDate, data_zzc.astype(float), '--+r', label='总资产')

plt.plot(data_reportDate, data_zfz.astype(float), '-.ob', label='总负债')

plt.legend()

plt.xticks(data_reportDate, rotation=90)

# plt.xlabel('年报日期')

plt.ylabel('资 产 负 债')

plt.title(stock_name + '-资产负债')

plt.grid()

plt.savefig('./数据-分析/' + stock_name + '-' + time.strftime("%Y%m", time.localtime()) + '-网易-主要财务指标-年度.png', dpi=600)

plt.show()
