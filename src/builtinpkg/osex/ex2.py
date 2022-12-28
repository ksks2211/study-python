import os


stat = os.stat('setup.py')

print(stat)


os.utime()

r, w = os.pipe()

rd = os.fdopen(r)


result = os.popen('dir','r')

result.read()

os.name
env = os.environ

os.getenv()

os.putenv()

os.strerror()

os.system(comman)

os.startfile()


os.execv()
os.execl()