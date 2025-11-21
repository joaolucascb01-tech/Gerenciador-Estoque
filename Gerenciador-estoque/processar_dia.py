import pickle

def carregar_estoque():
    with open('estoque_inicial.pkl', 'rb') as arq:
        return pickle.load(arq)

def salvar_estoque(estoque):
    with open('estoque_final.pkl', 'wb') as arq:
        pickle.dump(estoque, arq)

def processar_transacoes(estoque):
    with open('transacoes.txt', 'r') as transacoes, open('log_de_erros.txt', 'w') as log:
        for linha in transacoes:
            linha = linha.strip()
            try:
                tipo, produto, qtd = linha.split(',')
                qtd = int(qtd)
            except ValueError:
                log.write(f"ERRO: Linha inválida: {linha}\n")
                continue

            if tipo == "ENTRADA":
                estoque[produto] = estoque.get(produto, 0) + qtd
            elif tipo == "SAIDA":
                if produto not in estoque:
                    log.write(f"ERRO: Tentativa de venda de '{produto}', produto não cadastrado.\n")
                elif estoque[produto] >= qtd:
                    estoque[produto] -= qtd
                else:
                    log.write(f"ERRO: Venda de '{produto}' falhou. Estoque: {estoque[produto]}, Pedido: {qtd}.\n")

def main():
    estoque = carregar_estoque()
    processar_transacoes(estoque)
    salvar_estoque(estoque)
    print("✅ Processamento concluído.")

if __name__ == "__main__":
    main()