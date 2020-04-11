import tabula

# Example: '1-2,3', 'all' or [1,2]
def convert_pdf(path_file, pages_str):
    tabula.convert_into(path_file,path_file+".csv", pages=pages_str)


if __name__ == '__main__':
    path = "G:/_Stock/temp/000007全新好2016年半年度报告.(2181k).PDF"
    convert_pdf(path, '7')