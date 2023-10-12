print('''Choice your number
[1]alugar um imovel 
[2] comprar um imovel
[3] falar com corretor
[4] elif option == 3:
          print(' falar com corretor')
            ''')

option = int(input('Your option: '))
while option != 1 or 4:
      option = int(input('Your option: '))
      if option == 1:
          print('setor aluguel entrara em contato ')
      elif option == 2:
        print('setor venda entrara em contato')
      elif option == 3:
        print(' corretor entrara em contato')
      else option == 4:
         print('setor judiciario entrara em contato')
      

