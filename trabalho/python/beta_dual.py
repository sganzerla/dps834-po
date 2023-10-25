from ortools.linear_solver import pywraplp
# python -m pip install ortools

class BetaD:
    def __init__(self):
        
        
        # Criar o modelo linear
        self.mdl = pywraplp.Solver.CreateSolver("GLOP")
        self.var()
        self.fo()
        self.const()
            
       
    def var(self):
        # fabricar 1000 auto no total
        self.y1 = self.mdl.NumVar(name=f'y_1', lb=0, ub=self.mdl.infinity())
        # fabricar 400 em vitoria
        self.y2 = self.mdl.NumVar(name=f'y_2', lb=0, ub=self.mdl.infinity())
        # mao de obra
        self.y3 = self.mdl.NumVar(name=f'y_3', lb=0, ub=self.mdl.infinity())
        # materia prima
        self.y4 = self.mdl.NumVar(name=f'y_4', lb=0, ub=self.mdl.infinity())

    def fo(self):
            self.mdl.Maximize(1000 * self.y1 + 400 * self.y2 - 3300 * self.y3 - 4000 * self.y4)
        
        
    def const(self):
        
            self.mdl.Add(1 * self.y1 + 0 * self.y2 - 2 * self.y3 - 3 * self.y4 <= 15)
            
            self.mdl.Add(1 * self.y1 + 0 * self.y2 - 3 * self.y3 - 4 * self.y4 <= 10)
            
            self.mdl.Add(1 * self.y1 + 1 * self.y2 - 4 * self.y3 - 5 * self.y4 <= 9)
            
            self.mdl.Add(1 * self.y1 + 0 * self.y2 - 4 * self.y3 - 6 * self.y4 <= 7)
            

    def solve(self):
   
            status = self.mdl.Solve()
            
            if status == pywraplp.Solver.OPTIMAL:
                print(f"FO: {self.mdl.Objective().Value():.2f}")
                print(f'Cada carro produzido aumenta a FO em y_1 = R$ {self.y1.solution_value():.2f}')
                print(f'Cada carro produzido em Vitória aumenta a FO y_2 = {self.y2.solution_value():.2f}')
                print(f'O custo das horas da mão de obra para produzir cada carro custa y_3 = {self.y3.solution_value():.2f}')
                print(f'O custo da tonelada de matéria prima para produzir cada carro y_4 = {self.y4.solution_value():.2f}')
            else:
                print(f"Problema não resolvido: {status}")

if __name__ == "__main__":
    
    model = BetaD()

    model.solve()