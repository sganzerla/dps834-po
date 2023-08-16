from ortools.linear_solver import pywraplp
class ReplanoProbl:
    def __init__(self):
        # Criar o modelo linear
        mdl = pywraplp.Solver.CreateSolver("GLOP")
        
        # dados
        fontes = ['Ara', 'Ven']
        produtos = ['gaso', 'quer', 'lubr']
        barril_Ara = {'gaso': 0.3, 'quer': 0.4, 'lubr': 0.2}
        barril_Ven = {'gaso': 0.4, 'quer': 0.2, 'lubr': 0.3}

        disponibilidade = {'Ara': 9000, 'Ven': 6000}
        producao_minima = {'gaso': 2000, 'quer': 1500, 'lubr': 500}
        custo = {'Ara': 20, 'Ven': 15}
        
        # variáveis
        x = {(i, j): mdl.NumVar(name=f'x_{i}_{j}', lb=0, ub=mdl.infinity()) for i in fontes for j in produtos}

        # objetivo
        mdl.Minimize(
            mdl.Sum([x['Ara', j] * barril_Ara[j] * custo['Ara'] for j in produtos]) +
            mdl.Sum([x['Ven', j] * barril_Ven[j] * custo['Ven'] for j in produtos])
  )

        # restrição  1
        for i in fontes:
            mdl.Add(mdl.Sum(x[i, j]  for j in produtos) <= disponibilidade[i])
  
        # restrição  2
        for j in produtos:
            mdl.Add(mdl.Sum(x[i, j]  for i in fontes ) >= producao_minima[j])
  
        status = mdl.Solve()
        
        if status == pywraplp.Solver.OPTIMAL:
            print(f"O custo mínimo é: {mdl.Objective().Value():.2f}")
            for i in fontes:
                for j in produtos:
                    # if x[i].solution_value() > 0:
                    print(f"Fonte {i}, produto {j} : {x[i,j].solution_value():.2f} barril.")

if __name__ == "__main__":
    
    model = ReplanoProbl()
 