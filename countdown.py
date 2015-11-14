import os
import time
for pp2 in range(1,10000):
 try:
  standard=input("Enter number of seconds:")
  sec=standard+1
  sec2=standard+2
  for i in range(1,sec2):
    sec=sec-1
    print"%s"%sec
    time.sleep(1)
    if sec<= 0:os.system('cls')
    os.system('cls')
 except:
    print"The input is not a number, being restored, wait for 5 seconds."
    time.sleep(5)
    os.system('cls')
