#Prime number between interval 900 to 1000

start = 900
end = 1000

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)