b = [1, 2, 3, 4, 5, 6, 9, 8, 7]
a = ["a", "c", "d", "e", "g", "b", "f", "h"]

# ________sorting________
# b_sorted = b.sort()  # empty paranthesis will show none
# print(b_sorted)
b.sort()
print(b)
a.sort()
print(a)
# ________reverse________
b.reverse()
print(b)
# ________append________
# _________appends at the end of list______

b.append(10)
b.reverse()
a.append("goru")
a.sort()
print(b)
print(a)
# ________insert________->inserting at the selected index point any value
a.insert(0, "goru")
print(a)
a.insert(5, "goru")
print(a)
# ________pop________
a.pop(0)  # removes at index 0
a.pop(5)  # removes at index 0
print(a)
a.remove("a")  # removes a from the list
print(a)
