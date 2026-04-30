emails=[
    'data@gmail.com',
    'kady@outlook.com',
    'maria@gmail.com',
    'DROP TABLE USERS;f',
    'rocky@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f'Processing Email : {email}')