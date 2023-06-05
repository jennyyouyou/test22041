#@coding=utf-8
#@TIME:2023/5/25 11:14
#@author:SX
class A():
    name='zenzen'
    def eat(self):
        height=168
        #print('eating.....')
        return (height)

if __name__ == '__main__':
    t=A()
    print(t.name)
    print(hasattr(t,'eat'))
    #setattr(t,'age', 18)
    print(getattr(t,'age',19))
    delattr(t,'age')


    t.eat()