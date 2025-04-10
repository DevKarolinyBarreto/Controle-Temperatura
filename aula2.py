class ControleTemperatura:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
 
    @property    
    def temperatura(self):
        return self.__temperatura
   
    @temperatura.setter
    def temperatura(self, temperatura):
        if -50 < temperatura <= 100:
            print(f'A temperatura que você inseriu é: {temperatura}')
            self.__temperatura = temperatura
        else:
            print('Temperatura inválida. Insira uma temperatura entre -50 C e 100 C.')
 
    def ex(self):
        print(f'A temperatura atual é de {self.temperatura}°C')
 
    def converter_para_fahrenheit(self):
        fahrenheit = (self.__temperatura * 9/5) + 32
        return fahrenheit
   
controle = ControleTemperatura(25)
 
while True:
    try:
        nova_temperatura = float(input('Insira uma temperatura entre -50 C e 100 C: '))
        if -50 < nova_temperatura <= 100:
            controle.temperatura = nova_temperatura
            break
        else:
            print('Temperatura inválida. Insira uma temperatura entre -50 C e 100 C.')
    except ValueError:
        print('Por favor, insira um número válido.')
 
controle.ex()
print(f'A temperatura em Fahrenheit é: {controle.converter_para_fahrenheit()}°F')
 
temp = ControleTemperatura
print(temp.temperatura)