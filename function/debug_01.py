def sum_all(start, end):
  output = 0
  for i in range(start, end+1):
    output += i
  return output

print('1 to 5:', sum_all(1,5))

#total_sum = 0

#for i in range(1, 5):
#    total_sum += i

#print(f'total_sum : {total_sum}')
#print(f'검증 : {1+2+3+4+5}')