import numpy as np

count = 0
number = np.random.randint(1,101)                   # загадали число
print ("Загадано число от 1 до 100,", str(number))  # Печатаем полученное число

for i in range(9,0,-1):                             #Ограничиваем работу в 8 шагов согласно Log
    if number - count >= 2**i:                      #Подбор путем возведения в степень
        count += 2**i
    if number - count == 0:
        break

print('Итог выполнения подсчета:', str(count))