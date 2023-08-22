from ortools.linear_solver import pywraplp
# python -m pip install ortools


# a) definir a quantidade de dinheiro a liberar em uma das 5 modalidades
# de crédito disponíveis de modo a maximar os lucros.

class InvestProbl2:
    def __init__(self):
        # Criar o modelo linear
        self.mdl = pywraplp.Solver.CreateSolver("GLOP")
        
        # dados
        self.emprestimos = [i for i in range(1, 6)]
        self.tipo = {1:"pessoal", 2:"automóvel", 3:"habitação", 4:"agrícola", 5:"comercial"}
        self.juros = {1:0.140, 2:0.130, 3:0.120, 4:0.125, 5:0.100}
        self.inadimplencia = {1:0.10, 2:0.07, 3:0.03, 4:0.05, 5:0.02}
        
          # variaveis
        self.criando_variaveis()

        # restricoes
        self.criando_restricoes()
        
        # funcao objetivo
        self.criando_funcao_objetivo()

        # resolver e apresentar solução
        self.resolver_problema()
        

    def criando_restricoes(self):
        
        # restrição 1
        #  soma do valor em todas as modalidades deve ser menor ou igual a 12;
        self.mdl.Add(self.mdl.Sum(self.x[i] for i in self.emprestimos) <= 12)
        
        # restrição 2
        # a soma de valores nas modalidades agrícola e comercial deve ser mais de 40 * dos emprestimos
        self.mdl.Add(self.mdl.Sum(self.x[i] for i in self.emprestimos if i >= 4) >= 12 * 0.4)
  
        # restrição 3
        # quantia destinada ao crédito habitacional deve ser igual
        # a no mínimo 50% do total de empréstimos pessoais, para compra
        # de automóveis e habitacionais
        self.mdl.Add(self.x[3] >=  0.5 * self.mdl.Sum(self.x[i] for i in self.emprestimos if i in [1,2,3]))
  
  
        # restrição 4
        # a soma dos créditos nas modalidades deve ter taxa de inadimplência menor que 4.8
        self.mdl.Add(self.mdl.Sum(self.x[i] * self.inadimplencia[i] for i in self.emprestimos) <= 12 * 0.04 )

        
    def resolver_problema(self):

        status = self.mdl.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            print(f"O lucro máximo é: {self.mdl.Objective().Value():.2f}")
            for i in self.emprestimos:
                print(f"Empréstimo {self.tipo[i]} com juros de {(self.juros[i]* 100):.2f}% com inadimplência de {(self.inadimplencia[i] * 100):.2f}%, liberar crédito R$ {self.x[i].solution_value():.2f} milhões.")
        else:
            print(f"Problema não resolvido: {status}")

    def criando_funcao_objetivo(self):
        
        # soma do valor creditado em cada modalidade considerando a sua taxa de juros e a taxa de inadimplencia
        self.mdl.Maximize(self.mdl.Sum([self.x[i] * self.juros[i] * (1-self.inadimplencia[i]) for i in self.emprestimos]))

    def criando_variaveis(self):
        self.x = {i: self.mdl.NumVar(name=f'x_{i}', lb=0, ub=self.mdl.infinity()) for i in self.emprestimos}

if __name__ == "__main__":
    
    model = InvestProbl2()
 