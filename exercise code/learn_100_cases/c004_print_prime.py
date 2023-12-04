# 输入开始数字和结束数字，找出里面的素数


def is_prime(number):
    if number in (1,2):
        return True
    for idx in (2,number):
        if number % idx == 0:
            return False
        return True




def print_prime(begin, end):
    for number in range(begin, end+1):
        if is_prime(number):
            print(f"{number} is a prime")

begin = 11
end = 26
print_prime(begin, end)
