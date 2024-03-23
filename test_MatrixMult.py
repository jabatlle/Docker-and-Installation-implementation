from MatrixMult import MatrixMult
import numpy as np

def test_2x2Mult():

    A_2x2 = np.array([
        [1, 2],
        [3, 4]
    ])

    B_2x2 = np.array([
        [4, 3],
        [2, 1]
    ])

    expected_result = np.array([
        [8, 5],
        [20, 13]
    ])

    my_function_result = MatrixMult(A_2x2, B_2x2)

    # Check if the result matches the expected result
    assert np.array_equal(my_function_result, expected_result)