A = (-12, 2)
B = (-5, 11)
C = (5, 24)
N = 6

print('Nalezy do :', end=' ')
if A[0] <= N <= A[1]:
    print('A', end=' ')
if B[0] <= N <= B[1]:
    print('B', end=' ')
if C[0] <= N <= C[1]:
    print('C', end='\n')
else:
    print('zadnego zbioru')
