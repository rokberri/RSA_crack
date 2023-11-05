from .decor import get_runtime

def factorisation_func(N:int):
    """
     Метод факторизации Ферма
    """
    res ={}
    for x in range(int(N**0.5),N,1):
        y = (x**2)-N
        tmp = y**0.5
        if str(tmp)[-2:]=='.0':
            if not x-int(tmp) in res.keys():
                res[x-int(tmp)]=x+int(tmp)
    return res


def split_big_num(N,n):
    blocks = list()
    tmp = ''
    for i in str(N):    
        prev_num = tmp
        tmp += i
        if int(tmp)>n:
            blocks.append(prev_num)
            tmp = i
    blocks.append(tmp)
    return blocks


def find_all_d(N:int):
    res = list()
    for i in range(2,int(N**0.5),1):
        if i not in set(res):
            if N % i == 0:
                res.append(i)
                res.append(int(N / i))
    return res