import time
lights = [('green',2)
          ,("red",2),
          ("yellow",0.5)]
i=0
while True:
    c,s = lights[i]
    print(c)
    time.sleep(s)
    if i==len(lights)-1:
        i=0
    else:
        i=i+1