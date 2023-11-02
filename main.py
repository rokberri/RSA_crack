# 549755813888
from utils.generate_key import get_keys




def main():
    e,d,n = get_keys()
    print(e,n)
    print(d,n)
    message = 789
    print(message)
    en_m = (message ** e) % n
    print(en_m)
    dec_m = (en_m ** d) % n
    print(dec_m)

if __name__ == '__main__':
    main()


    
    