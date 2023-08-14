from ortools.linear_solver import pywraplp
class InvestProbl2:
    def __init__(self):
        # Criar o modelo linear
        mdl = pywraplp.Solver.CreateSolver("GLOP")
        
        # dados
        emprestimos = [i for i in range(1, 6)]
        tipo = {1:"pessoal", 2:"automóvel", 3:"habitação", 4:"agrícola", 5:"comercial"}
        juros = {1:0.140, 2:0.130, 3:0.120, 4:0.125, 5:0.100}
        inadimplencia = {1:0.10, 2:0.07, 3:0.03, 4:0.05, 5:0.02}
        
        # variáveis
        x = {i: mdl.NumVar(name=f'x_{i}', lb=0, ub=mdl.infinity()) for i in emprestimos}

        # objetivo
        mdl.Maximize(mdl.Sum([x[i] * juros[i] for i in emprestimos]))

        # restrição  1
        mdl.Add(mdl.Sum(x[i] for i in emprestimos) <= 12)
        
        # restrição  2
        mdl.Add(mdl.Sum(x[i] for i in emprestimos if i >= 4) >= 4)
        
  
        # restrição  3
        mdl.Add(mdl.Sum(x[i] * inadimplencia[i] for i in emprestimos) <= 0.48 )

        status = mdl.Solve()
        
        if status == pywraplp.Solver.OPTIMAL:
            print(f"O lucro máximo é: {mdl.Objective().Value():.2f}")
            for i in emprestimos:
                # if x[i].solution_value() > 0:
                    print(f"Empréstimo {tipo[i]} com juros de {(juros[i]* 100):.2f}% com inadimplência de {(inadimplencia[i] * 100):.2f}%, investir R$ {x[i].solution_value():.2f} milhões.")

if __name__ == "__main__":
    
    model = InvestProbl2()
 