# -*- coding: utf-8 -*-
import os
filename = "track.log"
size = 10000000  # 10M

def mk_SubFile(srcName, sub, lines): #buf):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('       : %s' % filename)
    with open(filename, 'wb') as fout:
        #fout.write(buf)
        fout.writelines(lines)
        return sub+1

def split_By_size(filenm, size):
    # filenm =  '../app/data/mobility1_01.json'
    # size = 10000000 #    10M  = 10,(M)000,(K)000
    with open(filenm, 'rb') as fin:
        buf = fin.read(size)
        sub = 1
        while len(buf) > 0:
            sub = mk_SubFile(filenm, sub, buf)
            buf = fin.read(size)
    print("ok")

if __name__ == "__main__":
    split_By_size(filenm, size)
import os

# source_file='../app/data/mobility1_01.json'

file_count=10000 #       

def mk_SubFile(lines,srcName,sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str(sub) + extname
    print( '       : %s' %filename)
    with open(filename,'wb') as fout:
        fout.writelines(lines)
        return sub + 1


def split_By_LineCount(fileNm,count):
    # fileNm = '../app/data/mobi.json.test.txt'
    # count = 2
    with open(fileNm,'r') as f:
        #print(fin.read())
        buf = []
        sub = 1
        for line in f:
            # print("-----s------")
            # print(line.strip())
            # print("-----e------")
            if len(line.strip())>0:   # 앞뒤공백을 없앤 한라인의 글자수 
                buf.append(line)    # buf는 계속 쌓임
                line_tag=line.strip()[0]   #     ，      ，   ,       
                if len(buf) >= count : #and line_tag == '*': #  
                    buf = buf[:-1]
                    # sub = mk_SubFile(buf,fileNm,sub) # buf      
                    buf = [line] #          buf，    *   
                    print(buf)
                
        #      ，            
        if len(buf) != 0:
            sub = mk_SubFile(buf, fileNm, sub)
    print("ok")


if __name__ == '__main__':
    split_By_LineCount(source_file,file_count)#                