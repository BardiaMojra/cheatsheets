
import os
import subprocess
import time

# from pdb import set_trace as st

srcDir = './'
srcPath = os.path.abspath(srcDir)

def gitStatusAll():
  for i, Dir in enumerate(sorted(os.listdir(srcDir))):
    if os.path.isdir(Dir):
      print(f" \--->> now checking: {Dir}")
      dirPath = os.path.join(srcPath, Dir)
      subprocess.Popen(["cd", dirPath])
      subprocess.Popen(["git", "fetch"])
      subprocess.Popen(["git", "status"])
      subprocess.Popen(["cd", srcPath])
  return #

def rename_files():
  for i, file in enumerate(os.listdir(srcDir)):
    if os.path.isfile(file):
      newfile = file
      newfile = newfile.replace(' ', '_').lower()
      newfile = newfile.replace('&', 'n')
      newfile = newfile.replace(',', '')
      newfile = newfile.replace('and', 'n')
      newfile = newfile.replace("'", '')
      newfile = newfile.replace('-', '_')
      newfile = newfile.replace('__', '_')
      newfile = newfile.replace('__', '_')
      src = srcDir+file
      dest = srcDir+newfile
      os.rename(src,dest)
      print(i, file)

  print('files renamed... ')
  for i, file in enumerate(os.listdir(srcDir)):
    print(i, file)
  return # rename files

if __name__ == '__main__':

  gitStatusAll()


# EOF
