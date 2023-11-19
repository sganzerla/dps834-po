from ortools.linear_solver import pywraplp

class Producao:
    def __init__(self):
        self.mdl = pywraplp.Solver.CreateSolver("GLOP")
        self.var()
        self.fo()
        self.const()
    
    def var(self): # declarando variáveis
        # declarando variaveis continuas que podem crescer de 0 até o infinito
        self.r_sed = self.mdl.NumVar(name=f'r_sed', lb=5_000, ub=26_000)
        self.r_suv = self.mdl.NumVar(name=f'r_suv', lb=100, ub=1_950)
        self.u_sed = self.mdl.NumVar(name=f'u_sed', lb=2_000, ub=26_000)
        self.u_suv = self.mdl.NumVar(name=f'u_suv', lb=200, ub=1_560)
        self.p_sed = self.mdl.NumVar(name=f'p_sed', lb=3_000, ub=20_800)
        self.p_suv = self.mdl.NumVar(name=f'p_suv', lb=500, ub=3_900)
        self.g_sed = self.mdl.NumVar(name=f'g_sed', lb=7_000, ub=20_800)
        self.g_suv = self.mdl.NumVar(name=f'g_suv', lb=1_000, ub=5_200)

    def fo(self): # declarando função objetivo
        self.mdl.Minimize(30 * self.r_sed + 65 * self.r_suv + 35 * self.u_sed + 60 * self.u_suv + 40 * self.p_sed + 55 * self.p_suv + 45 * self.g_sed + 50 * self.g_suv)
        
    
    def const(self): # declarando as restrições 
            # restrição mão de obra
            self.mdl.Add(4 * self.r_sed + 5 * self.r_suv +  3 * self.u_sed + 6 * self.u_suv + 2 * self.p_sed + 7 * self.p_suv + 3 * self.g_sed + 4 * self.g_suv <= 348_000)
            
            # restrição matéria-prima
            self.mdl.Add(3 * self.r_sed + 6 * self.r_suv +  2 * self.u_sed + 4 * self.u_suv + 4 * self.p_sed + 8 * self.p_suv + 5 * self.g_sed + 10 * self.g_suv <= 412_500)
            
            # restrição de demanda mínima de SUV
            self.mdl.Add(1 * self.r_suv + 1 * self.u_suv + 1 * self.p_suv + 1 * self.g_suv == 11_863)

            # restrição de demanda mínima de SUV
            self.mdl.Add(1 * self.r_sed + 1 * self.u_sed + 1 * self.p_sed + 1 * self.g_sed == 93_335)

    def solve(self):
            status = self.mdl.Solve()
            if status == pywraplp.Solver.OPTIMAL:
                print(f"FO              : {self.mdl.Objective().Value():.2f}")
                print(f'Recife   -   SED: {self.r_sed.solution_value():.2f}')
                print(f'Recife   -   SUV: {self.r_suv.solution_value():.2f}')
                print(f'Uberlândia - SED: {self.u_sed.solution_value():.2f}')
                print(f'Uberlância - SUV: {self.u_suv.solution_value():.2f}')
                print(f'Porto Real - SED: {self.p_sed.solution_value():.2f}')
                print(f'Porto Real - SUV: {self.p_suv.solution_value():.2f}')
                print(f'Gravataí  -  SED: {self.g_sed.solution_value():.2f}')
                print(f'Gravataí  -  SUV: {self.g_suv.solution_value():.2f}')
            else:
                print(f"Problema não resolvido: {status}")

if __name__ == "__main__":
    
    model = Producao()
    model.solve()