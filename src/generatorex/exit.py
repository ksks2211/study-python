def fibonacci():
  cur,prev = 1,0

  try:
    while True:
      yield cur
      cur, prev = cur+prev, cur      
      if(cur > 100): raise GeneratorExit("FIN")
  except GeneratorExit as e:
    print(e) 
    print("=======")         


f = fibonacci()
for cur in f:
  print(cur)
  f.close()






