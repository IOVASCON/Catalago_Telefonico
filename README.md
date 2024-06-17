# Catálogo Telefônico

Este projeto é um sistema de catálogo telefônico simples desenvolvido em Python, utilizando um dicionário para armazenar os contatos e a biblioteca Tkinter para a interface gráfica.

## Estrutura do Projeto

- `utils/`
- `catalogo.py`: Contém a classe `CatalogoTelefonico` com as funcionalidades de incluir, excluir, pesquisar e imprimir contatos.
- `main.py`: Contém a implementação da interface gráfica usando Tkinter e as chamadas das funções do catálogo.
- `README.md`: Este arquivo, com a descrição do projeto.
- `test_tkinter.py`: Arquivo para testes com Tkinter.

## Funcionalidades

1. **Incluir Contato**: Adiciona um contato ao catálogo telefônico.
2. **Excluir Contato**: Remove um contato do catálogo telefônico.
3. **Pesquisar Contato**: Procura e exibe o número de telefone de um contato específico.
4. **Imprimir Catálogo**: Mostra todos os contatos no catálogo telefônico.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `main.py` para iniciar a interface gráfica.

### Arquivo `test_tkinter.py`

## test_tkinter.py

from utils.catalogo import CatalogoTelefonico

## Instanciando a classe CatalogoTelefonico

catalogo = CatalogoTelefonico()

## Testes das funcionalidades

print(catalogo.incluir_contato("Alice", "1234-5678"))
print(catalogo.incluir_contato("Bob", "8765-4321"))
print(catalogo.imprimir_catalogo())

print(catalogo.pesquisar_contato("Alice"))
print(catalogo.excluir_contato("Alice"))
print(catalogo.pesquisar_contato("Alice"))
print(catalogo.imprimir_catalogo())

### Explicações Detalhadas

    1. Instanciando a Classe CatalogoTelefonico:

        O objeto catalogo é criado a partir da classe CatalogoTelefonico, que é onde os números de telefone são armazenados internamente em um dicionário (self.catalogo).

    2. Interface Gráfica:

        Utilizamos a biblioteca Tkinter para criar a interface gráfica. Os campos de entrada (entry_nome e entry_telefone) permitem que o usuário insira dados. Os botões (button_incluir, button_excluir, button_pesquisar e button_imprimir) chamam funções específicas quando clicados.

    3. Funções:

        Incluir: Adiciona um novo contato ao dicionário.
        Excluir: Remove um contato do dicionário.
        Pesquisar: Pesquisa um contato no dicionário e exibe o telefone associado.
        Imprimir: Exibe todos os contatos armazenados no dicionário.

    4. Armazenamento dos Números de Telefone:

        Os números de telefone estão armazenados no dicionário self.catalogo da classe CatalogoTelefonico. Cada entrada no dicionário é um par chave/valor, onde a chave é o nome do contato e o valor é o número de telefone.

## Envio para o GitHub

Para enviar os arquivos do seu disco local para o repositório GitHub, você pode seguir estes passos:

### Navegar até o diretório do projeto

cd /caminho/para/o/diretorio/do/projeto

### Inicializar um repositório Git (se ainda não estiver inicializado)

git init

### Adicionar todos os arquivos ao repositório Git

git add .

### Fazer o commit dos arquivos adicionados

git commit -m "Primeiro commit do projeto de catálogo telefônico"

### Adicionar o repositório remoto no GitHub

git remote add origin [https://github.com/IOVASCON/Catalago_Telefonico.git]

### Enviar os arquivos para o repositório remoto

git push -u origin master
