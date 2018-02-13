import os
import time
print('This is a game:')
def shiyan():
	
	numbers=[1,2,3,4]
	print('There are some numbers:\n'+str(numbers))
	print('Which number is your hate most?')
	number=input("please pick a numner:")

	while 123:

		if number == '1':
			numbers.pop(0)
			print('剩下的数组是：'+str(numbers))
			break
		elif number == '2':
			numbers.pop(1)
			print('剩下的数组是：'+str(numbers))
			break
		elif number == '3':
			numbers.pop(2)
			print('剩下的数组是：'+str(numbers))
			break
		elif number == '4':
			numbers.pop(3)
			print('剩下的数组是：'+str(numbers))
			break
		else:
			print('输入错误！')
			break
while 333:
	
    shiyan()
    time.sleep(3)
    os.system("cls")
    os.system("color 3")
    
