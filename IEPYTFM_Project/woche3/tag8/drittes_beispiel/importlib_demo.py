import importlib

modul = importlib.import_module ("math")
print(type(modul))

print(modul.sin(2), modul.sqrt(10))

import time

modul = importlib.import_module("sag_was")

while True:
    time.sleep(5)
    importlib.reload(modul)
    modul.demo()


