A = (-12, 2)
B = (-5, 11)
C = (5, 24)
N = 153
check = False

print('Nalezy do :', end=' ')
if A[0] <= N <= A[1]:
    check = True
    print('A', end=' ')
if B[0] <= N <= B[1]:
    check = True
    print('B', end=' ')
if C[0] <= N <= C[1]:
    check = True
    print('C', end='\n')
if check == False:
    print('zadnego zbioru')
