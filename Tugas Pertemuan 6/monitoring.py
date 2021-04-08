import time
import multiprocessing
import subprocess
import sys
  

time1 = time.perf_counter()

def check(host):
	ip = host

	p = subprocess.Popen('ping '+ip,stdout=subprocess.PIPE)

	p.wait()
	if p.poll():
		print ("Host " + ip + " is DOWN")
	else:
		print ("Host " + ip+" is UP")

def main():
    hosts = ['192.168.1.1','192.168.1.2','192.168.1.3','8.8.8.8','8.8.4.4']
    proses = []
    
    for i in hosts:
        P = multiprocessing.Process(target=check, args=(i, ))
        P.start()
        proses.append(P)

    for process in proses:
        process.join()
    
    time2 = time.perf_counter()
    
    print('')

    print('Selesai dalam waktu {} detik'.format(time2-time1,2))
        
    
if __name__ == "__main__":
    main()
 