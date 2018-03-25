families=['dad','mom','me','sister','grandmother','grandfather','wife','son',
'daughter']
print(sorted(families,reverse=True))
#倒打字母排序
families.reverse()
print(families)
#倒打顺序
families.sort()
print(families)
#打顺序永久
for families_mumber in families:
    # ~ print(families_mumber.title())
    print("hello,"+families_mumber.title()+",happy new year!\n")

families_fuben=families[:]
print(families)
print(families_fuben)

families.append('zhi')
families_fuben.append("kang")
print(families)
print(families_fuben)


for member in families[-3:]:
    message="here are three mumeber in the end of the families:"
    print(message+member.title())
families=['dad','mom','me','sister','grandmother','grandfather','wife','son',
'daughter']
print(sorted(families,reverse=True))
#倒打字母排序
families.reverse()
print(families)
#倒打顺序
families.sort()
print(families)
#打顺序永久
for families_mumber in families:
    # ~ print(families_mumber.title())
    print("hello,"+families_mumber.title()+",happy new year!\n")

families_fuben=families[:]
print(families)
print(families_fuben)

families.append('zhi')
families_fuben.append("kang")
print(families)
print(families_fuben)
for member in families[-3:]:
    message="here are three mumeber in the end of the families:"
    print(message+member.title())

