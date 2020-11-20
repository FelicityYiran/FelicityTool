#批量重命名，注意事项：
# 1、一定要在被命名文件夹最上一层的文件夹中，否则找不到对应的要被命名的文件夹
# 2、 Recording 2 这样的源文件名字就会出现顺序错乱的问题，需要先将序号调整为统一的位数，比如改为Recording 02才会按照正确排序命名
# 3、i参数指的是天数，下一次用前来前记得修改，第1.3章将从i=108开始。
# 4、打包成一个函数RenameDay,使用方法：先import RenameDAY 然后RenameDay.Re()执行即可


import os

def Re():
    folder_name = input("请输入要重命名的文件夹:")
    m = input("请输入指定天数：")
    i = int (m)
    file_names = os.listdir(folder_name)
    for name in file_names:
        print(name)
        print(name.split('day-')[-1])
        name1 = name.split('day-')[-1]
        old_file_name = "./" + folder_name + "/" + name
        new_file_name = "./" + folder_name + "/" + "day-" +str(i) + name1
        os.rename(old_file_name, new_file_name)
        i += 1

