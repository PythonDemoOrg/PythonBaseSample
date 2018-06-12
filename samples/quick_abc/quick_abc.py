#! /usr/bin/python
# 中文

import py_compile
import global_var
import sys

def hello_world():
    print ("hello word") # 发放

def test_compile():
    py_compile.compile('./quick_abc.py')

def test_id():
    x = 1
    print (id(x))
    print ('----')
    x = 2
    print (id(x))

def fun():
    print (global_var._a)
    print (global_var._b)


# class _const:
#     class ConstError(TypeError): pass
#         def __setattr__(self,name,vlaue):
#             if self.__dict__.has_key(name):
#                 raise self.ConstError('Can’t rebind const(%s)'%name)
#                 self.__dict__[name]=value
# sys.modules[__name__] = _const()

def test_tuple():
    tuple_name=('apple','banana','grape','orange')
    for element in tuple_name:
        print(element)

def test_list():
    list=['apples','bananas','grapes','oranges']
    list.append('grapes')
    try:
        list.remove('banana')
    except:
        print('something wrong')
    for element in list:
        print(element)

def test_dict():
    dict={'a':'apple','b':'banana','g':'grape'}
    for element in dict:
        print(element)
    for element in dict.values():
        print(element)

def test_str():
    word='world'
    print (word[0:3])

def test_file():
    context='hello, world'
    filename='hello.txt'
    with open(filename, "wb") as file:
        file.write(context)
        file.close()

class Fruit:
    def grow(self):
        print('Fruit grow')

class Apple(Fruit):
   def test(self):
       print(Fruit.grow(Fruit))

if __name__ == '__main__':
    Apple.test(Apple)
    # Fruit.grow(Fruit)

    # fruit=Fruit()
    # fruit.grow()