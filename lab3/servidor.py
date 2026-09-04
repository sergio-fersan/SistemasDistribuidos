import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

tarefas = []
cont = 0

while True:
    message = socket.recv()
    dados = json.loads(message.decode())

    operacao = dados["operacao"]

    print("Mensagem recebida: {dados}", flush=True)
    if operacao == "adicionar":
        cont++
        tarefa = {
            "id" : cont
            "titulo" : dados["titulo"]
        }

        tarefas.append(tarefa)

        resposta = {
            "mensagem" : "Tarefa adicionada!"
            "tarefa" : tarefa
        }