from collections import OrderedDict
menu={
    '1':'mushroom',
    '2':'broccoli',
    '3':'bean',
    '4':'celery',
    '5':'carrot',
    '6':'cucumber'
    }
print('VEGETABLE MENU:\n')
#按顺序输出 先排序 然后用map()函数映射到lambda定义的函数中 然后打印输出
# ~ print('\n'.join(map(lambda item:'Number:%s\tVegetable: %s' % item ,
    # ~ sorted(menu.items(),key=lambda m:m[0]))))
for number,value in menu.items():
    message='Number:'+number+'\tVegetable: '+value.title()
    print(message)
request_memu=[]
message='\nPlease select which vegetable would you like to choose:'
message+="\n(If you want to make the pizza please input 'ok')\n"
print(message)
sign=True
while sign:
    request=input()
    if request!='ok' and request in menu.keys():
        request_0={key:value for key,value in menu.items()}
        request=request_0[request]
        request_memu.append(request)
    elif request=='ok':
        sign=False
if request_memu:
    print('\nPlease add these vegetables to my pizza:')
    for request in request_memu:
        print(request.title())
else:
    print('\nPlease take a prime pizza')
