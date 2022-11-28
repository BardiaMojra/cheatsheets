
import os
srcDir = './'
ext = '.pdf'
#print('\n\n\n rename files with extension: '+ext+'\n\n')
# or
#ext = int(input('\n enter file extension: '))
files = list()

for i, file in enumerate(os.listdir(srcDir)):
  #print(i, file)
  if (os.path.isfile(srcDir+file) & file.endswith(ext)):
    nfile = file
    nfile = nfile.replace('_n_', '_and_')
    nfile = nfile.replace('_', ' ').lower()
    nfile = nfile.replace('.pdf', '')
    #nfile = nfile.replace(',', '')
    #nfile = nfile.replace('and', 'n')
    #nfile = nfile.replace("'", '')
    #nfile = nfile.replace('-', '_')
    #nfile = nfile.replace('__', '_')
    #nfile = nfile.replace('__', '_')
    #src = srcDir + file
    #files.append(src)
    #nfile = '_' + nfile
    #nfile = '_{:0>3d}_'.format(len(files)) + nfile
    #nfile = nfile.replace('_icra_', '_ICRA_')
    #nfile = nfile.replace('_ral_', '_RAL_')
    #nfile = nfile.replace('_tor_', '_TOR_')
    #nfile = nfile.replace('__', '_')
    #dest = srcDir + nfile
    #os.rename(src, dest)
    print(i, "  ", nfile)
  else:
    i = i-1

#print('files renamed... ')
#for i, file in enumerate(os.listdir(srcDir)):
#  print(i, "  ", file)

# EOF
