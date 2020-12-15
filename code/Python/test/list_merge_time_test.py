# time test
import time
import itertools as iter

a = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
]

# way 1 : sum
start = time.time()
c = sum(a, [])
end = time.time() - start
print("way 1 time : ", end)
print(c)

# way 2 : iter
start = time.time()
c = list(iter.chain(*a))
end = time.time() - start
print("way 2 time : ", end)
print(c)

# way 3 : list comprehension
start = time.time()
c = [x for y in a for x in y]
end = time.time() - start
print("way 2 time : ", end)
print(c)
