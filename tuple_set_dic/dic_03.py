my_bag = {'필통':'파란색', '공책':'노란색', '지갑':'빨간색'}
print(f'my_bag = {my_bag}')
print(f'-'*20)

print(my_bag['필통'])
print(my_bag['공책'])

my_bag['지갑'] = '초록색'
my_bag['물통'] = '하얀색'
print(f'my_bag = {my_bag}')
print(f'-' * 20)
del my_bag['공책']
print(f'my_bag = {my_bag}')

for i in my_bag:
    print(f'key = {i} value = {my_bag[i]}')