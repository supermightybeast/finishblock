# Итоговая проверочная работа
## Условия задачи
#### Задача алгоритмически не самая сложная, однако для полноценного выполнения проверочной работы необходимо:

>1 Создать репозиторий на `GitHub`

>2 Нарисовать блок-схему алгоритма (можно обойтись блок-схемой основной содержательной части, если вы выделяете её в отдельный метод)

>3 Снабдить репозиторий оформленным текстовым описанием решения (файл README.md)

>4 Написать программу, решающую поставленную задачу

>5 Использовать контроль версий в работе над этим небольшим проектом (не должно быть так, что всё залито одним коммитом, как минимум этапы 2, 3, и 4 должны быть расположены в разных коммитах)

### Задача:

Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам. Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

### Примеры:
```py
[“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
[“1234”, “1567”, “-2”, “computer science”] → [“-2”]
[“Russia”, “Denmark”, “Kazan”] → []
```

## Решение задачи:
1 Вы находитесь в созданном репозитории ```finishblock```

>2 Блок-схема DRAWIO: 
![logo](/codes/csharp_drawio.png)


3 Репозироий снабжен файлом ```README.md```

4 Программа находится в ветке [codes](https://github.com/supermightybeast/finishblock/tree/main/codes) для [Pyrhon](https://github.com/supermightybeast/finishblock/blob/main/codes/prog.py) и для языка [C#](https://github.com/supermightybeast/finishblock/blob/main/codes/code.cs)

### ***Содержание кода программы на языке `C#`:***
```c#
Commands();
string[] array = new string[] {};

string fromUser = ReadInput("Введите команду: ");
switch (fromUser)
{
    case "1":
        array = new string[] { "Hello", "2", "world", ":-)" };
        break;
    case "2":
        array = new string[] { "1234", "1567", "-2", "computer science" };
        break;
    case "3":
        array = new string[] { "Russia", "Denmark", "Kazan" };
        break;
    default:
        Console.WriteLine($"{fromUser} - Такой команды нет");
        break;
}


int lenNewArray = 0;
for (int i = 0; i <= array.Length - 1; i++)
{
    if (array[i].Length <= 3) lenNewArray++;
}

string[] newArray = new string[lenNewArray];
int idx = 0;

for (int i = 0; i <= array.Length - 1; i++)
{
    if (array[i].Length <= 3)
    {
        newArray[idx] = array[i];
        idx++;
    }
}

PrintArray(array);
Console.Write("→ ");
PrintArray(newArray);

// Функция: Вывод команд для работы с программой
void Commands()
{
    Console.WriteLine();
    Console.WriteLine("СПИСОК КОМАНД:");
    Console.WriteLine("1 – использовать массив: [“Hello”, “2”, “world”, “:-)”]");
    Console.WriteLine("2 – использовать массив: [“1234”, “1567”, “-2”, “computer science”]");
    Console.WriteLine("3 – использовать массив: [“Russia”, “Denmark”, “Kazan”]");
    Console.WriteLine();
}

// Функция ввода
string ReadInput(string msg)
{
    Console.Write(msg);
    return Console.ReadLine();
}

//  Функция вывода массива в терминал
void PrintArray(string[] array)
{
    Console.Write("[ ");
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"“{array[i]}”, ");
    }
    Console.Write("] ");
}
```

### ***Содержание кода программы на языке `Python`:***
```python
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
```

## Результат вывода в терминал `C#`:
![logo](/codes/csharp.png)

## Результат вывода в терминал `Python`:
![logo](/codes/pyth.png)

## 5 Использовать контроль версий в работе над этим небольшим проектом
Список коммитов:
![logo](/codes/commits.png)
