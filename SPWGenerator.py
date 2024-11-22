# 2 Simple Permutation - Wordlist Generator
# Script baseado apenas em manipulação de strings e loops simples.
# Lista de frases
#
frases = [
    "Personal Jesus", # exemplo 
    "Enjoy the Silence", # exemplo 
    "Policy of Truth", # exemplo 
    "World in My Eyes" # exemplo 
]

# Função para processar a wordlist
def gerar_wordlist(frases):
    wordlist = set()  # Usamos um conjunto para evitar duplicatas

    for frase in frases:
        # Adiciona a frase original
        wordlist.add(frase)
        
        # Adiciona a versão concatenada (sem espaços)
        concatenado = "".join(frase.split())
        wordlist.add(concatenado)

    return wordlist

# Gera a wordlist
resultado = gerar_wordlist(frases)

# Salva no arquivo
with open("wordlist_simples.txt", "w") as arquivo:
    for linha in sorted(resultado):
        arquivo.write(linha + "\n")

print(f"Wordlist criada com {len(resultado)} variações e salva em 'wordlist_simples.txt'.")
