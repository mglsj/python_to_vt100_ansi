from winpty import PtyProcess
from vt100 import *


file_path = r"C:\Users\laksh\Documents\programming\web\encert\src\content\docs\class 12\Computer Science\program_1.1.py"

command = f"python {file_path}"


def generate():
    proc = PtyProcess.spawn(argv=["python", file_path], cwd="")

    content = ""
    try:
        while data := proc.read(1024):
            # print(data)
            content = content + data
    except EOFError:
        pass

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


if __name__ == "__main__":
    generate()
