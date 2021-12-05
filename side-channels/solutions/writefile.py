import subprocess

# Get target pwnable
pwd = ''.join(f'{__file__}'.split('/')[:-1])
cmds = ['python', f'{pwd}/../writefile.py']

# Construct python code for bit extraction
func_str = """def quiet():
    with open('flag.txt', 'w') as file:
        file.write(flag)"""

# Execute target pwnable
res = subprocess.run(cmds, input=func_str.encode())
