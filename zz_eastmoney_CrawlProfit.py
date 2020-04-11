import requests
import re
import json
import csv
import time


#
def get_table(page):
    params = {
        'type': 'CWBB_LRB',  # 表格类型,LRB为利润表缩写，必须
        'token': '70f12f2f4f091e459a279469fe49eca5',  # 访问令牌，必须
        'st': 'noticedate',  # 公告日期
        'sr': -1,  # 保持-1不用改动即可
        'p': page,  # 表格页数
        'ps': 50,  # 每页显示多少条信息
        'js': 'var LFtlXDqn={pages:(tp),data: (x)}',  # js函数，必须
        'filter': '(reportdate=^2018-06-30^)',  # 筛选条件，如果不选则默认下载全部时期的数据
        # 'rt': 51294261  可不用
    }
    url = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?'
    response = requests.get(url, params=params).text
    # 确定页数
    pat = re.compile('var.*?{pages:(\d+),data:.*?')
    page_all = re.search(pat, response)  # 总页数
    pattern = re.compile('var.*?data: (.*)}', re.S)
    items = re.search(pattern, response)
    data = items.group(1)
    data = json.loads(data)
    print('\n正在下载第 %s 页表格' % page)
    return page_all,data


def write_header(data):
    with open('eastmoney.csv', 'a', encoding='utf_8_sig', newline='') as f:
        headers = list(data[0].keys())
        writer = csv.writer(f)
        writer.writerow(headers)


def write_table(data):
    for d in data:
        with open('eastmoney.csv', 'a', encoding='utf_8_sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(d.values())


def main(page):
    page_all,data = get_table(page)
    write_table(data)


if __name__ == '__main__':
    start_time = time.time()  # 下载开始时间
    # 写入表头
    page_all, data = get_table(1)
    write_header(data)
    page_all = int(page_all.group(1))
    for page in range(1, page_all):
        main(page)
    end_time = time.time() - start_time  # 结束时间
    print('下载用时: {:.1f} s'.format(end_time))