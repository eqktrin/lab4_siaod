import random

# бинарный поиск
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# бинарное дерево поиска
class Node:
    def __init__(self, key, index):
        self.left = None
        self.right = None
        self.val = key
        self.index = index  # Добавляем поле для хранения индекса

def tree_insert(root, key, index):
    if root is None:
        return Node(key, index)  # При вставке сохраняем индекс
    if key < root.val:
        root.left = tree_insert(root.left, key, index)
    else:
        root.right = tree_insert(root.right, key, index)
    return root

def tree_search(root, key):
    if root is None:
        return None  # Если элемент не найден, возвращаем None
    if root.val == key:
        return root.index  # Возвращаем индекс найденного узла

    if key < root.val:
        return tree_search(root.left, key)
    return tree_search(root.right, key)




# фибоначчиев поиск
def fibonacci_search(arr, target):
    fib_m2, fib_m1 = 0, 1
    fib_m = fib_m1 + fib_m2

    while fib_m < len(arr):
        fib_m2, fib_m1 = fib_m1, fib_m
        fib_m = fib_m1 + fib_m2

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, len(arr) - 1)

        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1

        else:
            return i

    return -1

# интерполяционный поиск
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# простое рехэширование
class SimpleRehash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def re_hash(self, key):
        return key % self.size

    def re_insert(self, key):
        index = self.re_hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key

# рехэширование с помощью псевдослучайных чисел
class RandomRehash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def pre_hash(self, key):
        return key % self.size

    def pre_insert(self, key):
        index = self.pre_hash(key)
        step = random.randint(1, self.size - 1)
        while self.table[index] is not None:
            index = (index + step) % self.size
        self.table[index] = key

# метод цепочек
class ChainHash:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        self.table[index].append(key)

# задача о 8 ферзях
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    if row == n:
        return [board[:]]
    solutions = []
    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)
            solutions.extend(solve_n_queens(n, row + 1, board))
            board.pop()
    return solutions


# тестирование
if __name__ == "__main__":
    arr = sorted(random.sample(range(100), 10))
    target = arr[len(arr) // 2]
    print(f"Массив: {arr}")


    print(f"Бинарный поиск: {binary_search(arr, target)}")

    root = None
    for index, num in enumerate(arr):
        root = tree_insert(root, num, index)
    result = tree_search(root, target)
    if result is not None:
        print(f"Число {target} найдено в бинарном дереве, индекс: {result}")
    else:
        print(f"Число {target} не найдено в бинарном дереве.")


    print(f"Фибоначчиев поиск: {fibonacci_search(arr, target)}")


    print(f"Интерполяционный поиск: {interpolation_search(arr, target)}")

    print("Простое рехэширование:")
    simple_rehash = SimpleRehash(10)
    simple_rehash.re_insert(10)
    simple_rehash.re_insert(20)
    simple_rehash.re_insert(30)
    print(simple_rehash.table)

    print("Рехэширование с помощью псевдослучайных чисел:")
    random_rehash = RandomRehash(10)
    random_rehash.pre_insert(10)
    random_rehash.pre_insert(20)
    random_rehash.pre_insert(30)
    print(random_rehash.table)

    print("Метод цепочек:")
    chain_hash = ChainHash(10)
    chain_hash.insert(10)
    chain_hash.insert(20)
    chain_hash.insert(30)
    print(chain_hash.table)

    solutions = solve_n_queens(8)
    print(f"Решение задачи о 8 ферзях : {solutions[0]}")
