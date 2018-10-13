print('Iniciando escrita de arquivo')
texto = """
Aprendendo python
machine learning
python é muito legal
"""
run = str(input('Escolha a forma de execução (w, a) '))

if run == 'w':
    with open('testes_arquivos/arquivo.txt',run) as f:
        f.write('-----------Escrevendo com o modo write-----------')
        f.write(texto)
        f.close()
    print('Finalizando escrita de arquivo')
elif run == 'a':
    with open('testes_arquivos/arquivo.txt', run) as f:
        a = int(input('Digite quantas vezes deseja executar este arquivo: '))

        if a<=0:
            print("Número inválido")

        else:
            x = 1
            while x <= a:
                #arq.write('machine learning')
                #arq.write('\n aprendendo python')
                f.write('-----------Escrevendo com o modo append-----------')
                f.write(texto)
                x += 1
            f.close()
            print('Finalizando escrita de arquivo')