# coding:utf-8
import os


def cutFile(fileNm):
    with open(fileNm, 'r') as f:
        lines = f.read().splitlines()
        n = len(lines)
        print(f"All Lines: {str(n)} ")
        dividedFiles = int(input(""))
        numOfLines = n//dividedFiles + 1
        print(
            f"Divided Fiels: {str(dividedFiles)}, Lines per file: {str(numOfLines)} ")
        [sub_filename, extname] = os.path.splitext(fileNm)
        for i in range(dividedFiles):
            subFileNm = sub_filename+"_part"+str(i+1)+extname
            print(subFileNm)
            with open(subFileNm, "w", encoding='utf-8') as destFileData:
                if(i == dividedFiles-1):   # Last File
                    for eachLine in lines[numOfLines*i:]:
                        destFileData.write(eachLine + '\n')
                else:           # 1~ File
                    for eachLine in lines[numOfLines*i:numOfLines*(i+1)]:
                        destFileData.write(eachLine + '\n')


cutFile('../app/data/mobi.json.test.txt')
cutFile('../app/data/mobility1_01.json')
