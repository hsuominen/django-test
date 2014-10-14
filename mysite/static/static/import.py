import numpy as np
import matplotlib.pyplot as plt
import re
import time
import datetime
import dateutil.parser as dateparser

# Full path and name to your csv file
csv_filepathname="/Users/hsuominen/Dropbox/repos/django-test/mysite/data/214209_testmeasurement.dat"
#meta_filepathname="/Users/hsuominen/Dropbox/repos/django-test/mysite/data/214209_testmeasurement.set"

# Full path to your django project directory
your_djangoproject_home="/Users/hsuominen/Dropbox/repos/django-test/mysite/mysite/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from datastore.models import acquisition, coordinate, value#, meta

import csv
f = open(csv_filepathname, 'r')

filename = f.readline().strip().split("Filename: ",1)[1]
timestamp = f.readline().strip().split("Timestamp: ",1)[1]

print filename
dt = dateparser.parse(timestamp)
real_timestamp = int(time.mktime(dt.timetuple()))

readable_ts = datetime.datetime.fromtimestamp(int(real_timestamp)).strftime('%Y-%m-%d %H:%M:%S')

print readable_ts

names = []
types = []

for line in f:
    li=line.strip()
    if li.startswith("#	name"):
        names.append(line.split('#	name: ',1)[1].strip())
    if li.startswith("#	type"):
    	types.append(line.split('#	type: ',1)[1].strip())

coordinates = []
coo_units = []
values = []
val_units = []

for i in range(0,len(names)):
	if i<=1:
		coo_and_unit = names[i].split('[',1)
		coo = coo_and_unit[0].strip()
		if len(coo_and_unit) > 1:
			coo_unit = coo_and_unit[1][:-1].strip()
		else:
			coo_unit = ''

		coordinates.append(coo)
		coo_units.append(coo_unit)
	else:

		val_and_unit = names[i].split('[',1)
		val = val_and_unit[0].strip()
		if len(val_and_unit) > 1:
			val_unit = val_and_unit[1][:-1].strip()
		else:
			val_unit = ''

		values.append(val)
		val_units.append(val_unit)
		

print coordinates
print coo_units
print values
print val_units

raw_data = np.loadtxt(csv_filepathname, comments='#')

x = np.unique(raw_data[:,0])
y = np.unique(raw_data[:,1])

x_size = x.shape[0]
y_size = y.shape[0]

print x_size
print y_size

data = raw_data[:,2].reshape((y_size,x_size))

plt.imshow(data,aspect='auto')
plt.show()

acq = acquisition()
acq.acqdatetime = readable_ts

acq.save()

co1  = acq.coordinates.create(coordinate_label=coordinates[0],coordinate_unit=coo_units[0],coordinate_val=x)
co2  = acq.coordinates.create(coordinate_label=coordinates[1],coordinate_unit=coo_units[1],coordinate_val=y)

v  = acq.values.create(value_label=values[0],value_unit=val_units[0],value=data)

acq.save()

