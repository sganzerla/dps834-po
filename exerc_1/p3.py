from ortools.linear_solver import pywraplp
class TintasProbl:
    def __init__(self):
        # Criar o modelo linear
        mdl = pywraplp.Solver.CreateSolver("GLOP")
        
        # dados
        mat_prima = ['M1', 'M2']
        tintas = ['Ext', 'Int']
        exterior = {'M1': 0.16666666666, 'M2': 1.0}
        interior = {'M1': 0.25, 'M2': 0.5}
        disponibilidade = {'M1': 24, 'M2': 6}
        lucro = {'Ext': 5, 'Int': 4}
        
        # variáveis
        x = {(i, j): mdl.NumVar(name=f'x_{i}_{j}', lb=0, ub=mdl.infinity()) for i in mat_prima for j in tintas}

        # objetivo
        mdl.Maximize(
            mdl.Sum([x[i, 'Ext'] * lucro['Ext'] * exterior[i] for i in mat_prima]) +
            mdl.Sum([x[i, 'Int'] * lucro['Int'] * interior [i] for i in mat_prima])
            )

        # restrição  1
        mdl.Add(mdl.Sum(x[i, 'Ext']  for i in mat_prima) + 1 <= mdl.Sum(x[i, 'Int'] for i in mat_prima))
        
        # restrição  2
        mdl.Add(mdl.Sum(x[i, 'Int']  for i in mat_prima ) <= 2)
        
  
        # restrição  3
        for i in mat_prima:
            mdl.Add(mdl.Sum(x[i, j] for j in tintas) <= disponibilidade[i])

        status = mdl.Solve()
        
        if status == pywraplp.Solver.OPTIMAL:
            print(f"O lucro máximo é: {mdl.Objective().Value():.2f}")
            for i in mat_prima:
                for j in tintas:
                # if x[i].solution_value() > 0:
                    print(f"Matéria {i} para tinta {j} : {x[i,j].solution_value():.2f}t.")

if __name__ == "__main__":
    
    model = TintasProbl()
 