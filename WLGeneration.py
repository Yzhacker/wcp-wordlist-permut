# WordList Generator - Permutação e Concatenação
# Gera permutação ou concatenação fraser por frase, não junta todas palavras ou fraess do array em uma so para gerar uma nova wordlist, ele é baseado apenas em manipulação de strings e loops simples.
# Lista de frases
frases = [
    "Personal Jesus",
    "Enjoy the Silence",
    "Policy of Truth",
    "World in My Eyes"
]

# Função para processar a wordlist
def gerar_wordlist(frases):
    wordlist = set()  # Usamos um conjunto para evitar duplicatas

    for frase in frases:
        # Adiciona variações da frase original
        wordlist.add(frase)  # Original
        wordlist.add(frase.upper())  # Maiúsculas
        wordlist.add(frase.lower())  # Minúsculas
        wordlist.add(frase.title())  # Capitalizado

        # Adiciona a versão concatenada (sem espaços)
        concatenado = "".join(frase.split())
        wordlist.add(concatenado)
        wordlist.add(concatenado.upper())
        wordlist.add(concatenado.lower())
        wordlist.add(concatenado.title())

        # Adiciona a frase invertida
        invertido = frase[::-1]  # Exemplo: "susieJ lanosreP"
        wordlist.add(invertido)
        wordlist.add(invertido.upper())
        wordlist.add(invertido.lower())
        wordlist.add(invertido.title())

        # Adiciona o concatenado invertido
        concatenado_invertido = concatenado[::-1]
        wordlist.add(concatenado_invertido)
        wordlist.add(concatenado_invertido.upper())
        wordlist.add(concatenado_invertido.lower())
        wordlist.add(concatenado_invertido.title())

    return wordlist

# Gera a wordlist
resultado = gerar_wordlist(frases)

# Salva no arquivo
with open("wordlist_variada.txt", "w") as arquivo:
    for linha in sorted(resultado):
        arquivo.write(linha + "\n")

print(f"Wordlist criada com {len(resultado)} variações e salva em 'wordlist_variada.txt'.")
