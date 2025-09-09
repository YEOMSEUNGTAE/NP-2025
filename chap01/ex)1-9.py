from typing import List
Matrix3x3 = List[List[int]]

def add_matrix_3x3(A: Matrix3x3, B: Matrix3x3) -> Matrix3x3:
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

# 테스트
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
print(add_matrix_3x3(A,B))  
# [[10,10,10],[10,10,10],[10,10,10]]
