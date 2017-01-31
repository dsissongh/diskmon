import sys
import psutil
import argparse
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


parser = argparse.ArgumentParser()
parser.add_argument('--report', '-r', help='In additon to visual report, send an email when the value is lower than specified.',
			action="store_true")
parser.add_argument('--limit', '-l', help='Set the limit in Gb.  Default = 4G',
			nargs='?', const=4, type=int)
parser.parse_args()
args = parser.parse_args()


table = PrettyTable(['Drive','Freespace'])
drives = getdiskinfo()
report = []
for drive in drives:
	table.add_row([drive,drives[drive]])
	if args.report:
		if args.limit:
			limit = args.limit
		else:
			limit = 4

		if drives[drive] < limit:	
			report.append(drive)



table.sortby =  'Freespace'	
print(table)

if args.report:
	if len(report) > 0:
		print(report)