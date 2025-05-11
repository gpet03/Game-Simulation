import random

def simulation(my_num):
    numbers=[my_num, random.randint(1,10),min(random.randint(1,99)+5,99),min(random.randint(1,99)+5,99),min(random.randint(1,99)+5,99),min(random.randint(1,99)+5,99),min(random.randint(1,99)+5,99),min(random.randint(1,99)+5,99),min(random.randint(1,99)+5,99)]
    avg=(sum(numbers))/len(numbers)
    numbers_above=[]
    for number in numbers:
        if number>avg:
            numbers_above.append(number)
    winner=min(numbers_above)
    count=numbers_above.count(winner)
    if count>2:
        for j in range(count):
            numbers_above.remove(winner)
        if numbers_above!=[]:
            winner=min(numbers_above)
        else:
            numbers_below=[]
            for number in numbers:
                if number<avg:
                    numbers_below.append(number)
            winner=max(numbers_below)
    if winner==my_num:
        return True
    else:
        return False
    
for i in range (100):
    dic={}
    dic[i]=0
    for j in range (100000):
        if simulation(i)==True:
            dic[i]+=1
    dic[i]=round(dic[i]/100000*100,2)
    if dic[i]>-1:
        print(dic)