#Input section
Nome = str(input("Please insert a name: "))

#process section
LengCount = len(Name)
with open("logbook", "a", encoding="utf-8") as arquivo:
    arquivo.write(Name + "\n")

#output section
ultima_linha = ""

with open("logbook", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        ultima_linha = linha

# Remove a quebra de linha do final
ultima_linha = ultima_linha.strip()
print(ultima_linha)

print(f"{LengCount}")
