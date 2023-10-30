# dps-po

## Forma padrão

|||
|----------------------------------------------|--------------------------|
|$Max Z $|Função objetivo de maximizar (Max)|
|x1+x2 <= b|Restrições são de menor ou igual (<=)|
|b >= 0|Constantes (b) de todas as restrições são não negativas|
|x1,x1 >= 0|Variáveis não podem assumir valores negativos|

## Conversão de problemas que não estão na forma padrão

|Tipo|Ação|
|-------------------------------------------------|---------------------------------------------|
|Função objetivo de minimização (Min) | Mudar para maximização (Max) e inverter o sinal de Z|
|Restrição de menor ou igual (<=) | Acrescentar variável de folga|
|Restrição de maior ou igual (>=) | Acrescentar variável de folga e variável artificial |
|Restrição de igualdade (=) | Inserção de variável artificial|
|Constante (b) negativa | Multiplicação da restrição por -1|
