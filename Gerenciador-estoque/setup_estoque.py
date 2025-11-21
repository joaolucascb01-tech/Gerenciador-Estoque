
estoque_inicial = {
    'banana': 50,
    'maca': 100,
    'laranja': 75,
    'uva': 30
}

with open('estoque_inicial.pkl', 'wb') as arq:
    pickle.dump(estoque_inicial, arq)

print("Arquivo 'estoque_inicial.pkl' criado com sucesso!")

