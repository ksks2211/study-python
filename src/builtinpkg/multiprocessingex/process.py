from multiprocessing import Process, Lock, Value
import time
import os


def run(name, lock:Lock, fish):
  print(name, ' process created. PID : ', os.getpid())
  sushi = 0
  while True:
    lock.acquire()

    if fish.value > 0:
      fish.value -=1
      lock.release()
      sushi +=1
      time.sleep(0.1)
    else:
      lock.release()      
      print(name, ' : number of sushi - ',sushi)
      break


if __name__ == '__main__':
  lock = Lock()

  fish = Value('i',10)
  
  processes = []

  for name in ['james','john','tom']:
    p = Process(target=run, args=(name, lock, fish))
    processes.append(p)
    p.start()

  for p in processes:
    p.join()

  print("All Processed Finished")
  print('Main Process PID : ',os.getpid())
