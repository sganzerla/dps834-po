from ortools.linear_solver import pywraplp
class InvestProbl:
    def __init__(self):
        # Criar o modelo linear
        mdl = pywraplp.Solver.CreateSolver("GLOP")
        
        # dados
        investimentos = [i for i in range(1, 7)]
        risco = {1:1, 2:3, 3:4, 4:2, 5:4, 6:5}
        vencimento = {1:15, 2:12, 3:8, 4:7, 5:11, 6:5}
        retorno = {1:0.087, 2:0.095, 3:0.12, 4:0.09, 5:0.13, 6:0.2}
        
        # variáveis
        x = {i: mdl.NumVar(name=f'x_{i}', lb=0, ub=mdl.infinity()) for i in investimentos}

        # objetivo
        mdl.Maximize(mdl.Sum([x[i] * retorno[i] for i in investimentos]))

        # restrição  1
        for i in investimentos:
            mdl.Add(x[i] <= 0.25)
        
        # restrição  2
        mdl.Add(mdl.Sum(x[i] for i in investimentos if vencimento[i] > 10) >= 0.51 )
  
        # restrição  3
        mdl.Add(mdl.Sum(x[i] for i in investimentos if risco[i] >= 4) <= 0.50 )

        status = mdl.Solve()
        
        if status == pywraplp.Solver.OPTIMAL:
            print("O lucro máximo é:", mdl.Objective().Value())
            for i in investimentos:
                # if x[i].solution_value() > 0:
                    print("Investimento", i, " de risco", risco[i], "com retorno de", (retorno[i] * 100), "% em", vencimento[i], "anos, investir", (x[i].solution_value() * 100), "%.")

if __name__ == "__main__":
    
    model = InvestProbl()
 