flower_0={}
flower_0['color']='red'
flower_0['flavour']='fragrance'
flower_0['class']='no-eat'
print(flower_0)
flower_0['color']='green'
print(flower_0)
for nature,value in flower_0.items():
    print('nature:'+nature)
    print('value:'+value+'\n')


del flower_0['class']
print(flower_0)
