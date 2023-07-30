# 1. Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


MATRIX = [[1, 2, 3], [4, 5, 6]]

def main():
    print("Исходная матрица:")
    print_matrix(MATRIX)
    print("Транспонированная:")
    print_matrix(transpose_matrix(MATRIX))

def print_matrix(matrix: list[list]):
       for row in matrix:
        print(row)


def transpose_matrix(matrix: list[list]) -> list[list]:
    new_matrix = [[] for _ in range(0, len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[col].append(matrix[row][col])
    return new_matrix

if __name__ == "__main__":
    main()