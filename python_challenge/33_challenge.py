'''
Count Number of Odd and Even Elements in a List

'''

def  count_even_odd(lst):
    ecnt,ocnt=0,0
    for i in lst:
        if i % 2==0 :
            ecnt+=1
        else:
            ocnt+=1
    print(f'Count even numbers: {ecnt}')
    print(f'Count odd numbers: {ocnt}')



n=int(input(f'Enter Total number of list to be enter:'))
lst=[]
for i in range(n):
    lst.append(int(input(f'Enter lst[{i}] : ')))

count_even_odd(lst)