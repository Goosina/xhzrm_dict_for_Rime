import os

string = "是	shi;op	142460771"

shengmu_list1 = ['zh','ch','sh']
shengmu_list2 = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','r','s','c','z','y','w']

initials        = "initials.txt"
finals1         = "finals1.txt"
finals2         = "finals2.txt"

def create_dict(textfile):
    dict = {}
    with open(textfile, "r", encoding="utf-8") as file:

        for line in file:
            (key, value) = line.split()
            dict[key] = value
    return dict

#判断有无声母
def has_shengmu(word):
    s1=word[0]
    for letter in shengmu_list2:
        if s1 == letter:
            if word[0:2] in shengmu_list1:
                return 2
            else:
                return 1
    return 0

def output_shengmu_and_yunmu(word):
    return([word[0:has_shengmu(word)],word[has_shengmu(word):]])

def convert(string):
    if '\t' in string:
        ci,pinyin_whole,freq = string.split('\t')
        #pinyin_whole,ci,freq = string.split('\t')
        pinyin_whole_new=''
        for pinyin in pinyin_whole.rstrip().split(' '):
            #print(pinyin)
            shengmu,yunmu = output_shengmu_and_yunmu(pinyin)
            if ';' in yunmu:
                yunmu,aux = yunmu.split(";")
                aux = ";"+aux
            else:
                aux = ""
            try:
                if shengmu == '':
                    yunmu = finals2_dict[yunmu]
                else:
                    shengmu = initials_dict[shengmu]
                    yunmu   = finals1_dict[yunmu]
                pinyin_whole_new += shengmu+yunmu+' '
            except:
                return None
        return ci+'\t'+pinyin_whole_new.rstrip()+aux+'\t'+freq
        #return pinyin_whole_new+'\t'+ci+'\t'+freq
    else:
        return string

initials_dict   = create_dict(initials) #声母
finals1_dict    = create_dict(finals1)  #韵母
finals2_dict    = create_dict(finals2)  #无声母

def read_and_write(target,result):#yaml文件
    with open(target,'r',encoding='utf-8') as f:
        ret = f.readline()
        while ret:
            with open(result,'a',encoding='utf-8') as fr:
                try:
                    fr.write(convert(ret))
                except:
                    pass
            ret = f.readline()
        
def convert_files():
    file_list = os.listdir('./ku')
    for file in file_list:
        read_and_write('./ku/'+file,'./ku-convert/'+file.split('.dict')[0]+'.dict.yaml')

convert_files()

#print(convert(string))



