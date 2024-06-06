import numpy as np
# Tạo 2 ma trận A, B dạng numpy array
# (giúp thực hiện tính toán, tăng tốc xử lý)
matrix_a = np.array([[5, 6, 9],
                     [7, 2, 6]])
matrix_b = np.array([[1, 2, 3],
                     [4, 5, 6]])

# ===========================================
print("Matrix A: " + str(matrix_a))
# Đầu ra: Matrix A : [[5 6 9]
#                     [7 2 6]]
print("Matrix B: " + str(matrix_a))
# Đầu ra: Matrix B : [[5 6 9]
#                     [7 2 6]]

# ===========================================
# Cộng 2 ma trận A, B
sum_a_b = matrix_a + matrix_b
# a + b = [[a1+b1, a2+b2, a3+b3],
#          [a4+b4, a5+b5, a6+b6]]
print("A plus B: " + str(sum_a_b))
# Đầu ra: A plus B: [[6 8 12]
#                    [11 7 12]]

# ===========================================
# Trừ 2 ma trận A, B
minus_a_b = matrix_a - matrix_b
# a + b = [[a1-b1, a2-b2, a3-b3],
#          [a4-b4, a5-b5, a6-b6]]
print("A minus B: " + str(minus_a_b))
# Đầu ra: A minus B: [[4 4 6]
#                     [3 -3 0]]

# ===========================================
# Ma trận chuyển vị (transpose)
matrix_b_T = matrix_b.T
# mtB = [[b1, b2, b3]
#        [b4, b5, b6]]
# mtB.T = [[b1, b4]
#          [b2, b5]
#          [b3, b6]]
print("A transpose: " + str(matrix_b_T))
# Đầu ra: A transpose: [[1 4]
#                       [2 5]
#                       [3 6]]

# ===========================================
# Nhân vô hướng 2 vector A . B.T (dot product)
# (Nguyên tắc số cột A = số dòng B, ta có mtA[2x3] . mtB.T[3x2])
# mtA = [[a1, a2, a3]
#        [a4, a5, a6]]
# mtB.T = [[b1, b4]
#          [b2, b5]
#          [b3, b6]]
# Đầu ra [2x2]: [[a1*b1+a2*b2+a3*b3, a1*b4+a2*b5+a3*b6],
#                [a4*b1+a5*b2+a6*b3, a4*b4+a5*b5+a6*b6]]
dot_product_a_b = matrix_a @ matrix_b.T

print("A dot B: " + str(dot_product_a_b))

# Đầu ra: A dot B:[[ 44 104]
#                  [ 29  74]]
