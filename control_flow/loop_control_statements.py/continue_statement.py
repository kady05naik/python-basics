# Loop through a list of days and print only the working days, skipping the weekends

days=['Sunday  ','Monday','Tuesday','  Wednesday','Thursday','Friday','Saturday']

for day in days:
    if day.strip().lower() in ('saturday', 'sunday'):
        continue
    print(day.strip())