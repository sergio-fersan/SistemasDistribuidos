import zmq
import json


context = zmq.Context()

socket = context.socket(zmq.REQ)

socket.connect("tcp://broker:5555")

#Função enviar_requisicao:
def enviar_requisicao(dados):
    mensagem = json.dumps(dados).encode()

    socket.send(mensagem)

    resposta = socket.recv()

    return json.loads(resposta.decode())

#Menu geral, das funções:
while True:
    print("\nTask manager:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o titulo da tarefa: ")

        dados = {
            "operacao": "adicionar",
            "titulo": titulo
        }

        resposta = enviar_requisicao(dados)

        print(resposta["mensagem"])
        print(f"Tarefa: {resposta['tarefa']}")

    elif opcao == "2":
        id_tarefa = int(input("Digite o ID da tarefa: "))

        dados = {
            "operacao": "remover",
            "id": id_tarefa
        }

        resposta = enviar_requisicao(dados)

        print(resposta["mensagem"])

    elif opcao == "3":
        dados = {
            "operacao": "listar"
        }

        resposta = enviar_requisicao(dados)

        print("\nTarefas:")

        if len(resposta["tarefas"]) == 0:
            print("Lista de tarefas vazia")
        else:
            for tarefa in resposta["tarefas"]:
                print(
                    f"{tarefa['id']} - {tarefa['titulo']}"
                )

    elif opcao == "0":
        print("Desligando....")
        break

    else:
        print("Opção invalida.")