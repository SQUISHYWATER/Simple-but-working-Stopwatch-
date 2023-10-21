import time
print("Hit ENTER to start the stopwatch, afterwards, press ENTER to count a lap.")
input()
print("Stopwatch Started.")
startTime = time.time()
lastTime = startTime
lap = 1
while True:
    input()
    lapTime = round(time.time() - lastTime, 3)
    gameTime = round(time.time() - startTime, 3)
    if lap == 1:
        print("First Lap Done! Lap Time: " + str(lapTime) + " Total Time: " + str(gameTime), end="")
    else:
        print("Lap " + str(lap) + " Done! Lap Time: " + str(lapTime) + " Total Time: " + str(gameTime), end="")
    lap += 1
    lastTime = time.time()
