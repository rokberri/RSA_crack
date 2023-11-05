from utils.generate_key import get_keys, euler
from utils.factorisation import find_all_d, split_big_num
import decimal



def convert_data_into_sim(data):
    s = ' '.join([str(block) for block in data])
    s = s.replace(' ','')
    print(s)
    res = ''
    tmp = ''
    for el in s:
        tmp += el
        if len(tmp)==2:
            res += chr(int(tmp))
            tmp = ''
    return res

def RSA_standart(message):
    e,d,n = get_keys()
    print(f"ПАРА e;n: {e},{n}")
    print(f"ПАРА d;n: {d},{n}")
    print(f"СООБЩЕНИЕ: {message}")
    en_m = (message ** e) % n
    print(f"ЗАШИФРОВАННОЕ СООБЩЕНИЕ: {en_m}")
    dec_m = (en_m ** d) % n
    print(f"РАСШИФРОВАННОЕ СООБЩЕНИЕ: {dec_m}")

def RSA_crack(N,e,n):
    p , q = find_all_d(n)

    eurel_n =(p-1)*(q-1)

    blocks = split_big_num(N,n)

    d = pow(e,(euler(eurel_n)-1) , eurel_n)

    print(convert_data_into_sim([pow(int(block),int(d),n) for block in blocks]))

if __name__ == '__main__':
    RSA_standart(758)
    e = 23311
    n = 274611845366113
    N = 108230462382949240744446393133139920760825242128635453394626156290136879344
    RSA_crack(N,e,n)
