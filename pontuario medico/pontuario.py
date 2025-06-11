class Paciente:
    def __init__(self, identificador=-1, nome=None, altura=None, idade=None, peso=None):
        self.identificador = identificador
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

class PontuarioMedico:
    def __init__(self, tam=10):
        self.pontuario = [Paciente() for _ in range(tam)]
        self.tam = tam

    def imprimir_menu(self):
        print("---------PONTUARIO MEDICO---------")
        print("Digite 1: Inicializar o pontuario.")
        print("Digite 2: imprimir um paciente.")
        print("Digite 3: inserir um paciente.")
        print("Digite 4: editar um paciente.")
        print("Digite 5: Sair.")
        print("------------------------------------")

    def inicializar_pontuario(self):
        for i in range(self.tam):
            self.pontuario[i].identificador = -1
        print("pontuario medico inicializado com sucesso!")

    @staticmethod
    def ler_paciente():
        paciente = Paciente()

        paciente.identificador = int(input("Digite o indentificador do paciente: "))
        paciente.nome = input("Digite o seu nome: ")
        paciente.altura = float(input("Digite a sua altura: "))
        paciente.idade = int(input("Digite a sua idade: "))
        paciente.peso = float(input("Digite o seu peso: "))

        return paciente

    @staticmethod
    def imprimir_paciente(paciente):
        print("--------Paciente----------")
        print("Indentificador: ", paciente.identificador)
        print("Nome: ", paciente.nome)
        print("Altura: ", paciente.altura)
        print("Idade: ", paciente.idade)
        print("Peso: ", paciente.peso)
        print("--------------------------")

    def adicionar_paciente(self):
        print("Adicionando pacientes no pontuario medico...")

        adicionou = False

        for i in range(self.tam):
            if self.pontuario[i].identificador == -1:
                paciente_adicionar = self.ler_paciente()
                self.pontuario[i] = paciente_adicionar
                adicionou = True
                break

        if adicionou:
            print("Paciente adicionado no pontuario com sucesso!")
        else:
            print("Paciente nao adicionado no pontuario! Pontuario cheio.")

    def imprimir_pontuario(self):
        print("Imprimindo pontuario medico...")
        imprimiu = False

        for i in range(self.tam):
            if self.pontuario[i].identificador != -1:
                self.imprimir_paciente(self.pontuario[i])
                imprimiu = True

        if not imprimiu:
            print("Pontuario medico vazio! Adicione um paciente.")

    def editar_paciente(self):
        editar_nome = input("Digite o nome do paciente que deseja editar: ")

        print("Digite o que deseja editar: ")
        print("Digite 1: Nome.")
        print("Digite 2: Altura.")
        print("Digite 3: Idade.")
        print("Digite 4: Peso.")
        opcao = int(input())

        for i in range(self.tam):
            if self.pontuario[i].nome == editar_nome:
                if opcao == 1:
                    self.pontuario[i].nome = input("Digite o novo nome: ")
                elif opcao == 2:
                    self.pontuario[i].altura = float(input("Digite a nova altura: "))
                elif opcao == 3:
                    self.pontuario[i].idade = int(input("Digite a nova idade: "))
                elif opcao == 4:
                    self.pontuario[i].peso = float(input("Digite o novo peso: "))
                else:
                    print("Opcao invalida!")
                break
        else:
            print("Paciente nao encontrado no pontuario!")

    def remover_paciente(self):
        remover_nome = input("Digite o nome do paciente que deseja remover: ")

        for i in range(self.tam):
            if self.pontuario[i].nome == remover_nome:
                self.pontuario[i].identificador = -1
                print("Paciente removido com sucesso!")
                break
        else:
            print("Paciente nao encontrado no pontuario!")

    def executar(self):
        opcao = 0

        while opcao != 6:
            self.imprimir_menu()
            opcao = int(input("Digite a opcao desejada: "))

            if opcao == 1:
                self.adicionar_paciente()
            elif opcao == 2:
                self.imprimir_pontuario()
            elif opcao == 3:
                self.editar_paciente()
            elif opcao == 4:
                self.remover_paciente()
            elif opcao == 5:
                print("Saindo...")
            else:
                print("Opcao invalida!")

if __name__ == "__main__":
    pontuario_medico = PontuarioMedico()
    pontuario_medico.executar()