task = '''
Задача на дин. программирование: наибольшая кратная подпоследовательность

Дано:
    целое число 1≤n≤1000
    массив A[1…n] натуральных чисел, не превосходящих 2E9.

Необходимо:
    Выведите подпоследовательность индексов i[1]<i[2]<…<i[k] <= длины k,
    для которой каждый элемент A[i[j]] где 2<=j<k делится на предыдущий
    A[i[j-1]] без остатка.
    
    Найдите решение за время O(n*n) и восстановите подпоследовательность за время O(n) 
    не используя запоминание предыдущих элементов в оптимальном решении. 
    
    Индексы начинаются с 1.

Решить задачу МЕТОДАМИ ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ

    Sample Input:
    4
    3 6 7 12

    Sample Output:
    1 2 4
'''


def getSeqIndexses(filename):
    # тут реализуйте логику задачи методами динамического программирования (!!!)
    # рекомендуется создать массив для найденных максимальных значений длины последовательности.
    # число в массиве означает достигнутую длину к этой точке.
    # индексы в обоих массивах при этом совпадают.
    # !!!!!!!!!!!!!!!!!!!!!!!!!     НАЧАЛО ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!
    return [0]
    # !!!!!!!!!!!!!!!!!!!!!!!!!     КОНЕЦ ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!


def main():
    filename = "dataB.txt"
    answer = getSeqIndexses(filename)
    for i in answer: print(i,end=" ")


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
