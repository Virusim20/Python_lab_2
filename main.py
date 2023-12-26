import math

def main():
    print("Практична робота №2 Забрянська Маріанна312ст")  
    task1()  
    newtask()  
    task2()  
    newtask()  
    task3()  

def newtask():  
    print("\n\n=================================================\n\n")
    input() 

def task1():
    print("=====Завдання 1=====\n")
    print("Дано цілочисельні координати трьох вершин прямокутника, сторони якого паралельні координатним осях. Знайти координати його четвертої вершини.\n")
    x1 = int(input("Введіть x1: "))
    y1 = int(input("Введіть y1: "))
    x2 = int(input("Введіть x2: "))
    y2 = int(input("Введіть y2: "))
    x3 = int(input("Введіть x3: "))
    y3 = int(input("Введіть y3: "))


    x4 = x2 + x3 - x1
    y4 = y2 + y3 - y1


    print("Координати четвертої вершини:", x4, y4)


def task2():
    print("=====Завдання 2=====\n")
    print("∑ n=1 ->∞ = ((n!)*n)/((2n)!)")

    series_sum = 0
    n = 0

    while True:
        n = int(input("Введіть кількість кроків: "))
        if n>0:
            break
        else:
            print(f"Число {n} менше нуля.")

    for i in range(1, n + 1):
        term = (math.factorial(n)*n)/(math.factorial(2*n))
        series_sum += term

    print(f"∑ n=1 ->{n} = (n**3)/(2**(n+1)) = {series_sum}")



def task3():
    print("=====Завдання 3=====\n")
    print("∑ n=1 ->∞ = ((2**n)*(n-1)!)/(n**math.sqrt(n))")

    series_sum = 0
    n = 0

    while True:
        n = int(input("Введіть кількість кроків: "))
        if n>0:
            break
        else:
            print(f"Число {n} менше нуля.")

    for i in range(1, n + 1):
        term = ((2**n)*math.factorial(n-1))/(n**math.sqrt(n))
        series_sum += term

    print(f"∑ n=1 ->{n} = ((math.pi**n)*n**3)/(n!) = {series_sum}")

main()