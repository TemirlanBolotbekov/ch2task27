#Напишите функцию где исходный список содержит положительные и отрицательные
#числа. Требуется положительные поместить в один список, а отрицательные - в другой.

# def number(pos):
pos = (input("Input any Numbers :").split())
spis = []
spis2 = []
for i in pos:
    i = int(i)
    if i > 0 :
        spis.append(i)
    elif i < 0 :
        spis2.append(i)
print("Positive integer - :",spis)
print("Negative integer - :",spis2)