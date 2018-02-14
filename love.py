import os
import time
print("\n"+'(情人节)'+time.strftime('%Y-%m-%d %H:%M:%S')+"	"+"From a coder：")
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-50, 30)]) for y in range(20, -30, -1)]))

os.system("color b5")

os.system("pause")


