import sys
import getopt
# 处理arff开头
def arffhead(f1,f2):

    feature1 = 0
    feature2 = 0
    flag1 = 1
    flag2 = 1
    strlist = []
    firststr =  f1.readline()#.replace('\n','') +" and "+f2.readline().replace('@','')
    f2.readline()
    strlist.append(firststr)
    for str1 in f1:
        if str1.isspace():
            continue
        if flag1:
            if 'class' not in str1:
                feature1 += 1
            else:
                strlist.append(str1)
                break

    for str2 in f2:
        if str2.isspace():
            continue
        if flag2:
            if 'class' not in str2:
                feature2 += 1
            else:
                strlist.append(str2)
                break
    return feature1,feature2,strlist
# 处理arff数据
def writefile3(f1,f2,f3,sum,firststr):
    f3.write(firststr[0]+'\n')  #@relation Protein
    for i in range(sum):
        f3.write('@attribute Feature{0} real \n'.format(i+1))
        i+=1

    f1.readline()#跳过class1
    f2.readline()#同上      2
    f3.write(firststr[1])  #@class       defaulit the  class of file1
    f3.write('\n@data\n')

    for str1,str2 in zip(f1,f2):
        while(str1.isspace()):
            str1=f1.readline()
        while (str2.isspace()):
            str2=f2.readline()
        if(str1[-3]=='-'):
            f3.write(str1[:-3]+str2)
        else:
            f3.write(str1[:-2]+str2)
    print("arff done !")
#处理libsvm
def merge_svmlib(f1,f2,f3):
    i = 1
    for str1, str2 in zip(f1, f2):

        while (str1.isspace()):
            f1.readline()
        while (str2.isspace()):
            f2.readline()
        dim1 = int(str1.split()[-1].split(':')[0])
        dim2 = int(str2.split()[-1].split(':')[0])

        str2=str2.split( )
        str_temp=str2[1:]  #去掉标签
        secondfile_1num = str1.split()[-2]
        secondfile_1num=int(secondfile_1num.split(':')[0])+1
        str2 = [str(int(l.split(':')[0]) + secondfile_1num) + ':' + l.split(':')[1] for l in str_temp]  #修改第二个文件维度  如f! : 1 2 3 f2:1 2 --->f3 1 2 3 4 5
        str_add_file1dim = ' '+' '.join(str2)

        #print(str1[:-1] + str_add_file1dim)

        f3.write(str1[:-1] + str_add_file1dim+'\n')

        # if(i==4):
        #     break
        # print(i)
        # i += 1
    print("libsvm done !")


file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
format = sys.argv[4]
with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'w') as f3:
    # 处理arff
    if format == "arff":
        feature1, feature2, firststr = arffhead(f1, f2)
        writefile3(f1, f2, f3,feature1+feature2 , firststr)
    # 处理svmlib
    elif (format == "libsvm"):
        merge_svmlib(f1, f2, f3)
    else:
        print("Please make sure that the two files have the same format (ex: blank line, space:category label)")





