from random import randint

a = int(input('height: '))
b = int(input('weight: '))

def fielding(h,w):
    field = list()
    for i in range(h):
        field.append([])
        for j in range(w):
            field[i].append('  ')
    return field

field = fielding(a,b)
'''
for i in range(a):
    print(field[i])
'''
grass_percent = int(input('How much percents of field do you want to make with grass: '))

grass_percent/=100
grass_counter=0

def ING(percent, h, w,counter, char):
    if char == '2' or char == '3':
        while counter<int(h*w*percent):
            rand_direction = randint(0,3)
            h_rand = randint(0,h-1)
            w_rand = randint(0,w-1)
            if field[h_rand][w_rand] == '  ':
                if rand_direction == 0:
                    field[h_rand][w_rand] = f'{char}^'
                if rand_direction == 1:
                    field[h_rand][w_rand] = f'{char}>'
                if rand_direction == 2:
                    field[h_rand][w_rand] = f'{char}v'
                if rand_direction == 3:
                    field[h_rand][w_rand] = f'{char}<'
                counter+=1
            else:
                pass
    elif char == '1 ':
        while counter<int(h*w*percent):
            h_rand = randint(0,h-1)
            w_rand = randint(0,w-1)
            if field[h_rand][w_rand] == '  ':
                field[h_rand][w_rand] = char
            else:
                pass
            counter+=1       
    return counter

grass_counter=ING(grass_percent,a,b,grass_counter,'1 ')
'''
for i in range(a):
    print()
    for j in range(b):
        print(field[i][j],end = '')
print()
print(grass_counter)
print(grass_percent*100)

'''
sheeps_percent = int(input(f'how much perents of field do you want to make with sheeps (<{100-grass_percent*100}): '))
sheeps_percent/=100
sheeps_counter = 0
sheeps_counter = ING(sheeps_percent,a,b,sheeps_counter, '2')
'''
def sheeping(percent, h, w):
    global sheeps_counter
    while sheeps_counter<int(h*w*percent):
        h_rand = randint(0,h-1)
        w_rand = randint(0,w-1)
        if field[h_rand][w_rand] == ' ':
            field[h_rand][w_rand] = '2'
            sheeps_counter+=1
        else:
            pass

sheeping(sheeps_percent,a,b)
#da f@ck!
'''
'''
for i in range(a):
    print()
    for j in range(b):
        print(field[i][j],end = '')
print()
print(grass_counter)
print(grass_percent*100)
print(sheeps_percent*100)
print(sheeps_counter)
'''

wolf_percent = int(input(f'how much perents of field do you want to make with wolfs (<{100-grass_percent*100-sheeps_percent*100}): '))
wolf_percent/=100
wolf_counter = 0
wolf_counter = ING(wolf_percent,a,b,wolf_counter, '3')

for i in range(a):
    print()
    for j in range(b):
        print(field[i][j],end = '')
print()
print(grass_counter)
print(grass_percent*100)
print(sheeps_percent*100)
print(sheeps_counter)
print(wolf_counter)
print(wolf_percent*100)
