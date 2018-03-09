lists=['bus','mountain','kang','ausa']
print(lists)
# ~ 输出
lists.append('zhi')
lists.insert(1,'yuan')
print(lists)
print(sorted(lists))
# ~ 临时按字母大小写排序输出
print(sorted(lists,reverse=True))
# ~ 按字母顺序反向输出
lists.reverse() 
print(lists)
# ~ 倒叙输出
lists.sort()
print(lists)
# ~ 按字母顺序永久输出
lists.sort(reverse=True)
print(lists)
# ~ 按字母永久倒叙输出
