from queue import Queue

def reorganize(pilha):
    tamanho = len(pilha)
    metade = tamanho // 2

    fila1 = Queue()
    fila2 = Queue()

    for i in range(metade):
        fila1.put(pilha[i])

    for i in range(metade, tamanho):
        fila2.put(pilha[i])

    while not fila1.empty() or not fila2.empty():
        if not fila1.empty():
            print(fila1.get(), end=' ')
        if not fila2.empty():
            print(fila2.get(), end=' ')

pilha = [1, 5, 9, 24, 56, 16, 53, 105]
reorganize(pilha)