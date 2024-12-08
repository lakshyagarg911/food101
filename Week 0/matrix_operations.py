import numpy as np


def matrix_operation(array1, array2, operation):
    if operation == "dot":
        return np.dot(array1, array2)

    elif operation == "matrix":
        if array1.shape[1] != array2.shape[0]:
            return "Matrix multiplication is not possible with these dimensions."
        return array1 @ array2

    elif operation == "determinant":
        # Compute determinants of square matrices
        det1 = det2 = None
        if array1.shape[0] == array1.shape[1]:
            det1 = np.linalg.det(array1)
        else:
            det1 = "Determinant not defined for non-square matrices (array1)."

        if array2.shape[0] == array2.shape[1]:
            det2 = np.linalg.det(array2)
        else:
            det2 = "Determinant not defined for non-square matrices (array2)."

        return det1, det2

    else:
        return "Invalid operation. Please choose 'dot', 'matrix', or 'determinant'."


if __name__ == "__main__":
    array1 = np.array([[1, 2],[3,4]])
    array2 = np.array([[5, 6],[7,8]])

    print("Dot product:\n", matrix_operation(array1, array2, "dot"))
    print("Matrix multiplication:\n", matrix_operation(array1, array2, "matrix"))
    print("Determinants:\n", matrix_operation(array1, array2, "determinant"))
