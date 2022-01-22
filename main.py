"""
Double every multiple of 3 in input list. Print the list again.
Input-> [4,12,17,21]
Output-> [4,24,17,42]
"""

lst = [4,12,17,21]
ln = len(lst)
index = 0
for i in range(0,ln):
  e = lst[i]
  if(e%3==0):
    e = e*2
    lst[i] = e
print(lst)
