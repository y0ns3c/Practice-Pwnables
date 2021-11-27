import time

print("This program will request you for a positive integer n.")
print("It will then run some computation using that n-th char of the flag.")
print()
print("This computation will take time proportional to its ascii value.")
print("Specifically, a char with ascii value k will take k - 64 seconds.")
print()

flag = "{flag_SLOTH}"

num = -1
while True:
    try:
        num = int(input(f"Input a number in the range [0, {len(flag)}): "))
        if(0 <= num < len(flag)):
            break
    except:
        pass

val = ord(flag[num])
time.sleep(val - 64)
print(f"The result is {val % 2}")
