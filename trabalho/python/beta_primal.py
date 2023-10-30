from ortools.linear_solver import pywraplp
# python -m pip install ortools

class BetaP:
    def __init__(self):
        
        
        
        # Criar o modelo linear
        self.mdl = pywraplp.Solver.CreateSolver("GLOP")
        self.var()
        self.fo()
        self.const()
            
       
    def var(self):
        # Rio de Janeiro
        self.x1 = self.mdl.NumVar(name=f'x_1', lb=0, ub=self.mdl.infinity())
        # São Paulo
        self.x2 = self.mdl.NumVar(name=f'x_2', lb=0, ub=self.mdl.infinity())
        # Vitória
        self.x3 = self.mdl.NumVar(name=f'x_3', lb=0, ub=self.mdl.infinity())
        # Uberaba
        self.x4 = self.mdl.NumVar(name=f'x_4', lb=0, ub=self.mdl.infinity())

    def fo(self):
            self.mdl.Minimize(15 * self.x1 + 10 * self.x2 + 9 * self.x3 + 7 * self.x4)
        
        
        # 15 +10 + 9 + 7
        #  1 + 1 + 1 + 1 == 1000
        #  0 + 0 + 1 + 0 >= 400
        #  2 + 3 + 4 + 4 <= 3300
        #  3 + 4 + 5 + 6 <= 4000
        
    def const(self):
        
            # deve construir 1000 automoveis
            self.mdl.Add(1 * self.x1 + 1 * self.x2 + 1 * self.x3 + 1 * self.x4 == 1000)

            # fabrica de vitoria 400 carros
            self.mdl.Add(0 * self.x1 + 0 * self.x2 + 1 * self.x3 + 0 * self.x4 >= 400)
            
            # mao de obra disponivel
            self.mdl.Add(2 * self.x1 + 3 * self.x2 + 4 * self.x3 + 5 * self.x4 <= 3300)

            # materia prima
            self.mdl.Add(3 * self.x1 + 4 * self.x2 + 5 * self.x3 + 6 * self.x4 <= 4000)            

    def solve(self):
   
            status = self.mdl.Solve()
            
            if status == pywraplp.Solver.OPTIMAL:
                print(f"FO: {self.mdl.Objective().Value():.2f}")
                print(f'Produção de carros na fábrica x_1 = {self.x1.solution_value():.2f}')
                print(f'Produção de carros na fábrica x_2 = {self.x2.solution_value():.2f}')
                print(f'Produção de carros na fábrica x_3 = {self.x3.solution_value():.2f}')
                print(f'Produção de carros na fábrica x_4 = {self.x4.solution_value():.2f}')
            else:
                print(f"Problema não resolvido: {status}")

if __name__ == "__main__":
    
    model = BetaP()

    model.solve()