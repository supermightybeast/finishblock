# Список комманд массива
print("СПИСОК КОМАНД:")
print("1 – использовать массив: [“Hello”, “2”, “world”, “:-)”]")
print("2 – использовать массив: [“1234”, “1567”, “-2”, “computer science”]")
print("3 – использовать массив: [“Russia”, “Denmark”, “Kazan”]")

# Функция ввода 
def read_input(msg):
    return input(msg)

# Функция вывода массива в терминал
def print_array(array):
    print("[", end=" ")
    for i in range(len(array)):
        print(f"“{array[i]}”,", end=" ")
    print("]")

array = []
massive = read_input("Введите команду: ")
if massive == "1":
    array = ["Hello", "2", "world", ":-)"]
elif massive == "2":
    array = ["1234", "1567", "-2", "computer science"]
elif massive == "3":
    array = ["Russia", "Denmark", "Kazan"]
else:
    print(f"{massive} - Такой команды нет")

len_new_array = 0
for i in range(len(array)):
    if len(array[i]) <= 3:
        len_new_array += 1

new_array = [None] * len_new_array
idx = 0

for i in range(len(array)):
    if len(array[i]) <= 3:
        new_array[idx] = array[i]
        idx += 1

print_array(array)
print("→", end=" ")
print_array(new_array)