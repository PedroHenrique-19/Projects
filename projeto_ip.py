# Gestão de estoque
""" obs: esses tipos de formatação para deixar o código mais bonito e essa maneira de criar arquivo
 eu vi no canal do curso em vídeo, enquanto estudava sobre os assuntos."""


def verificar_existencia():  # Verifica se existe um aquivo, se não retorna false.
    try:
        a = open("arquivo_projeto", 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo():  # Cria o arquivo.
    a = open("arquivo_projeto", 'wt+')
    a.close()


estoque = {}  # Cria o dicionário.


def listar_produtos():  # vai listar os produtos do dicionário.
    global estoque
    try:
        with open("arquivo_projeto", "r") as arquivo:
            for linha in arquivo:
                identificador, nome, categoria, quantidade, valor = linha.strip().split(", ")
                estoque[identificador] = {
                    "nome": nome,
                    "categoria": categoria,
                    "quantidade": int(quantidade),
                    "valor": float(valor)
                }
    except FileNotFoundError:
        print('\033[31mArquivo inexistente.\033[m')


def adicionar_estoque(identificador, produto):  # Função pra salvar o estoque quando preciso.
    with open("arquivo_projeto", "a") as arquivo:
        arquivo.write(f"{identificador}, {produto['nome']}, {produto['categoria']}, {produto['quantidade']}"
                      f", {produto['valor']}\n")


def menu_opcoes():  # Menu de opções do usuário
    print('-' * 48)
    print('\033[34mBem-vindo ao menu de opções! Como posso ajudar?\033[m')  # Usei esses códigos para adiconar cor.
    print('-' * 48)
    print('1 - Inserção')
    print('2 - Remoção')
    print('3 - listagem')
    print('4 - tamanho')
    print('5 - procurar')
    print('6 - Sair')

    opcao = int(input('\033[35mEscolha uma das opções acima ou digite "6" para encerrar:\033[m '))
    return opcao


def insercao():  # O usuário vai poder inserir produtos aqui.
    global estoque
    print('-' * 27)
    print('\033[33mInsira os dados do produto:\033[m ')
    print('-' * 27)
    
    identificador = input('Identificador: ')

    if identificador in estoque:
        print("\033[31mERRO: identificador já existente.\033[m")
        return

    nome = input('Nome: ')
    categoria = input('Categoria: ')
    quantidade = input('Quantidade: ')
    valor = input('Valor: ')

    try:  # Aqui o usuário verá uma mensagem de erro se a quantidade ou o valor não for um número.

        quantidade = int(quantidade)
        valor = float(valor)
    except ValueError:
        print('\033[31mERRO: valor ou quantidade inválidos. Por favor, insira dados válidos.\033[m')
        return

    estoque[identificador] = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "valor": valor
    }
    adicionar_estoque(identificador, estoque[identificador])

    print('\033[36mProduto inserido\033[m')


def remocao():  # Usuário poderá re mover algum produto.
    identificador = input('Qual o identificador do intem que você deseja remover? ')

    if identificador in estoque:
        del estoque[identificador]

        with open("arquivo_projeto", "w") as arquivo:  # Aqui, quando ele deletar o produto, ele vai reescrever o arquivo.
            for identificador, produto in estoque.items():
                arquivo.write(f"{identificador}, {['nome']}, {produto['categoria']}, {produto['quantidade']}"
                              f", {produto['valor']}\n")
        print('\033[34mProduto removido com sucesso\033[m!')
    else:
        print('\033[34mERRO: produto não encontrado\033[m!')


def listagem():  # aqui imprime o aquivo.
    try:
        # Aqui eu usei essa formatação pra ficar mais visível cada informação do produto, utilizando esses espaços.
        print(f"{'Identificador':<15} {'Nome':<10} {'Categoria':<15} {'Quantidade':<10} {'Valor':<10}")
        print("-" * 60)  # Linha separadora

        # Ler cada linha do arquivo
        for identificador, produtos in estoque.items():
            print(f"{identificador:<15} {produtos['nome']:<10} {produtos['categoria']:<15} "
                  f"{produtos['quantidade']:<10} {produtos['valor']:<10}")

    except FileNotFoundError:
        print('\033[31mERRO: arquivo inexistente.\033[m')


def verificar_tamanho():  # a lógica aqui foi definir uma variável pra contar o tamanho do identificador.
    tamanho = 0

    try:
        with open("arquivo_projeto", "r") as arquivo:
            for i in arquivo:
                linha_arquivo = i.strip().split(", ")
                if len(linha_arquivo[0]) >= 1:  # se existir um identificador, tamanho aumenta 1.
                    tamanho += 1

        if tamanho == 0:
            print('Não foi encontrado nenhum produto.')

    except FileNotFoundError:
        print('\033[31mArquivo inexistente.\033[m')

    return tamanho


def procurar(tamanho):  # aqui eu usei o tamanho como parâmetro pro range.
    produto_procurar = input('Qual o identificador do intem que você deseja procurar? ')

    posicao = 0
    encontrado = False

    try:
        with open("arquivo_projeto", "r") as arquivo:
            for i, linha in enumerate(arquivo):  # enumerate pra ele poder iterar sobre cada linha.
                linha_arquivo = linha.strip().split(", ")
                if linha_arquivo[0] == produto_procurar:
                    encontrado = True
                    posicao = i + 1
                    print(f'Produto na linha {posicao}: {linha_arquivo}')

        if not encontrado:
            print('\033[31mProduto não encontrado\033[m')            

    except FileNotFoundError:
        print('\033[31mArquivo inexistente.\033[m')

    return posicao


if not verificar_existencia():  # Vai verificar o valor da existencia, se for falso chama a criar_aqruivo.
    criar_arquivo()


listar_produtos()  # Chama a listagem de produtos, pra quando eu encerrar, na próxima chamada eles estarem lá.

while True:  # Aqui cada função vai ser chamada dependendo do que é desejado.
    opcoes = menu_opcoes()

    if opcoes == 1:
        insercao()
    elif opcoes == 2:
        remocao()
    elif opcoes == 3:
        listagem()
    elif opcoes == 4:
        tamanho = verificar_tamanho()
        if tamanho > 0:
            print(f'Existe(m) {tamanho} produto(s) no estoque.')
    elif opcoes == 5:
        tamanho = verificar_tamanho()
        if tamanho > 0:
            procurar(tamanho)
    elif opcoes == 6:
        print('Até a próxima...')
        break
    else:
        print('\033[31mERRO: opção inválida. Tente novamente!\033[m')  # Caso seja digitado um número fora do range.

    """Nessa chamada 4 e 5 eu precisei fazer desse jeito, pois quando eu chamada a 5 ela retornava o valor da 4"""
