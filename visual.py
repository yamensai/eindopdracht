from program import *
def progess_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '+' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}|{percent:.2f}%", end="\r")
while(1):
    progess_bar(len(Station1.bikes), Station1.capacity)
    progess_bar(len(Station2.bikes), Station2.capacity)