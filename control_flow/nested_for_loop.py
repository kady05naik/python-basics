# Nested for loop

year=[2016,2017]
month=['Jan', 'Feb']
for y in year:
    for m in month:
        for d in range(1,28):
            print(f'Report_{y}_{m}_{d}.csv')