import random
import ctypes
b = [0, 0, 0, 0, 0, 1]
i = 0
p = ""
while True:
    random.shuffle(b)
    if b[0] == 1:
        print("RIP")
        ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
        exit()
    i += 1
    while not p == "ano":
        try:
            p = input(f"Pokračovat ({i}. kolo)? (ano): ")
        except KeyboardInterrupt:
            pass
