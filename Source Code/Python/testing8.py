from labinstrument.tools.buildin_ex import *


a={
    'a':'1',
    'b':'1',
    'c':{'cc':2},
    'd':{'dd':3},
    'e':{'ee':{'eee':4}},
    'f':{'ff':{'fff':5}},
   }
b={
    'a':'1',
    'b':'2',
    'c':{'cc':2},
    'd':{'dd':2},
    'e':{'ee':{'eee':4}},
    'f':{'ff':{'fff':4}},
}

print(dict_delta(a,b))