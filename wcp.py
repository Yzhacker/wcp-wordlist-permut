
##  wcp = Wordlist concatenação + Permutação

# Esse Script usa  itertools, necessário apenas se para gerar permutações ou combinações entre diferentes itens da lista de entrada.

# 01 Esse Script faz Permutação + Concatenações de palavras ou frases, se você usar varias palavras ou frazes vai tornar uma so.

#Explicação do Script
 # Permutações:

# O itertools.permutations gera todas as ordens possíveis das palavras na lista. Exemplo: ["admin", "user"] gera:

 #Variações de Cases:

# A manipulação usa funções como .lower(), .upper() e .title() para criar diferentes variações de letras maiúsculas e minúsculas.
# Reversões:

# Adiciona as palavras em ordem inversa com o slicing [::-1].
# Concatenações:

# Usa espaços (" ") e junção direta ("") para criar as combinações com e sem separação.
# Remoção de Duplicatas:

# Usamos set() para garantir que cada variação seja única.

#Customização
# Para adicionar mais palavras, insira-as na lista palavras.
# Para incluir caracteres especiais, insira-os manualmente no conjunto gerado ou adicione uma etapa de geração extra.



import itertools

# Palavra inicial
palavras = ["admin", "user"]

# Função para gerar permutações e manipular strings
def gerar_wordlist(palavras):
    wordlist = set()  # Usamos um conjunto para evitar duplicatas
    
    # Gera permutações das palavras fornecidas
    for perm in itertools.permutations(palavras):
        # Junta as palavras da permutação
        combinado = " ".join(perm)
        junto = "".join(perm)
        
        # Adiciona variações ao conjunto
        wordlist.add(combinado)  # Ex: "admin user"
        wordlist.add(junto)      # Ex: "adminuser"
        wordlist.add(combinado.lower())  # Ex: "admin user"
        wordlist.add(combinado.upper())  # Ex: "ADMIN USER"
        wordlist.add(combinado.title())  # Ex: "Admin User"
        wordlist.add(junto.lower())  # Ex: "adminuser"
        wordlist.add(junto.upper())  # Ex: "ADMINUSER"
        wordlist.add(junto.title())  # Ex: "AdminUser"
        
        # Reversões
        wordlist.add(combinado[::-1])  # Ex: "resu nimda"
        wordlist.add(junto[::-1])      # Ex: "resunimda"

    return wordlist

# Gera e salva a wordlist
resultado = gerar_wordlist(palavras)

# Salva no arquivo
with open("wordlist_permutacoes.txt", "w") as arquivo:
    for linha in sorted(resultado):
        arquivo.write(linha + "\n")
        print(linha)  # Exibe no terminal

print(f"\nWordlist criada com {len(resultado)} variações e salva em 'wordlist_permutacoes.txt'.")
