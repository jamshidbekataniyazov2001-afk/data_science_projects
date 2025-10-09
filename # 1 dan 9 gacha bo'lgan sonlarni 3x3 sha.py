# 1 dan 9 gacha bo'lgan sonlarni 3x3 shaklidagi 2 o'lchamli massiv ko'rinishida ekranga chiqaruvchi dastur
import numpy as np
import random
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
array = np.array(random.sample(range(1, 10), 9)).reshape(3, 3)
print(array)    
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')
print("Dastur yakunlandi!")
