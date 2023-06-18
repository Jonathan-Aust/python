# !/user/bin/python

# Example Python script

import sys

arge = len(sys.argv)

if arge > 1:
    print ('too many args')
else:
    where = 'World'
    print ("Hello", where)

print ('Goodbye from ' + sys.argv[0])
