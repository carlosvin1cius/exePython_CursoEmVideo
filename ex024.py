print("===== EXERCICIO 024 =====")
nome = input("Digite o nome da sua cidade: ")
nome = nome.title()
cidade = nome.split()
print("A CIDADE {} COMEÇA OU NÃO COM A PALAVRA 'SANTO': {}".format(nome, 'Santo' in cidade[0]))

# if cidade[0] == "SANTO":
#   print("A Cidade {} começa com a palavra 'Santo'".format(nome))
# else:
#    print("A cidade {} não começa com a palavra 'Santo' e sim com: {}".format(nome, cidade[0]))
