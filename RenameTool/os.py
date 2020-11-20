
#批量重命名，注意事项：
# 1、一定要在被命名文件夹最上一层的文件夹中，否则找不到对应的要被命名的文件夹
# 2、 Recording 2 这样的源文件名字就会出现顺序错乱的问题，需要先将序号调整为统一的位数，比如改为Recording 02才会按照正确排序命名
# 3、i参数指的是天数，下一次用前来前记得修改，第1.3章将从i=108开始。
# 4、打包成一个函数试试 RenameDay

import os
folder_name = input("请输入要重命名的文件夹:")
file_names = os.listdir(folder_name)
i = 65
for name in file_names:
    print(name)
    print(name.split('day-')[-1])
    name1 = name.split('day-')[-1]
    old_file_name = "./" + folder_name + "/" + name
    new_file_name = "./" + folder_name + "/" + "day-" +str(i) + name1
    os.rename(old_file_name, new_file_name)
    i += 1

# 下面这种我还不太会用，
# 参考资料源于：https://zhuanlan.zhihu.com/p/71861602  
# https://www.zhihu.com/search?type=content&q=python%E6%89%B9%E9%87%8F%E5%91%BD%E5%90%8Dimport%20glob%20
# https://zhuanlan.zhihu.com/p/31549917

#import os
#import glob

#files_list = glob.glob('./*.m4a')
#print（files_list）

#def rename(path,file):
    with open(path) as f:
        for i, line in enumerate(f):
            print(i,line.strip())
            os.rename(file[i],line.strip()+'.m4a')

#rename('./Recording.m4a',file_list)

