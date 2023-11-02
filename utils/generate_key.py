import time
import random

def ferma_nums(n:int)->list[int]:
    res = list()
    for i in range(n):
        tmp = 2**i
        res.append((2**tmp)+1)
    return res

def get_runtime(func):
    def wrapper(arg):
        print("Диапазон поиска чисел: от 1 до", arg)
        start_time = time.monotonic()
        print(func(arg))
        print('Время выполнения: ', time.monotonic() - start_time)

    return wrapper

def sieve_eratosthenes(n):
    """
    Решето Эратосфена
    """
    a = range(n + 1)
    a = list(a)
    a[1] = 0
    result_list = []
    i = 2
    while i <= n:
        if a[i] != 0:
            result_list.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return result_list

def get_keys():
    """
    Генерация секретных ключей
    """
    p, q = get_prime_num()
    n = p * q
    euler_n = (p-1)*(q-1)
    # ???????????????????????????????????????????????????????
    e = -1
    for el in range(euler_n,0,-1):
        if el < euler_n and bezout(euler_n,el)[2]==1:
            e = el
            break
    # ???????????????????????????????????????????????????????
    d = euler_n - abs(min(bezout(euler_n, e)[0:2]))
    return (e, d, n)

def bezout(a, b):
    '''
    Расширенный алгоритм Евклида
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)

def get_prime_num():
    """
    Функция для получения типа рандомных простых чисел
    """
    primary_numbers = sieve_eratosthenes(1024)
    length = len(primary_numbers)
    a, b = primary_numbers[random.randint(0,length)], primary_numbers[random.randint(0,length)]
    return(a,b)