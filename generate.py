from winpty import PtyProcess

input_data = ""

with open("input.txt", "r") as f:
    input_data = f.read()

proc = PtyProcess.spawn("python")
proc.write(input_data)

proc.write("\nexit()\n")

content = ""
try:
    while data := proc.read(1024):
        # print(data)
        content = content + data
except EOFError:
    pass

from vt100 import *

t = Terminal(100, 100, False, TextFormatter())
t.parse(content)

result = t.to_string() or ""
lines = result.split("\n")
if lines[-1] == "":
    result = "\n".join(lines[:-2])
else:
    result = "\n".join(lines[:-1])

with open("output.txt", "w", encoding="UTF8") as f:
    f.write(result)
