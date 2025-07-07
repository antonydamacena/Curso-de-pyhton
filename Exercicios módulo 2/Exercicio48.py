s=0
for impar in range(1,500+1, 2):
        if impar%3 == 0 :
                print(impar, end= ' ')
                s+= impar # s= s+par            
print(s)
