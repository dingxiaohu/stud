
#读取cvs文件放到data列表中，每个元素都是一个列表，每行数据为一个列表存储到data中[[],[]]
def get_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    data = []
    for i in range(len(lines)):
        data1 = lines[i].split(",")
        #strip去除首尾的空格，制表符，换行符，还可以指定参数，lstrip()左，rstrip()右
        data1[-1] = data1[-1].strip()
        data.append(data1)
    return data

