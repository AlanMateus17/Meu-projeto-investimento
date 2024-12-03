class Açoes:
    def __init__(self, rentabilidade, individamento, valorempresa, crescimento ):
        self.rentabilidade = rentabilidade
        self.individamento = individamento
        self.valorempresa = valorempresa
        def calcular_rentabilidade(lucro_liquido, investimento_total):
            if investimento_total == 0:
                return 0
            return (lucro_liquido / investimento_total) * 100
        def calcular_endividamento(divida_total, ativo_total):
            if ativo_total == 0:
                return 0
            return (divida_total / ativo_total) * 100
        def calcular_valor_mercado(preço_açao, numero_açoes):
            return preço_açao * numero_açoes
        def calcular_carg(valor_inicial, valor_final, anos):
            if anos <= 0:
                return 0
            return (valor_final / valor_inicial )** (1/anos) - 1 
        # Exemplo de uso das funções com dados fictícios
ticker = 'PETR3'
dados_empresa = obter_dados_empresa(ticker)

# Supondo que os dados retornem as seguintes informações:
lucro_liquido = dados_empresa['lucro_liquido']
investimento_total = dados_empresa['investimento_total']
divida_total = dados_empresa['divida_total']
ativo_total = dados_empresa['ativo_total']
preco_acao = dados_empresa['preco_acao']
numero_acoes = dados_empresa['numero_acoes']
valor_inicial = dados_empresa['valor_inicial']
valor_final = dados_empresa['valor_final']
anos = dados_empresa['anos']

# Realizando os cálculos
rentabilidade = calcular_rentabilidade(lucro_liquido, investimento_total)
endividamento = calcular_endividamento(divida_total, ativo_total)
valor_mercado = calcular_valor_mercado(preco_acao, numero_acoes)
cagr = calcular_cagr(valor_inicial, valor_final, anos)

# Exibindo os resultados
print(f"Rentabilidade: {rentabilidade:.2f}%")
print(f"Endividamento: {endividamento:.2f}%")
print(f"Valor de Mercado: R${valor_mercado:.2f}")
print(f"CAGR: {cagr:.2f}%")
        