import zmq
import json

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

tarefas = []
contador = 0

while True:
    message = socket.recv()

    dados = json.loads(message.decode())

    operacao = dados["operacao"]

    print(f"Mensagem recebida: {dados}", flush=True)

    if operacao == "adicionar":
        contador += 1

        tarefa = {
            "id": contador,
            "titulo": dados["titulo"]
        }

        tarefas.append(tarefa)

        resposta = {
            "mensagem": "Tarefa adicionada",
            "tarefa": tarefa
        }

    elif operacao == "listar":
        resposta = {
            "tarefas": tarefas
        }

    elif operacao == "remover":
        id_remover = dados["id"]

        tarefa_encontrada = False

        for tarefa in tarefas:
            if tarefa["id"] == id_remover:
                tarefas.remove(tarefa)
                tarefa_encontrada = True
                break

        if tarefa_encontrada:
            resposta = {
                "mensagem": "Tarefa removida"
            }
        else:
            resposta = {
                "mensagem": "Tarefa não encontrada"
            }

    else:
        resposta = {
            "mensagem": "Operação inválida"
        }

    socket.send(
        json.dumps(resposta).encode()
    )