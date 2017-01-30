import psutil


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
	

drives = getdiskinfo()
print(str(drives))
