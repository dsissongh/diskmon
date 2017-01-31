import psutil
from prettytable import PrettyTable


def getdiskinfo():
	disks = {}
	partitions = psutil.disk_partitions()
	for p in partitions:
		try:
			freespace = psutil.disk_usage(p.mountpoint).free/1000000000
			disks.update({p.mountpoint:freespace})
		except:
			pass

	return disks

table = PrettyTable(['Drive','Freespace'])
drives = getdiskinfo()
for drive in drives:
	table.add_row([drive,drives[drive]])
	
table.sortby =  'Freespace'	
print(table)
