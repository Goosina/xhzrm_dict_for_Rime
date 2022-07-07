#精简规则
#大于5个字的词去掉
#词频=0的去掉

import os

def is_retain(string):
    if "\t" in string:
        phase1,code,freq=string.split("\t")
        if len(phase1) >=5 or int(freq)==0:
            return False
        else:
            return True
    else:
        return True

def read_and_write(target,result):#yaml文件
    with open(target,'r',encoding='utf-8') as f:
        ret = f.readline()
        while ret:
            with open(result,'a',encoding='utf-8') as fr:
                if is_retain(ret):
                    try:
                        fr.write(ret)
                    except:
                        pass
            ret = f.readline()

def convert_files():
    file_list = os.listdir('./ku')
    for file in file_list:
        read_and_write('./ku/'+file,'./ku-convert/'+file.split('.dict')[0]+'.dict.yaml')

convert_files()