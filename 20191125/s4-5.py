a = [1, 2, 4, 5, 7, 9, 10, 27, 101]

# append 新增元素或陣列在 list 最後面
a.append(77)
print(a)
a.append([3, 2, 1])
print(a)

# extend 將陣列中的元素,新增至陣列的最後面
a.extend([3, 2, 1])
print(a)

# inset 在我們指定的索引位置插入值為 x 的元素
a.insert(10,11)
print(a)

# pop 從陣列中彈出(刪除)索引n的元素
a.pop()
print(a)
a[11].pop(1)
print(a)

a.pop(11)
print(a)

# remove 移除從陣列中第一次出現值的元素
a.remove(2)
print(a)

# sort 排序
a.sort()
print(a)
