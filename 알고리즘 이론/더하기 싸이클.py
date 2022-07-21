n = int(input())
 
def cycle_sum(n):
    num = []
 
    num.append(n//10)
    num.append(n % 10)
 
    sum = num[0] + num[1]
 
    cycle = (num[1]*10) + (sum % 10)
 
    return cycle
 
temp = cycle_sum(n)
count = 1
 
while(1):
 
    if(temp == n):
        break
    else:
        temp = cycle_sum(temp)
        count += 1
 
print(count)
num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)