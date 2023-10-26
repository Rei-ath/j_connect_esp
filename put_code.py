import os
import subprocess
import time

ignored_ls = [
    "test.py",
    "terminate.py",
    "__pycache__",
    ".git",
    ".gitignore",
    "put_code.py",
    "boot.py",
    "main.py",
    "microdot"
    
]

# AMPY_PORT = 'AMPY_PORT=/dev/ttyUSB0'

print()
cwd = os.getcwd()
cwdir = os.listdir(cwd)
print(cwdir)
# messages = []
for name in cwdir:
    # print(name)
    if name not in ignored_ls:
        # _path = os.path.join(cwd,name)
        # if os.path.isfile(_path):
            try:
                print("putting : ",name)
                result = subprocess.run(
                    ["ampy", "put", name], stdout=subprocess.PIPE, text=True
                )
                print(f"lodead successfully : {name}")
            except:
                print(f"cant load : {name}")
        # else:
            # _path = os.path.join(cwd,name)
            # _cwd  = os.listdir(_path)
            # subprocess.run(['ampy','mkdir',name])
            # for file in _cwd:
            #     _name = f'{name}/{file}'
            #     print(_name)
            #     try:
            #         result = subprocess.run(
            #             ["ampy", "put", _name], stdout=subprocess.PIPE, text=True
            #         )
            #         print(f"lodead successfully : {_name}")
            #     except:
            #         print(f"cant load : {_name}")
            #     time.sleep(1)

    time.sleep(2)
# print(messages)
print("Loaded everthing: ")
subprocess.run(["ampy", "ls"])