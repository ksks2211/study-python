import glob, os.path as path


ndir = nfile = 0


def traverse(dir, depth):
  global ndir, nfile

  for obj in glob.glob(dir+'/*'):
    if depth == 0 :
      prefix = '|--'
    else:
      prefix = '|' + ' '*depth + '|--'

    if path.isdir(obj):
      ndir +=1
      print(prefix + path.basename(obj))
      traverse(obj,depth + 1)
    elif path.isfile(obj):
      nfile += 1
      print(prefix + path.basename(obj))
    else:
      print(prefix + 'unknown object : ',obj)  



if __name__ == '__main__':
  traverse('.',0)
  print('\n',ndir, 'directories, ',nfile,'files')
