def quadrado(numero):
    return numero ** 2

def cubo(numero):
    return numero ** 3

if __name__ == "__main__":
    num = int(input("Digite um número: "))
    print(f"O quadrado de {num} é {quadrado(num)}")
    print(f"O cubo de {num} é {cubo(num)}")