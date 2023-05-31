from numpy import array

A = array([[1, 2, 3],
           [4, 5, 6]])

print(A, "\n")

B = array([[0.5, 0.5, 0.5],
           [0.5, 0.5, 0.5]])

print(B, "\n")

C = A - B
print(C, "\n")
