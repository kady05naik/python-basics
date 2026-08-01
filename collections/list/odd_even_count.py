def count_even_odd(lst):
    even=0
    odd=0
    for num in lst:
        if num%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[4,6,2,3,5,0]
tup=count_even_odd(lst)
print(f"EVEN :  {tup[0]} \nOdd : {tup[1]}")