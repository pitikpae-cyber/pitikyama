import sys
if len(sys.argv) != 4: 
        print("Использование:python average.py <число1> <число2> <число3>")
sys.exit(1)
try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        num3 = float(sys.argv[3])
        average = (num1 + num2 + num3) / 3
        print(f"Числа: {num1}, {num2}, {num3}")
        print(f"Среднее: {average}")
except ValueError: print("Ошибка: все аргументы должны быть числами!")
sys.exit(1)


