def generateTable(n):
    table = ""
    for i in range(1, 11):
        table = table +f"{n} x {i} = {n * i}\n"
    with open(f"Chapter 9 - File/tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(1, 11):
    generateTable(i)
