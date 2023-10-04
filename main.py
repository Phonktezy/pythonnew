# 1
first_number = int(input("Введите число: "))
second_number = first_number + 1
third_number = first_number + 2
print (first_number)
print (second_number)
print (third_number)
# 2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

sum = a + b + c

print(sum)
# 3
длина_ребра = int(input("Введите длину ребра: "))
Обьем= длина_ребра ** 3
Площадь_поверхности = 6 * (длина_ребра ** 2)
print("Обьем куба:", Обьем)
print("Полная площадь поверхности:", Площадь_поверхности)
# 4
a = int(input ("Введите первое число: "))
b = int(input("Введите второе число: "))
f = 3*(a + b)**3 + 275*b**2 -127*a - 41
print (f)
# 5
a = int(input("Введите число: "))
f = a+1
n = a-1
print(f"Следущее за числом {a} число: {f}")
print(f"Предыдущее для числа {a} число:{n}")
# 6
a = int(input ("Стоимость монитора: "))
b = int(input ("Стоимость системного блока: "))
c = int(input ("Стоимость клавиатур: "))
d = int(input ("Стоимость мыши: "))
sum = int(a+b+c+d)*3
print ("Стоимость трех компьютеров =", sum)
# 7
a_1 = int(input())
d = int(input())
n = int(input())
a_n = a_1 + d*(n-1)
print ("Алг. прог.: ", a_n)
# 8
x1 = int(input("Введите число: "))
x2 = x1 * 2
x3 = x2 + x1
x4 = x3 + x1
x5 = x4 + x1
print(x1,x2,x3,x4,x5, sep='---')
# 9
n = int(input("Кол. школьников: "))
k = int(input("Мандаринки: "))
half = n // k
bask = n % k
print ("Количество мандаринок у каждого школьникa: ",half)
print ("Количество мандаринок в корзине : ",bask)
# 10
a=int(input())
print(a//2 + a%2)
# 11
m = int(input("Введите число: "))
h = m // 60
s = m % 60
print(m, "мин. это - ", h, "час", s, "минут.")
# 12
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма чисел =", c + b + a)
print("Произведение чисел =", c * b * a)
# 13
n = input()
print('    _~_    ' *int(n))
print('   (o o)   ' *int(n))
print('  /  V  \  ' *int(n))
print(' /(  _  )\ ' *int(n))
print('   ^^ ^^   ' *int(n))
# 14
abc = int(input())
x = 1
n = (x // 10 ** k) % 10
print(n)
# 15
a = int(input())
h = a % (60 * 24) // 60
m = a % 60
print(h, m)
# 16
a = int(input())
print(1 - a)
# 17
a = int(input())
print((a//2+1)*2)
# 18
v = int(input())
t = int(input())
a = v * t
n = a // 109
print(-(109 * n - a))
#19
a = float(input("1: "))
b = float(input("2: "))
c = float(input("3: "))
print(int(1 + (a - c - 1) / (b - c)))







