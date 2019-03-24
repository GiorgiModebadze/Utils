import os
import shutil
from shutil import copy2
from os.path import expanduser
from subprocess import check_call
import datetime

start = datetime.datetime.now()
home = expanduser("~")
dest = home + '/Desktop/.files'
meta_loc = dest + "/.meta.txt"
ending = ('.txt')
gb = float(1000000000)
files = list()
total_size = 0

try:
    os.mkdir(dest)
except:
    pass


for dirpath, dirnames, filenames in os.walk(home): 
    if total_size / gb < 1:
        for file in filenames:
            if file.lower().endswith(ending):
                source = dirpath+"/"+ file
                total_size += os.path.getsize(source)

                files.append(source + ':' + str(os.path.getsize(source)))
                try: 
                    copy2(source,dest)
                except:
                    pass
    else:
        break

with open(meta_loc, 'w') as f:
    for file in files:
        f.write("%s\n" % file)

final_dest = home + '/Desktop/'
os.chdir(final_dest)

try:
    final_dest = home + '/Desktop/'
    os.chdir(final_dest)
    shutil.make_archive('.data_f_analysis', 'zip', dest)
except:
    pass

end = datetime.datetime.now()

try:
    shutil.rmtree(dest)
except:
    pass

print("Time needed:",(end-start).seconds)
print("Files found:", len(files))