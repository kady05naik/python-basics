print(all(['a','b',None]))      # None- False
print(all(['a','b','c','']))    # '' Empty String - False
print(all(['a','b',' ']))       # ' ' contains space hence, True

print(all([1,2,None]))          # None - False
print(all([-1,2]))              # True
print(all([1,2,0]))             # 0 - False

print('Any:',any(['a','b',None]))       # True 
print('Any:',any(['a','b','c','']))     # True
print('Any:', any([None, None]))        # False
print('Any:', any([0,0,0]))             # False