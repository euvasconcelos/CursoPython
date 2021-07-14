
def CalculaImc(peso, altura):
    imc = (peso/pow(altura,2))
    if (imc <18.5):
        print('\nIMC: {:.2f}\n ABAIXO DO PESO'.format(imc))
    
    elif (imc >18.5 and imc <=24.9):
        print('\nIMC: {:.2f}\n PESO NORMAL'.format(imc))

    elif (imc >24.9 and imc <=29.9):
        print('\nIMC: {:.2f}\n SOBREPESO'.format(imc))

    elif (imc >29.9 and imc <=34.9):
        print('\nIMC: {:.2f}\n OBESIDADE GRAU I'.format(imc))

    elif (imc >34.9 and imc <=39.9):
        print('\nIMC: {:.2f}\n OBESIDADE GRAU II'.format(imc))

    else:
        print('\nIMC: {:.2f}\n OBESIDADE GRAU III OU MÓRBIDA'.format(imc))

altura = float(input('ALTURA: '))
peso = float(input('PESO: '))

CalculaImc(peso,altura)


