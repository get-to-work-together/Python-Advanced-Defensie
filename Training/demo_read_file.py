keyword = 'class'

filename = 'functions.py'

found_keyword = False

with open(filename, mode='r') as f:
    for line in f:
        if keyword in line:
            found_keyword = True
            break

if found_keyword:
    print(f'File "{filename}" contains the keyword "{keyword}".')
else:
    print(f'File "{filename}" contains NOT the keyword "{keyword}".')


# with open(filename, mode='r') as f:
#     content = f.read()
#     print(content)

# if keyword in content:
#     print(f'File "{filename}" contains the keyword "{keyword}".')
