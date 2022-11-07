import time
from itertools import product
from hashlib import sha256 as hash_
import threading
print("Выберите в каком потоке расшифровать: 1 - однопоток, 2 - многопоток")
choise = int(input())
hash = '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad', '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b', '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'
if choise == 1:
    timee = time.time()
    for j in range(3):
        start_time = time.time()
        for i in product("abcdefghijkmnloqrsptuvwxyz", repeat=5):
            if hash_("".join(i).encode("utf-8")).hexdigest() == hash[j]:
                print("".join(i), (time.time() - start_time))
                break
    print(time.time() - timee)
elif choise == 2:
    hash_2 = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f', '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b', '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'
    start_time = time.time()
    using_list = []
    def multi(abc):
        y = int(0)
        for i in product(abc, repeat=5):
            if multi_stop == 2:
              print("Программа закончила работу")
              break
            else:
              x = hash_("".join(i).encode("utf-8")).hexdigest()
              if x == hash_2[0] or x == hash_2[1] or x == hash_2[2]:
                  if x not in void_list:
                      print("".join(i), (time.time() - start_time))
                      multi_stop += 1
                      using_list.append(x)

thr1 = threading.Thread(target = multi, args=("abcdefghijkmnloqrsptuvwxyz" )).start()
thr2 = threading.Thread(target = multi, args=("zyxwvutsrqponmlkjihgfedcba")).start()
