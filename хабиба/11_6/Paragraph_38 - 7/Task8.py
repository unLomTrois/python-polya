
'''
    ???????? ?????? ????????? ??? ?????????? ?????? ??????????? ????? ?? ?????? ?????.
    ?????????, ??? ??? ????? ????????, ???? ?? ???? ??????? isqrt ?????? ??????? ????????.
'''

def isqrt(a):
    x = a
    while True:
        x1 = (x*x + a)//(2*x)
        if x1 >= x: return x
        x = x1

number = int(input('??????? ????? ?????: '))
print(isqrt(number))