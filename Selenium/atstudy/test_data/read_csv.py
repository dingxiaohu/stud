import csv

# 用来读取csv文件
# def get_csv_data(csv_file, line):
#     dxh_csv_file = open(csv_file, 'r', encoding='utf-8-sig')
#     reader = csv.reader(dxh_csv_file)
#     # 遍历reader这个可迭代对象，同时获取每个元素在可迭代对象中的索引值和对应的值，索引值从1开始计数。
#     for index, result in enumerate(reader, 1):
#         if index == line:
#             return result

'''
    返回的是一个存列表的字典
    字典中的key对应文件中的行数
    value对应文件中每行的内容（以列表的形式存取）
'''


# 用来读取csv文件
def get_csv_data(csv_file):
    dxh_csv_file = open(csv_file, 'r', encoding='utf-8-sig')
    reader = csv.reader(dxh_csv_file)
    # 遍历reader这个可迭代对象，同时获取每个元素在可迭代对象中的索引值和对应的值，索引值从1开始计数。
    result = {}
    for index, data in enumerate(reader, 1):
        result[index] = data
    return result


if __name__ == '__main__':
    print(get_csv_data("login.csv"))
