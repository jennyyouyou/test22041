#@coding=utf-8
#@TIME:2023/5/23 17:02
#@author:SX
import csv
class Readcsv():
    def __init__(self):
        pass

    def read_list_csv(self,filename):
        data=[]
        #'../test_data/tpshoplogin1.csv'
        with open(filename,'r+',encoding='utf-8')  as file:
            reader=csv.reader(file)
            for r in reader:
              if r[0]!='caseid':
                data.append(r)
        return(data)


    def read_dict_csv(self,filename) :
        data1=[]
        with open(filename,'r+',encoding='utf-8')  as f:
            dreader=csv.DictReader(f)

            for c in dreader:
                dic = {}
                dic['username']=c['ueername']
                dic['password'] = c['password']
                dic['verify_code'] = c['verfiled']
                dic['res']=c['exp']

                data1.append(dic)

        return(data1)




if __name__ == '__main__':
    rc=Readcsv()
    setattr(rc,'name','hahaha')
    print(rc.read_dict_csv('../test_data/tpshoplogin1.csv'))
    print(getattr(rc,'name'))
    #print(rc.read_list_csv('../test_data/tpshoplogin1.csv'))