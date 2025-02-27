import time, math

num = int(input())
delay = int(input())

time.sleep(delay/1000)
print(f"Square root of {num} after {delay} miliseconds is {math.sqrt(num)}")