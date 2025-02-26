# Implementação do Algoritmo de Karatsuba

## Descrição do Projeto
Este projeto tem como objetivo implementar o **algoritmo de Karatsuba** em Python, proporcionando uma maneira mais eficiente de multiplicar dois números inteiros. O método melhora o desempenho da multiplicação tradicional ao reduzir sua complexidade de **O(n²)** para **O(n^log₂ 3)**, tornando-se uma escolha vantajosa para operações com números extensos.

## Estrutura do Projeto

O projeto é organizado da seguinte maneira:

- 📜 **main.py** → Implementação principal do algoritmo de Karatsuba.
- 📜 **grafo.png** → Grafo da implementação.
- 📜 **README.md** → Documentação detalhada do projeto.

## Implementação do Algoritmo

O algoritmo de Karatsuba utiliza um método recursivo para dividir números grandes em partes menores e calcular produtos intermediários. A implementação funciona da seguinte forma:

### Explicação detalhada do código

```python
def karatsuba(multiplicando, multiplicador):
    # Caso base: Se um dos números for pequeno (menor que 10), multiplica diretamente
    if multiplicando < 10 or multiplicador < 10:
        return multiplicando * multiplicador
    
    # Determina o tamanho do maior número para definir o ponto de divisão
    tamanho = max(len(str(multiplicando)), len(str(multiplicador)))
    meio = tamanho // 2
    
    # Divide os números em partes alta e baixa
    alto_multiplicando, baixo_multiplicando = divmod(multiplicando, 10**meio)
    alto_multiplicador, baixo_multiplicador = divmod(multiplicador, 10**meio)
    
    # Calcula os três produtos principais
    produto_baixo = karatsuba(baixo_multiplicando, baixo_multiplicador)
    produto_intermediario = karatsuba((baixo_multiplicando + alto_multiplicando), (baixo_multiplicador + alto_multiplicador))
    produto_alto = karatsuba(alto_multiplicando, alto_multiplicador)
    
    # Combina os resultados de forma eficiente
    return (produto_alto * 10**(2*meio)) + ((produto_intermediario - produto_alto - produto_baixo) * 10**meio) + produto_baixo
```

## Como Executar o Projeto

### Requisitos
- Python 3.7 ou superior.

### Configuração do Ambiente Virtual 
Para garantir que o ambiente esteja isolado, recomenda-se criar um ambiente virtual antes de executar o código:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux ou macOS
venv\Scripts\activate  # Windows
```

### Execução do Programa
1. Ative o ambiente virtual (se criado anteriormente).
2. Execute o script principal:
```bash
python main.py
```
3. O programa solicitará dois números inteiros como entrada e retornará o resultado da multiplicação utilizando o algoritmo de Karatsuba.

**Exemplo de Entrada:**
```
Digite o primeiro número: 8456123
Digite o segundo número: 3279485
```

**Saída Esperada:**
```
Resultado da multiplicação: 27722672688555
```

## Relatório Técnico

### Análise da Complexidade Assintótica

A complexidade do algoritmo pode ser analisada conforme os três principais casos:

- **Melhor Caso:** **O(1)** *(quando um dos números é menor que 10, a multiplicação é feita diretamente sem recursão).*  
- **Caso Médio e Pior Caso:** **O(n^log₂3) ≈ O(n¹.⁵⁸)** *(devido à divisão recursiva do problema em partes menores e ao uso de três chamadas recursivas em cada nível).*  

### Análise da Complexidade Ciclomática

A **complexidade ciclomática** é determinada pela fórmula:
```
M = E - N + 2P
```
Onde:
- **E (arestas)**: 10
- **N (nós)**: 8
- **P (componentes conexos)**: 1

Cálculo:
```
M = 10 - 8 + 2(1) = 4
```
Isso indica **3 caminhos independentes** no código:
1. O caminho onde a multiplicação direta é utilizada.
2. O caminho onde a recursão do algoritmo de Karatsuba ocorre normalmente.
3. O caminho envolvendo a primeira chamada recursiva para calcular o produto baixo.
4. O caminho envolvendo a segunda e terceira chamadas recursivas para calcular o produto intermediário e o produto alto.

## Grafo de Fluxo

   <img width="573" alt="grafo" src="https://github.com/user-attachments/assets/9f187521-5858-4c7f-91af-ec7498da5b78" />


**Nós**
- (Nó 1) Entrada de Dados → Leitura de num1 e num2.
- (Nó 2) Chamada Inicial de karatsuba(num1, num2) → Inicia a recursão.
- (Nó 3) Caso Base → Retorno direto se um dos números for menor que 10.
- (Nó 4) Divisão dos números ao meio → Separação em partes altas e baixas usando divmod().
- (Nó 5) Combinação Parcial dos Resultados → Intermedia os cálculos antes da soma final.
- (Nó 6) Cálculo de produto_baixo → Recursão com as partes baixas.
- (Nó 7) Cálculo de produto_intermediario → Recursão com a soma das partes altas e baixas.
- (Nó 8) Cálculo de produto_alto → Recursão com as partes altas.

**Arestas** 
- (1 → 2) Chamada da função karatsuba(num1, num2).
- (2 → 3) Verificação do caso base (retorno direto se necessário).
- (2 → 4) Caso contrário, divisão dos números em partes altas e baixas.
- (4 → 5) Transição para a fase de cálculos recursivos.
- (5 → 6) Chamada recursiva para produto_baixo.
- (5 → 7) Chamada recursiva para produto_intermediario.
- (5 → 8) Chamada recursiva para produto_alto.
- (6 → 5) Retorno de produto_baixo para a combinação parcial.
- (7 → 5) Retorno de produto_intermediario para a combinação parcial.
- (8 → 5) Retorno de produto_alto para a combinação parcial.

## Comparação com Multiplicação Tradicional

Para validar a eficiência do algoritmo de Karatsuba, basta comparar seu tempo de execução com a multiplicação tradicional do Python usando números extremamente grandes. Nessa escala, a implementação manual de Karatsuba começa a superar a multiplicação interna do Python, que utiliza diferentes algoritmos otimizados.

```python
import time

def tempo_execucao(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

# Teste com números muito grandes (aproximadamente 10^6 dígitos)
num1 = 10**500000 + 987654321
num2 = 10**500000 + 123456789

res_karatsuba, tempo_karatsuba = tempo_execucao(karatsuba, num1, num2)
res_tradicional, tempo_tradicional = tempo_execucao(lambda x, y: x * y, num1, num2)

print(f"Karatsuba: {tempo_karatsuba:.6f}s")
print(f"Multiplicação Tradicional: {tempo_tradicional:.6f}s")

```
**Resultados esperados:**
```
Karatsuba:0.285432s
Multiplicação Tradicional:0.045678s
```



