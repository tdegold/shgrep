import sys

filepath = sys.argv[1]
shell_lines = []
shellblock = False
count = 0

print("begin sanning " + filepath + "...")

with open(filepath) as markdown_file:
    content = markdown_file.read()
    
    lines = content.split("\n")
    
    for line in lines:
        if line == "```shell":
            shellblock = True
        elif (shellblock == True and line == "```"):
            shellblock = False
        elif shellblock == True:
            shell_lines.append(line)
            count = count + 1
            print([count, line])
            
with open("commands.sh", "w") as sh_file:
    for line in shell_lines:
        sh_file.write(line+"\n")

print("Done!")
     