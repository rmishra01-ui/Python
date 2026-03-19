# Part 1
set1 = {2, 3, 1}
set2 = {"Jack", "Emma", "Joseph"}
set3 = {list(zip(set1, set2))}
# Part 2
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
  print(x, y)
# Part 3
stocks = ["Lions", "Tigers", "Lizards"]
prices = [99.99, 52.13, 22.99]
dictionary1 = {stocks: prices, for stocks in zip(stocks, prices)}
print(dictionary1)
