import time

def alarme():
    for i in range(10 , 0 ,-1):
        time.sleep(0.50)
        print(i)
    print('FOGOO!!!!')

alarme()