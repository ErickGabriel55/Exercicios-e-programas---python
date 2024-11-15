strings = ["apple", "pear", "kiwis"]
print("First code without for loop:")
print(f"1- {strings[0][0]}")
print(f"1.2- {strings[0][1]}")
print(f"2- {strings[1][1]}")
print(f"3- {strings[2][2]}")

print("-" * 40)
print("Second code with for loop:")
lista = ["apple", "pear", "kiwis"]
x = 0


for palavra in lista:
    print(palavra)

for palavra in lista: # acessa as palavras da listas
    for letra in palavra: # acessa cada letra de cada palavra
        print(letra)
        x += 1
        if x == len(palavra):
            print("-" * 20)
            x = 0


