#Number of moves Bishop can make based on position
def solve(A, B):
    count = 0
    temp = A + B
    for i in range(1, 9):
        for j in range(1, 9):
            if A == i and B == j:
                continue
            elif i + j == temp:
                count += 1
                #print(i,j)
    if A > B:
        count += (B-1) + (8-A)
    else :
         count += (A-1)+ (8 - B)

solve(4,4)
