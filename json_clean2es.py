# coding:utf-8


def js_clean2es(filename):
    f = open(filename, 'r', encoding='utf-8')
    newname = "gotobed.json"
    save = open(newname, 'a+', encoding='utf-8')
    line = f.readline()
    line = line[:-2]
    i = 1
    while(line):
        print('{"index":{"_index":"insu","_type":"health","_id":',i,'}}',file=save)
        print(line,file=save)
        i+=1
        print('No',i,'Operation Finished')
        line = f.readline()[:-2]
        if(line[line.__len__() -2]==','):
            line = line[:-2]+'}'
            print(line)
    #print('\n',file=save)

def main():
    js_clean2es(filename='insurance_info.json')

if __name__ == '__main__':
    main()