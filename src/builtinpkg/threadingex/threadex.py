from threading import Thread, Lock
import time

fish = 10
lock = Lock()


class SushiMaster(Thread):

  def __init__(self,name):
    # Thread.__init__(self)
    super().__init__()
    self.name = name
    self.sushi = 0

  def run(self):
    global fish

    while True:
      lock.acquire()

      if fish > 0:
        fish -=1
        lock.release()
        self.sushi +=1
        time.sleep(0.1)
      else:
        lock.release()
        break


threads = []

for name in ['James','Brad','John']:
  chef = SushiMaster(name)
  threads.append(chef)
  chef.start()


for chef in threads:
  chef.join()
  print(chef.name, 'made',chef.sushi," piece of sushi")

