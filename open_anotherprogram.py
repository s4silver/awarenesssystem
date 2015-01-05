import os

import subprocess
#

from os.path import join

lookfor = "firefox.exe"
for root, dirs, files in os.walk('C:\\'):
    print("searching", root)
    if lookfor in files:
        print("found: %s" % join(root, lookfor))
        break

file_location = join(root, lookfor)
print(file_location)

subprocess.call([file_location])
