def karatsuba(multiplicando, multiplicador):
    if multiplicando < 10 or multiplicador < 10:
        return multiplicando * multiplicador
    
    tamanho = max(len(str(multiplicando)), len(str(multiplicador)))
    meio = tamanho // 2
    
    alto_multiplicando, baixo_multiplicando = divmod(multiplicando, 10**meio)
    alto_multiplicador, baixo_multiplicador = divmod(multiplicador, 10**meio)
    
    produto_baixo = karatsuba(baixo_multiplicando, baixo_multiplicador)
    produto_intermediario = karatsuba((baixo_multiplicando + alto_multiplicando), (baixo_multiplicador + alto_multiplicador))
    produto_alto = karatsuba(alto_multiplicando, alto_multiplicador)
    
    return (produto_alto * 10**(2*meio)) + ((produto_intermediario - produto_alto - produto_baixo) * 10**meio) + produto_baixo

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = karatsuba(num1, num2)
    print(f"O resultado da multiplicação é: {resultado}")
