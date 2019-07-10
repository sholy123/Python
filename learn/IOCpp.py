from os.path import isdir,join
from os import listdir

AllLines = []
NotRepeatedLines = []
file_num = 0
code_num = 0

def LinesCount(directory):
    global AllLines
    global NotRepeatedLines
    global file_num
    global code_num

    for filename in listdir(directory):
        temp = join(directory,filename)
        print(temp)
        if isdir(temp):
            LinesCount(temp)
        elif temp.endswith('.md'):
            file_num += 1
            with open(temp,'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    if line not in NotRepeatedLines:
                        NotRepeatedLines.append(line)
                    code_num+=1


path = "/home/sholy/sholy/md/article/shell-others/shell/"
LinesCount(path)
print(code_num)
print('DAFAGAHA:{0}'.format(file_num))