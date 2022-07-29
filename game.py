from models.calcular import Calcular


def main():
    print('Math Game')
    print('Escolha uma dificuldade: \n1 - Fácil \n2 - Médio \n3 - Difícil \n4 - Muito Difícil')
    print('Em caso de divisão colocar apenas as duas primeiras casas flutantes arredondando para cima. Bom Jogo!\n')
    pontos = 0
    jogar(pontos)


def jogar(pontos):
    dificuldade = int(
        input('Informe o nível de dificuldade desejado [1,2,3,4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado = float(input())

    if calc.chegar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar = int(input('Deseja continuar no jogo? [1 - Sim, 0  - Não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} ponto(s). Até uma próxima')


if __name__ == '__main__':
    main()
