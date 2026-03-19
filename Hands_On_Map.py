list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1.6, 1, 2, 5, 3, 1, 42, 5, 4, 25]
result = map(lambda x, y: x + y, list1, list2)
print("The Combination of Two Lists.")
print(list(result))

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Define Function
def square(n):
    return n * n
sq = list(map(square, list3))
print(sq)
