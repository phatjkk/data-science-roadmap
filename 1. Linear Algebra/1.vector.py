import numpy as np
# Tạo 2 vector A, B
list_a = [5, 6, 9]
list_b = [1, 2, 3]

# ===========================================
# Chuyển 2 vector A, B về dạng numpy array
# (giúp thực hiện tính toán, tăng tốc xử lý)
vector_a = np.array(list_a)
vector_b = np.array(list_b)

# ===========================================
print("Vector A: " + str(vector_a))
# Đầu ra: Vector A  : [5 6 9]
print("Vector B: " + str(vector_b))
# Đầu ra: Vector B : [1 2 3]

# ===========================================
# Cộng 2 vector A, B
sum_a_b = vector_a + vector_b
# a + b = [a1+b1, a2+b2, a3+b3]
print("A plus B: " + str(sum_a_b))
# Đầu ra: A plus B: [6 8 12]

# ===========================================
# Trừ 2 vector A, B
minus_a_b = vector_a - vector_b
# a + b = [a1-b1, a2-b2, a3-b3]
print("A minus B: " + str(minus_a_b))
# Đầu ra: A minus B: [4 4 6]

# ===========================================
# Nhân vô hướng 2 vector A . B (dot product)
# a . b = (a1 * b1 + a2 * b2 + a3 * b3)
dot_product_a_b = vector_a @ vector_b
print("A dot B: " + str(dot_product_a_b))
# Đầu ra: A dot B: 44
