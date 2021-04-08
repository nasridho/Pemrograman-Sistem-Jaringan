import subprocess
import sys

argv_len = len(sys.argv[1:])
if not argv_len==1:
	sys.exit(f'Gagal: IP address belum diberikan')


ipnya = sys.argv[1:]
ip = ipnya[0]

p = subprocess.Popen('ping '+ip,stdout=subprocess.PIPE)

p.wait()
if p.poll():
    print ("Host " + ip + " is DOWN")
else:
    print ("Host " + ip+" is UP")