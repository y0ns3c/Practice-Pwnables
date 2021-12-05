import subprocess
import time

def getChar(char_pos):
    # Get target pwnable
    pwd = ''.join(f'{__file__}'.split('/')[:-1])
    cmds = ['python', f'{pwd}/../runtime.py']

    # Record start time
    start = time.time()

    # Execute target pwnable
    res = subprocess.run(cmds, input=str(char_pos).encode(), capture_output=True)

    # Get character from execution time
    duration = time.time() - start
    char_val = round(duration) + 64

    return chr(char_val)

# Since flag length and format is known, get characters up to 2nd last char
flag_chars = ['{', 'f', 'l', 'a', 'g', '_']
flag_len = 12
for i in range(6, flag_len - 1):
    char = getChar(i)
    print(f'Obtained char = {char}')
    flag_chars.append(char)

flag = ''.join(flag_chars) + '}'
print(f'flag = {flag}')
