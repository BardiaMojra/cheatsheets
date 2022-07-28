
import os
srcDir = './'


ext = '.pdf'
print('\n\n\n rename files with extension: '+ext+'\n\n')
# or
#ext = int(input('\n enter file extension: '))
files = list()

for i, file in enumerate(os.listdir(srcDir)):
  print(i, file)
  if (os.path.isfile(srcDir+file) & file.endswith(ext)):
    newfile = file
    newfile = newfile.replace(' ', '_').lower()
    newfile = newfile.replace('&', 'n')
    newfile = newfile.replace(',', '')
    newfile = newfile.replace('and', 'n')
    newfile = newfile.replace("'", '')
    newfile = newfile.replace('-', '_')
    newfile = newfile.replace('__', '_')
    newfile = newfile.replace('__', '_')
    src = srcDir + file
    files.append(src)
    #newfile = '_' + newfile
    newfile = '_{:0>3d}_'.format(len(files)) + newfile
    newfile = newfile.replace('__', '_')
    dest = srcDir + newfile
    os.rename(src, dest)
    #print(i, file)
  else:
    i = i-1

print('files renamed... ')
for i, file in enumerate(os.listdir(srcDir)):
  print(i, file)

# EOF
