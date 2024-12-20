import math

def task1(): # 6
    # Take two numbers as input from the user
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    
    # Compare the two numbers and print the larger one
    if a > b:
        print("Більше число:", a)
    elif b > a:
        print("Більше число:", b)
    else:
        print("Числа рівні.")
    
    
def task2(): # 22
    # Введення параметрів
    a = float(input("Введіть сторону квадрата (a): "))
    r = float(input("Введіть радіус кола (r): "))

    # Введення координат точок
    n = int(input("Введіть кількість точок (n): "))
    points = []
    for i in range(n):
        x, y = map(float, input(f"Введіть координати точки {i+1} (x, y): ").split())
        points.append((x, y))

    # Перевірка, чи точка належить темно-зеленій області
    def is_in_dark_green_area(x, y, a, r):
        # Темно-зелена область - I and IV чверть квадрата, поза колом
        if -a / 2 <= x <= a / 2 and 0 <= y <= a / 2 and x**2 + y**2 > r**2:
            return True
        return False

    # Підрахунок точок у темно-зеленій області
    count = 0
    for x, y in points:
        if is_in_dark_green_area(x, y, a, r):
            count += 1

    print("Кількість точок у темно-зеленій області: ", count)
        
# 13

def task3():

    # N input
    N = int(input("N = "))
    if N == 0:
        print("N cannot be 0 in denominator")
    else:
        total = 0
        for n in range(1, N + 1):
            # Calculate each term of the series
            numerator = 2**n * math.factorial(2*n - 1)
            denominator = math.sqrt(math.factorial(n))
            term = numerator / denominator
            total += term

    # total
    
    print("The approximate sum of the series for {N} terms is: ", total)

def main_menu():
    
    while True:
        print("\nМеню:")
        print("1. Виконати завдання 6")
        print("2. Виконати завдання 22")
        print("3. Виконати завдання 13")
        print("4. Вийти")
        
        choice = input("Введіть номер опції (1-4): ")
        
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main_menu()












