print('Iniciando escrita de arquivo')
texto = """
Aprendendo python
machine learning
python é muito legal
"""
run = str(input('Escolha a forma de execução (w, a)'))

if run == 'w':
    arq = open('testes_arquivos/arquivo.txt',run)
    arq.write('-----------Escrevendo com o modo write-----------')
    arq.write(texto)
    arq.close()
    print('Finalizando escrita de arquivo')
elif run == 'a':
    arq = open('testes_arquivos/arquivo.txt', run)
    a = int(input('Digite quantas vezes deseja executar este arquivo: '))

    if a<=0:
        print("Número inválido")

    else:
        x = 1
        while x <= a:
            #arq.write('machine learning')
            #arq.write('\n aprendendo python')
            arq.write('-----------Escrevendo com o modo append-----------')
            arq.write(texto)
            x += 1
        arq.close()
        print('Finalizando escrita de arquivo')