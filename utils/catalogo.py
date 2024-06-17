# utils/catalogo.py

# Definição da classe CatalogoTelefonico para gerenciar o catálogo de contatos
class CatalogoTelefonico:
    def __init__(self):
        # Inicializa o dicionário para armazenar os contatos
        self.catalogo = {}

    # Método para incluir um contato no catálogo
    def incluir_contato(self, nome, telefone):
        self.catalogo[nome] = telefone
        return f"Contato '{nome}' incluído com sucesso."

    # Método para excluir um contato do catálogo
    def excluir_contato(self, nome):
        if nome in self.catalogo:
            del self.catalogo[nome]
            return f"Contato '{nome}' excluído com sucesso."
        else:
            return f"Contato '{nome}' não encontrado no catálogo."

    # Método para pesquisar um contato no catálogo
    def pesquisar_contato(self, nome):
        if nome in self.catalogo:
            return f"O número de telefone de '{nome}' é {self.catalogo[nome]}."
        else:
            return f"Contato '{nome}' não existe no catálogo."

    # Método para imprimir todos os contatos do catálogo
    def imprimir_catalogo(self):
        if self.catalogo:
            catalogo_str = "Catálogo Telefônico:\n"
            for nome, telefone in self.catalogo.items():
                catalogo_str += f"Nome: {nome}, Telefone: {telefone}\n"
            return catalogo_str
        else:
            return "O catálogo está vazio."
