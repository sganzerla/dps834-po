from ortools.linear_solver import pywraplp
# python -m pip install ortools


# a) deve-se escolher a melhor combinação de títulos para investir 
# de modo que obtenha-se o máximo lucro possível.

class InvestProbl:
    def __init__(self):
       
       
        # dados
        self.investimentos = [i for i in range(1, 7)]
        self.risco = {1:1, 2:3, 3:4, 4:2, 5:4, 6:5}
        self.vencimento = {1:15, 2:12, 3:8, 4:7, 5:11, 6:5}
        self.retorno = {1:0.087, 2:0.095, 3:0.12, 4:0.09, 5:0.13, 6:0.2}
        
        # Criar o modelo linear
        self.mdl = pywraplp.Solver.CreateSolver("GLOP")
        
        # variaveis
        self.criando_variaveis()

        # restricoes
        self.criando_restricoes()
        
        # funcao objetivo
        self.criando_funcao_objetivo()

        # resolver e apresentar solução
        self.resolver_problema()

    def resolver_problema(self):
        status = self.mdl.Solve()
        
        if status == pywraplp.Solver.OPTIMAL:
            print(f"O lucro máximo é: {self.mdl.Objective().Value():.2f}")
            for i in self.investimentos:
                # if x[i].solution_value() > 0:
                    print(f"Investimento {i}, de risco {self.risco[i]}, com retorno de {(self.retorno[i] * 100):.2f}% em {self.vencimento[i]} anos. Investir {(self.x[i].solution_value() * 100):.2f}%.")
        else:
            print(f"Problema não resolvido: {status}")
            
            
    def criando_funcao_objetivo(self):
        # d) cada variavel x tem o seu respectivo coeficiente de retorno contribuindo para o peso da funcao objetivo
        self.mdl.Maximize(self.mdl.Sum([self.x[i] * self.retorno[i] for i in self.investimentos]))


    def criando_restricoes(self):

        # restrição  1
        # nenhum título deve possuir mais de 25% do total investido
        for i in self.investimentos:
            self.mdl.Add(self.x[i] <= 0.25)

        # restrição  2
        # 50% do total investido deve ser aplicado no título 1, 2 e 6
        self.mdl.Add(self.mdl.Sum(self.x[i] for i in self.investimentos if self.vencimento[i] > 10) >= 0.51)
        
        
        # restrição  3
        # Os títulos 3, 5  e 6 não devem representar mais de 50% do valor investido.
        self.mdl.Add(self.mdl.Sum(self.x[i] for i in self.investimentos if self.risco[i] >= 4) <= 0.50)

        # restrição 4
        # soma de todos os investimentos deve ser 100%
        self.mdl.Add(self.mdl.Sum(self.x[i] for i in self.investimentos) <= 1)
        


    def criando_variaveis(self):
        # c) x vai representar o percentual que deve ser investido em cada investimento
        self.x = {i: self.mdl.NumVar(name=f'x_{i}', lb=0, ub=self.mdl.infinity()) for i in self.investimentos}

if __name__ == "__main__":
    
    model = InvestProbl()
    
    # O lucro máximo é: 0.13
    # Investimento 1, de risco 1, com retorno de 8.70% em 15 anos. Investir 1.00%.
    # Investimento 2, de risco 3, com retorno de 9.50% em 12 anos. Investir 25.00%.
    # Investimento 3, de risco 4, com retorno de 12.00% em 8 anos. Investir 0.00%.
    # Investimento 4, de risco 2, com retorno de 9.00% em 7 anos. Investir 24.00%.
    # Investimento 5, de risco 4, com retorno de 13.00% em 11 anos. Investir 25.00%.
    # Investimento 6, de risco 5, com retorno de 20.00% em 5 anos. Investir 25.00%.