import time

print('press ENTER to begin.Afterward , press ENTER to click the stopwatch. and then press Ctrl-c to quit')
input()
print('started')
startTime = time.time()

lastTime = startTime
lapNum=1
try:
    while True:
        input()
        lapTime=round(time.time()-lastTime,2)
        totalTime=round(time.time()-startTime,2)
        print('lap #%s: %s (%s)' % (lapNum,totalTime,lapTime),end="")
        lapNum=lapNum+1
        lastTime= time.time()
except:
    print('\ndone')
