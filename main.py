import os, sys
import time

path = sys.argv[1]

try:
    file = sys.argv[2]
except IndexError:
    file = "index.html"

try:
    os.path.exists(os.path.join(path, file))
except FileNotFoundError:
    print("File not found")
    time.sleep(2)
    sys.exit(1)

SECURE_TEMPLATE = open(os.path.join(sys.path[0], "template", "securiser.php"), "r").read()

os.system("title=React Securiser")

print("Start Securiser . . .")

globalSecurity = "MVC_PROTOCOL"


while 1:
    tmp = input("Global Security Variable name [{}]: ".format(globalSecurity))
    if tmp == "":
        tmp = globalSecurity
    globalSecurity = tmp
    del tmp

    print("\n")
    break

file = os.path.join(path, file)

mtime = 0
while 1:
    if os.path.getmtime(file) != mtime or mtime == 0:
        os.system("cls")
        print('Compile . . .\n')

        try:
            with open(file, 'r') as f:
                content = f.read()

            content = (SECURE_TEMPLATE.replace("{gsv}", globalSecurity) + content)
            os.remove(file)
            tmp_file = ".".join(file.split(".")[:-1]) + ".php"
            with open(tmp_file, 'w') as f:
                f.write(content)
        except:
            pass

        mtime = os.path.getmtime(tmp_file)
        print('Compiled: OK')
        print("Last compilation:", time.ctime(mtime))
    time.sleep(0.5)