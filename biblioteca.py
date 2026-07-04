ARQUIVO   = "livros.txt"
SEPARADOR = "|"


def carregar_livros():
    livros = []
    arquivo = open(ARQUIVO, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        linha = linha.strip()
        if linha == "":
            continue
        partes = linha.split(SEPARADOR)
        if len(partes) == 5:
            livro = {
                "titulo": partes[0],
                "autor":  partes[1],
                "genero": partes[2],
                "ano":    partes[3],
                "status": partes[4]
            }
            livros.append(livro)

    return livros


def salvar_livros(livros):
    arquivo = open(ARQUIVO, "w", encoding="utf-8")
    for livro in livros:
        linha = (livro["titulo"] + SEPARADOR +
                 livro["autor"]  + SEPARADOR +
                 livro["genero"] + SEPARADOR +
                 livro["ano"]    + SEPARADOR +
                 livro["status"] + "\n")
        arquivo.write(linha)
    arquivo.close()

#comand#
def linha():
    print("-" * 45)


def cabecalho(titulo):
    print()
    linha()
    print("  " + titulo)
    linha()


def pausar():
    input("\n  Pressione ENTER para continuar...")


def ler_texto(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada != "" and SEPARADOR not in entrada:
            return entrada
        print("  ! Campo obrigatorio. Nao use o caractere |")
#fimcomand#

def ler_inteiro(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit():
            numero = int(entrada)
            if minimo <= numero <= maximo:
                return numero
        print("  ! Digite um numero entre " + str(minimo) + " e " + str(maximo) + ".")


def cadastrar(livros):
    cabecalho("CADASTRAR LIVRO")

    titulo = ler_texto("  Titulo : ")
    autor  = ler_texto("  Autor  : ")
    genero = ler_texto("  Genero : ")
    ano    = str(ler_inteiro("  Ano    : ", 1000, 2100))

    print("\n  Status:")
    print("  1 - Disponivel")
    print("  2 - Emprestado")
    opcao = ler_inteiro("  Escolha: ", 1, 2)
    status = "Disponivel" if opcao == 1 else "Emprestado"

    livro = {
        "titulo": titulo,
        "autor":  autor,
        "genero": genero,
        "ano":    ano,
        "status": status
    }

    livros.append(livro)
    salvar_livros(livros)
    print("\n  Livro cadastrado!")
    pausar()


def listar(livros):
    cabecalho("ACERVO COMPLETO")

    if len(livros) == 0:
        print("\n  Nenhum livro cadastrado.")
        pausar()
        return

    print("\n  Total: " + str(len(livros)) + " livro(s)\n")

    for i in range(len(livros)):
        livro = livros[i]
        print("  [" + str(i + 1) + "] " + livro["titulo"] + " - " + livro["autor"])
        print("      " + livro["genero"] + " | " + livro["ano"] + " | " + livro["status"])

    pausar()


def buscar(livros):
    cabecalho("BUSCAR LIVRO")

    if len(livros) == 0:
        print("\n  Nenhum livro cadastrado.")
        pausar()
        return

    print("  1 - Buscar por titulo")
    print("  2 - Buscar por genero")
    opcao = ler_inteiro("  Escolha: ", 1, 2)

    termo = ler_texto("  Termo de busca: ").lower()

    encontrados = []
    for livro in livros:
        if opcao == 1:
            campo = livro["titulo"].lower()
        else:
            campo = livro["genero"].lower()

        if termo in campo:
            encontrados.append(livro)

    if len(encontrados) == 0:
        print("\n  Nenhum livro encontrado.")
    else:
        print("\n  " + str(len(encontrados)) + " resultado(s):\n")
        for livro in encontrados:
            print("  - " + livro["titulo"] + " - " + livro["autor"])
            print("    " + livro["genero"] + " | " + livro["ano"] + " | " + livro["status"])

    pausar()


def editar(livros):
    cabecalho("EDITAR LIVRO")

    if len(livros) == 0:
        print("\n  Nenhum livro cadastrado.")
        pausar()
        return

    for i in range(len(livros)):
        print("  [" + str(i + 1) + "] " + livros[i]["titulo"])

    escolha = ler_inteiro("\n  Numero do livro: ", 1, len(livros))
    livro = livros[escolha - 1]

    print("\n  Editando: " + livro["titulo"])
    print("  (ENTER para manter o valor atual)\n")

    novo = input("  Titulo [" + livro["titulo"] + "]: ").strip()
    if novo != "" and SEPARADOR not in novo:
        livro["titulo"] = novo

    novo = input("  Autor [" + livro["autor"] + "]: ").strip()
    if novo != "" and SEPARADOR not in novo:
        livro["autor"] = novo

    novo = input("  Genero [" + livro["genero"] + "]: ").strip()
    if novo != "" and SEPARADOR not in novo:
        livro["genero"] = novo

    novo = input("  Ano [" + livro["ano"] + "]: ").strip()
    if novo.isdigit():
        numero = int(novo)
        if 1000 <= numero <= 2100:
            livro["ano"] = novo

    print("\n  Status atual: " + livro["status"])
    print("  1 - Disponivel  2 - Emprestado  0 - Manter")
    opcao = ler_inteiro("  Escolha: ", 0, 2)
    if opcao == 1:
        livro["status"] = "Disponivel"
    elif opcao == 2:
        livro["status"] = "Emprestado"

    salvar_livros(livros)
    print("\n  Livro atualizado!")
    pausar()


def remover(livros):
    cabecalho("REMOVER LIVRO")

    if len(livros) == 0:
        print("\n  Nenhum livro cadastrado.")
        pausar()
        return

    for i in range(len(livros)):
        print("  [" + str(i + 1) + "] " + livros[i]["titulo"])

    escolha = ler_inteiro("\n  Numero do livro: ", 1, len(livros))
    livro = livros[escolha - 1]

    confirmacao = input("\n  Remover '" + livro["titulo"] + "'? (S para confirmar): ").strip().upper()

    if confirmacao == "S":
        livros.pop(escolha - 1)
        salvar_livros(livros)
        print("\n  Livro removido!")
    else:
        print("\n  Cancelado.")

    pausar()


def menu():
    livros = carregar_livros()

    while True:
        print()
        linha()
        print("  BIBLIOTECA POPULAR")
        linha()
        print("  1 - Cadastrar livro")
        print("  2 - Listar livros")
        print("  3 - Buscar livro")
        print("  4 - Editar livro")
        print("  5 - Remover livro")
        print("  0 - Sair")
        linha()

        opcao = input("  Escolha: ").strip()

        if opcao == "1":
            cadastrar(livros)
        elif opcao == "2":
            listar(livros)
        elif opcao == "3":
            buscar(livros)
        elif opcao == "4":
            editar(livros)
        elif opcao == "5":
            remover(livros)
        elif opcao == "0":
            print("\n  Ate logo!\n")
            break
        else:
            print("\n  ! Opcao invalida.")


menu()
