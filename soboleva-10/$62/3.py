
'''
    Заполните массив первыми числами Фибоначчи.
'''


N = int(input("введите число --> "));

A = [];

cur, fut = 0, 1; # текущий, следующий
for i in range(N):
    a = cur;
    cur = fut;

    A.append(cur);

    fut = a + fut; 

print(A);