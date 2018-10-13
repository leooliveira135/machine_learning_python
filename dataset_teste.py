with open('testes_arquivos/dataset.txt','r') as f:
    """for linha in f.readlines():
        print(linha)"""
    #conteudo = f.read()
    lista = f.read().splitlines()
    print(len(lista))