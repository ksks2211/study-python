"""simplest set"""
from functools import reduce


def intersect(*arg):
  """교집합 함수"""
  return reduce(__intersectSC,arg)

def __intersectSC(listX,listY):
  setList=[]
  for x in listX:
    if x in listY:
      setList.append(x)
  return setList


def union(*arg):
  """합집합"""
  setList = []
  for item in arg:
    for x in item:
      if not x in setList:
        setList.append(x)
  return setList        

  
      

def difference(*arg):
  """차집합 함수"""
  setList=[]

  intersectSet = intersect(*arg)  

  for x in arg[0]:
    if not x in intersectSet:
      setList.append(x)
  return setList

if __name__ == '__main__':
  a = [1,2,3,4,5]
  b = [4,5,6,7,8]

  c = difference(a,b)

  print(c)