import sys

def merge(f1,f2,f3):
    i = 0
    for f1_str in f1:

        if(f1_str[0]=='%'):
            continue
        if (f1_str.isspace()):
            continue
        if (f1_str == "@data\n"):
            break
        if(i==1):
            f3.write('\n'+f1_str)
        else:
            f3.write(f1_str)
        i+=1


    for f2_str in f2:
        if(f2_str[0]=='%'):
            continue
        if (f2_str.isspace()):
            continue
        if (f2_str == "@data\n"):
            break
        f3.write(f2_str)
    f3.write('\n@data\n')
    for f1_str,f2_str in zip(f1,f2):
        f3.write(f1_str[:-1]+','+f2_str)
    print("arff done !!")

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

#test
# file1 = "weather.numeric1.arff"
# file2 = "weather.numeric2.arff"
# file3 = "weather.out1.arff"


with open(file1,'r') as f1,open(file2,'r') as f2,open(file3,'w') as f3:
    merge(f1,f2,f3)

