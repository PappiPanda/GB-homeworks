import time
sec = int(input('write time in seconds, please: '))
ty_res = time.gmtime(sec)
res = time.strftime("%H:%M:%S",ty_res)
print('Time is ' + res)