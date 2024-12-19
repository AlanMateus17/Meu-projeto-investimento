import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go

class Acoes:
    def __init__(self, preco_por_acao, lucro_projetado_por_acao, valor_patrimonial_por_acao, numero_total_acoes,
                 dividas_liquidas, ebitda, lucro_operacional, depreciacao, amortizacao, divida_total,
                 caixa, equivalente_de_caixa, ativos_nao_operacionais, receita_liquida,
                 custos_totais, despesas_operacionais, impostos, lucro_bruto, lucro_liquido,
                 custos_diretos, capital_investido, patrimonio_liquido, nopat,  capital_nivel_1, capital_nivel_2, ativos_ponderados_risco, divida_bruta, nome):
        # Validação de entrada
        if preco_por_acao < 0 or lucro_projetado_por_acao < 0 or valor_patrimonial_por_acao < 0:
       
            raise ValueError("Preço por ação, lucro projetado por ação e valor patrimonial por ação devem ser não negativos.")
        self.nome = nome
        self.preco_por_acao = preco_por_acao
        self.lucro_projetado_por_acao = lucro_projetado_por_acao
        self.valor_patrimonial_por_acao = valor_patrimonial_por_acao
        self.numero_total_acoes = numero_total_acoes
        self.dividas_liquidas = dividas_liquidas
        self.ebitda = ebitda
        self.lucro_operacional = lucro_operacional
        self.depreciacao = depreciacao
        self.amortizacao = amortizacao
        self.divida_total = divida_total 
        self.caixa = caixa
        self.equivalente_de_caixa = equivalente_de_caixa
        self.ativos_nao_operacionais = ativos_nao_operacionais
        self.receita_liquida = receita_liquida
        self.custos_totais = custos_totais
        self.despesas_operacionais = despesas_operacionais
        self.impostos = impostos
        self.lucro_bruto = lucro_bruto
        self.lucro_liquido = lucro_liquido
        self.custos_diretos = custos_diretos
        self.capital_investido = capital_investido
        self.patrimonio_liquido = patrimonio_liquido
        self.nopat = nopat
        self.capital_nivel_2 = capital_nivel_2
        self.ativos_ponderados_risco = ativos_ponderados_risco
        self.divida_bruta = divida_bruta
        

    def calcular_P_L(self, preço_por_açao, lucro_projetado_por_açao):
        """Calcula o índice Preço/Lucro (P/L).

        Returns:
            float: O índice P/L calculado.

        Raises:
            ValueError: Se o lucro projetado por ação for menor ou igual a zero.
        """
        if self.lucro_projetado_por_acao <= 0:
            raise ValueError("Lucro projetado por ação deve ser maior que zero.")
        elif self.preco_por_acao <=0:
            raise ValuerError("Preço deve ser maior que zero.")
        return round(self.preco_por_acao / self.lucro_projetado_por_acao, 2)
    def avaliar_P_L(self,):
        """AVISA SE O P/L ESTA ALTO OU BAIXO."""
        pl = self.calcular_p_l()
        
        print(f"{self.nome}: P/L = {pl}")
        
        # Definindo os limites para avaliaçao.
        
        if pl > 20:
            print("Açao: O P/L esta alto. Pode ser um sinal de supervalorizaçao.")
            
            # Aqui foi adicionado a logica adicional, como alertar ou recomendar venda.
        
        elif pl < 15:
            print("Açao: O P/L esta baixo. Pode ser uma oportunidade de compra.")
            
            # Açao recomendada : considerar compra.
     
        else:
            print("Açao: O P/L esta na media. Monitoras a situaçao.")
            

# Função para coletar dados financeiros
def coletar_dados_acoes(tickers):
    acoes = []
    for ticker in tickers:
        # Coletando dados históricos
        try:
            dados = web.DataReader(ticker, data_source='yahoo', start='2022-01-01', end='2024-01-01')
            preco_atual = dados['Close'][-1]  # Último preço de fechamento
            lucro_projetado_por_acao = 5.00  # Substitua isso pela lógica de coleta do LPA real
            acoes.append(Acoes(ticker, preco_atual, lucro_projetado_por_acao))
        except Exception as e:
            print(f"Erro ao coletar dados para {ticker}: {e}")
    return acoes

# Função para comparar e classificar ações
def comparar_acoes(acoes):
    """Compara as ações e imprime seus P/Ls."""
    for acao in acoes:
        acao.avaliar_P_L()

# Lista de tickers das empresas que você deseja analisar
tickers = ['AAPL', 'MSFT', 'GOOGL']  # Exemplos: Apple, Microsoft, Google

# Coletando dados das ações
acoes_exemplo = coletar_dados_acoes(tickers)

# Comparando as ações coletadas
comparar_acoes(acoes_exemplo)        
        
        
# COMPARAR O RESULTADO COM OS DE OUTRAS EMPRESAS DO MESMO SETOR
##########################################################################
  
    def calcular_P_VP(self):
        """Calcula o índice Preço/Valor Patrimonial (P/VP)."""

        if self.valor_patrimonial_por_acao <= 0:
            raise ValueError("Valor patrimonial por ação deve ser maior que zero.")
        
        return round(self.preco_por_acao / self.valor_patrimonial_por_acao, 2)
    def avaliar_P_VP(self):
        """Avalia se o P/VP esta alto ou baixo"""
        p_vp = self.calcular_P_VP()
        
        print(F"{self.nome}: P/VP = {P/VP}")
        
        # Definindo os limites para avaliaçao.
        
        if p_vp > 20:
            print("Açao: OP/VP esta alto. Pode ser um sinal de supervalorizaçao.")
        elif p_vp < 1.5:
            print("Açao: 0 P/VP esta baixo. Pode ser uma oportunidade de compra.")
        else:
            print("Açao: O P/VP esta na media. Monitorar a situaçao.")

# FUNÇAO PARA COLETAR DADOS FINANCEIROS.

def coletar dados_financeiros():
    acoes = []
    for ticker in tickers:
        # Coletando dados historicos 
        
        try:
            dados = web.DataReader(ticker, 'yahoo', start='2022-01-01', end='2024-01-01')
            
            preco_atual = dados['Close'][-1]    # Ultimo preço de fechamento
            
            valor_patrimonial_por_acao = 30.00 # Substitua isso pela logica de coleta do VPA real.
            
            acoes.append(Acoes(ticker, preco_atual, valor_patrimonial_por_acao))
        except Exception as e:
            print(f"Erro ao coletar dados para {ticker}: {e}")
            
            return acoes
# Funcao para comparar e classificar açoes.
def comparar_acoes(acoes):
    """Compara as açoes e imprime seusP/VPs.""" 
    for acao in acoes:
        acao.avaliar_p_vp()
ticker = ['AAPL', 'MSFT', 'GOOGL']      # eXEMPLOS: Apple, Microsoft, Google. 
# Coletando dados das açoes
acoes_exemplo = coletar_dados_acoes(ticker)

# Comparando as açoes coletadas
comparar_acoes(acoes_exemplo)          
            

    def classificar_acao(self, fator_multiplicativo=1):Classifica a ação como crescimento futuro, desconto ou neutro.

        """ Args:
            fator_multiplicativo (float): Um fator multiplicativo para comparação.

        Returns:
            str: A classificação da ação.
        
        Raises:
            ValueError: Se o fator multiplicativo for menor ou igual a zero.
        """
        if fator_multiplicativo <= 0:
            raise ValueError("Fator multiplicativo deve ser maior que zero.")
        
        if self.preco_por_acao >= fator_multiplicativo * self.valor_patrimonial_por_acao:
            return "CRESCIMENTO FUTURO"
        elif self.preco_por_acao < (self.valor_patrimonial_por_acao / fator_multiplicativo):
            return "DESCONTO"
        else:
            return "NEUTRO"

    def calcular_valor_mercado(self):
        """Calcula o valor de mercado da empresa.

        Returns:
            float: O valor de mercado calculado.
        """
        return round(self.preco_por_acao * self.numero_total_acoes, 2)

    def calcular_enterprise_value(self):
        """Calcula o Enterprise Value (EV).

        Returns:
            float: O Enterprise Value calculado.
        """
        return round((self.calcular_valor_mercado() + 
                       self.divida_total - 
                       self.caixa - 
                       self.equivalente_de_caixa - 
                       self.ativos_nao_operacionais), 2)

    def calcular_valor_ebitda(self):
        """Calcula o valor EBITDA.

       Returns:
           float: O valor EBITDA calculado.
       """
       return round((self.lucro_operacional + 
                      self.depreciacao + 
                      self.amortizacao), 2)

    def calcular_ev_ebitda(self):
       """Calcula a relação EV/EBITDA.

       Returns:
           float: A relação EV/EBITDA calculada.

       Raises:
           ValueError: Se o EBITDA for menor ou igual a zero.
       """
       if self.ebitda <= 0:
           raise ValueError("EBITDA deve ser maior que zero para calcular EV/EBITDA.")
       
       return round(self.calcular_enterprise_value() / self.ebitda, 2)

    def calcular_lucro_liquido(self):
       """Calcula o lucro líquido.

       Returns:
           float: O lucro líquido calculado.
       """
       return round((self.receita_liquida - 
                      (self.custos_totais + 
                       self.despesas_operacionais + 
                       self.impostos)), 2)

    def calcular_cagr_investimento(self, valor_inicial, valor_final, anos):
       """Calcula a taxa de crescimento anual composta (CAGR) para investimento.

       Args:
           valor_inicial (float): O valor inicial do investimento.
           valor_final (float): O valor final do investimento.
           anos (int): O número de anos durante os quais o investimento foi mantido.

       Returns:
           float: A taxa de crescimento anual composta em porcentagem.

       Raises:
           ValueError: Se o valor inicial ou anos forem menores ou iguais a zero.
       """
       if valor_inicial <= 0 or anos <= 0:
           raise ValueError("Valor inicial e anos devem ser maiores que zero.")
       
       cagr = (valor_final / valor_inicial) ** (1 / anos) - 1
       return round(cagr * 100, 2)  # Retorna em porcentagem

    def calcular_taxa_de_crescimento_dos_lucros(self, lucro_atual, lucro_anterior):
       """Calcula a taxa de crescimento dos lucros.

       Args:
           lucro_atual (float): O lucro atual da empresa.
           lucro_anterior (float): O lucro do período anterior.

       Returns:
           float: A taxa de crescimento dos lucros em porcentagem.

       Raises:
           ValueError: Se o lucro anterior for igual a zero.
       """
       if lucro_anterior == 0:
           raise ValueError("Lucro anterior não pode ser zero.")
       
       return round(((lucro_atual - lucro_anterior) / lucro_anterior) * 100 ,2)

    def calcular_peg_ratio(self):
       """Calcula o PEG ratio.

       Returns:
           float: O PEG ratio calculado.

       Raises:
           ValueError: Se a taxa de crescimento dos lucros for igual a zero.
       """
       
       taxa_crescimento = float(input("Insira a taxa de crescimento dos lucros: "))
       
       if taxa_crescimento == 0:
           raise ValueError("A taxa de crescimento dos lucros não pode ser zero para calcular PEG ratio.")
       
       return round(self.calcular_P_L() / taxa_crescimento ,2)

    def classificar_peg_ratio(self, fator_multiplicativo=1):
       """Classifica o PEG ratio.

       Args:
           fator_multiplicativo (float): Um fator multiplicativo para comparação do PEG ratio.

       Returns:
           str: Uma classificação do PEG ratio baseado no fator multiplicativo fornecido.

       Raises:
           ValueError: Se o fator multiplicativo for menor ou igual a zero.
       """
       
       if fator_multiplicativo <= 0:
           raise ValueError("Fator multiplicativo deve ser maior que zero.")
       
       
       if peg_ratio >= fator_multiplicativo * (self.calcular_taxa_de_crescimento_dos_lucros()):
           return "PEG RATIO ALTO"
       elif peg_ratio < (self.calcular_taxa_de_crescimento_dos_lucros() / fator_multiplicativo):
           return "PEG RATIO BAIXO"
       else:
           return "PEG RATIO IDEAL"
    
    
    
                  # """CALCULANDO MARGENS OPERACIONAIS..."""
    def calcular_margem_bruta(self):
       """Calcular Margem Bruta.

      Returns:
          float: A margem bruta expressa em porcentagem.

      Raises:
          ValueError: Se a receita líquida for menor ou igual a zero.
      """
      if self.receita_liquida <= 0:
          raise ValueError("A receita líquida deve ser maior que zero.")
      
      return round((self.lucro_bruto / self.receita_liquida) * 100, 2)
    
    def calcular_margem_ebitda(self):
      """Calcular Margem EBITDA.

      Returns:
          float: A margem EBITDA expressa em porcentagem.

      Raises:
          ValueError: Se a receita líquida for menor ou igual a zero.
      """
      if self.receita_liquida <= 0:
          raise ValueError("A receita líquida deve ser maior que zero.")
      
      return round((self.ebitda / self.receita_liquida) * 100, 2)
    
    def calcular_margem_liquida(self):
      """Calcular Margem Líquida.

      Returns:
          float: A margem líquida expressa em porcentagem.

      Raises:
          ValueError: Se a receita líquida for menor ou igual a zero.
      """
      if self.receita_liquida <= 0:
          raise ValueError("A receita líquida deve ser maior que zero.")
      
      return round((self.lucro_liquido / self.receita_liquida) * 100, 2)
    
    
                # """INDICADORES FUNDAMENTALISTAS:ROE E ROIC..."""  
                
    def calcular_roe(self,lucro_liquido, patrimonio_liquido):
        if partimonio_liquido == 0:
            return None                  # Evitar divisao por zero.
        
        """CALCULAR ROE..."""
        """RETORNO SOBRE O PATRIMÔNIO LÍQUIDO DA EMPRESA (ROE) """
        return (self.lucro_liquido / self.patrimonio_liquido) * 100    # Retorna em porcentagem.
    def calcular_roic(self):
        if capital_investido ==0:
            return None                  # Evitar divisao por zero.
        """CALCULAR ROIC..."""
        """RETORNO SOBRE O CAPITAL INVESTIDO (ROIC)"""
        return (self.nopat / self.capital_investido) * 100     # Retorna em porcentagem.
    def avaliar_indicadores(roe, roic):
        # Avaliaçao do ROE.
        if roe is not Nnone:
            if roe > 20:
                print(f"ROE: {roe:.2f}%. EXCELENTE!")
            elif roe < 15:
                print(f"ROE: {roe:.2f}%. BOM!")
            elif roe < 10:
                print(f"ROE: {roe:.2f}%. INSATISFATORIO!")
            else:
                print(f"ROE: {roe:.2f}%. NA MEDIA.")
        else:
            print("ROE: NAO DISPONIVEL.")
            
        # Avaliaçao do ROIC.
        if roic is not None:
            if roic > 10:
                print(f"ROIC: {roic:.2f}%. EXCELENTE!")
            elif roic > 2:
                print(f"ROIC: {roic:.2f}%.BOM!")
            elif roic < 2:
                print(f"ROIC: {roic:.2f}%. INSATISFATORIO!")
            else:
                print(f"ROIC: {roic:.2f}%. NA MEDIA.")
        else:
            print("ROIC: NAO DISPONIVEL.")
        
        
                        
    def calcular_alavancagem(self):
      """Calcula a alavancagem da empresa em relação ao EBITDA.

      Returns:
          str: Uma descrição da situação financeira da empresa com base na alavancagem.

      Raises:
          ValueError: Se o EBITDA for menor ou igual a zero.
      """
      
      if self.ebitda <= 0:
          raise ValueError("EBITDA deve ser maior que zero para calcular alavancagem.")
      
      alavancagem = round((self.dividas_liquidas / self.ebitda), 2)
      
      if alavancagem < 1:
          return "EMPRESAS FINANCEIRAMENTE TRANQUILAS."
      elif alavancagem < 3:
          return "EMPRESAS ESTÁVEIS FINANCEIRAMENTE."
      else:
          return "EMPRESA COM SITUAÇÃO MAIS DELICADA."

    def calcular_alavancagem_2(self):
      """Calcula uma segunda medida de alavancagem da empresa em relação ao patrimônio líquido.

      Returns:
          str: Uma descrição do risco financeiro da empresa com base na alavancagem em relação ao patrimônio líquido.

      Raises:
          ValueError: Se o patrimônio líquido for menor ou igual a zero.
      """
      
      if self.patrimonio_liquido <= 0:
          raise ValueError("O patrimônio líquido deve ser maior que zero para calcular alavancagem.")
      
      alavancagem_2 = round((self.dividas_liquidas / self.patrimonio_liquido), 2)
      
      if alavancagem_2 < 0.5:
          return "EMPRESA DE BAIXO RISCO."
      elif alavancagem_2 <= 1:
          return "EMPRESA DE RISCO MODERADO."
      else:
          return "EMPRESA DE ALTA RISCO."

    def calcular_basileia(self):
       """Calcula a basileia da empresa.
       Returns:
           float: A basileia calculada.
       """
       if self.setor != "bancário":
            return None  # Retorna None se não for do setor bancário
        
       return round((self.dividas_liquidas / self.patrimonio_liquido), 2)
       
    def calcular_patrimonio_referencia(self):
        """
        Calcula o Patrimônio de Referência (PR).

        Returns:
            float: O patrimônio de referência total.
        """
        return self.capital_nivel_1 + self.capital_nivel_2

    def calcular_indice_basileia(self):
        """
        Calcula o Índice de Basileia.

        Returns:
            float: O Índice de Basileia em porcentagem.

        Raises:
            ValueError: Se os ativos ponderados pelo risco forem menores ou iguais a zero.
        """
        if self.ativos_ponderados_risco <= 0:
            raise ValueError("Os ativos ponderados pelo risco devem ser maiores que zero.")
        
        patrimonio_referencia = self.calcular_patrimonio_referencia()
        indice_basileia = (patrimonio_referencia / self.ativos_ponderados_risco) * 100
        return round(indice_basileia, 2)
    
''












