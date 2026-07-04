# Biblioteca Popular

Sistema simples de gerenciamento de acervo para uma biblioteca publica municipal.
Feito em Python puro, sem dependencias externas.

---

## Integrantes

- Miguel Vinícius Messias Da Silva
- Gleybson Anderson da Silva Nascimento
- André Luís Freitas de Santana

---

## O que o sistema faz

O programa permite controlar os livros de uma biblioteca pelo terminal:
cadastrar novos livros, listar o acervo, buscar por titulo ou genero,
editar informacoes e remover livros. Tudo fica salvo no arquivo `livros.txt`.

---

## Como rodar

Voce so precisa ter Python 3 instalado. Sem biblioteca extra, sem configuracao.

```bash
python biblioteca.py
```

Se o arquivo `livros.txt` nao existir, o programa comeca com o acervo vazio mesmo.

---

## Arquivos

| Arquivo         | Para que serve                              |
|-----------------|---------------------------------------------|
| `biblioteca.py` | Codigo principal do sistema                 |
| `livros.txt`    | Onde os dados dos livros ficam salvos       |
| `README.md`     | Este arquivo                                |

---

## Divisao de tarefas

| Integrante                            | O que fez                                               |
|---------------------------------------|---------------------------------------------------------|
| Miguel Vinícius Messias Da Silva      | Cadastro de livros e leitura/escrita do arquivo .txt    |
| Gleybson Anderson da Silva Nascimento | Listagem, busca e funcoes de validacao de entrada       |
| André Luís Freitas de Santana         | Edicao, remocao e menu principal                        |

---

## Conceitos usados

Aplicamos o que foi visto em aula:

- Variaveis, strings e inteiros
- `input()` e `print()`
- `if`, `elif`, `else`
- Lacos `for` e `while`
- Funcoes com parametros e retorno
- Listas e dicionarios
- Leitura e escrita de arquivos com `open()`
- Tratamento basico de erros com `try/except`
