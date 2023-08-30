from ortools.linear_solver import pywraplp
# python -m pip install ortools

class Probl:
    def __init__(self):
       
        # Criar o modelo linear
        self.mdl = pywraplp.Solver.CreateSolver("GLOP")
        
        
        self.x1 = self.mdl.NumVar(name=f'x_1', lb=0, ub=self.mdl.infinity())
        self.x2 = self.mdl.NumVar(name=f'x_2', lb=0, ub=self.mdl.infinity())
        self.x3 = self.mdl.NumVar(name=f'x_3', lb=0, ub=self.mdl.infinity())
        self.x4 = self.mdl.NumVar(name=f'x_4', lb=0, ub=self.mdl.infinity())
        self.x5 = self.mdl.NumVar(name=f'x_5', lb=0, ub=self.mdl.infinity())

        
        self.mdl.Maximize(4 * self.x1 + 8 * self.x2)
        
        self.mdl.Add(3 * self.x1 + 2 * self.x2 + 1 * self.x3 == 18)
        self.mdl.Add(1 * self.x1 + 2 * self.x2 + 1 * self.x4 == 5)
        self.mdl.Add(1 * self.x1 + 1 * self.x5 == 4)

   
        status = self.mdl.Solve()
        
        if status == pywraplp.Solver.OPTIMAL:
            print(f"FO: {self.mdl.Objective().Value():.2f}")
            print(f'x_1 = {self.x1.solution_value()}')
            print(f'x_2 = {self.x2.solution_value()}')
            print(f'x_3 = {self.x3.solution_value()}')
            print(f'x_4 = {self.x4.solution_value()}')
            print(f'x_5 = {self.x5.solution_value()}')

        else:
            print(f"Problema não resolvido: {status}")

if __name__ == "__main__":
    
    model = Probl()
