import platform
import subprocess
import os

system_number = 1 if platform.system() == "Windows" else 2 if platform.system() == "Linux" else "MacOS bruh."

def run(system_number):
    if system_number == 1:
        executable = "xmrig.exe"
    elif system_number == 2:
        executable = "xmrig"
    else:
        print(system_number)
        exit(2137)

    if not os.path.isfile(executable):
        print("no exe run configure.py")
        exit(1)

    command = [executable]

    subprocess.run(command)

run(system_number)