from random import *
class Game:
    def play(self):
        print('Let\'s play In-between')
class Inbetween(Game):
    def play(self):
        number = int(input('Choose a number(1 - 10): '))
        while number <1 or number >10:
            number = int(input('Choose a number(1 - 10): '))
        num1 = randint(1,10)#生成较小的数
        num2 = randint(num1,10)#生成较大的数
        while num1 == num2:#检查是否相等，如果相等则重新获得
            num1 = randint(1,10)
            num2 = randint(num1,10)
        print('DEBUG: '+str(num1)+' - '+str(num2))
        if number > num1 and number < num2:#胜利
            print('Computer chose ' +
                  str(num1)+' and '+
                  str(num2)+
                  ', you chose '+
                  str(number)+'.')
            print('You Win!')
            return 1
        if number < num1 or number > num2:#失败
            print('Computer chose ' +
                  str(num1)+
                  ' and '+
                  str(num2)+
                  ', you chose '
                  +str(number)+
                  '.')
            print('You lose!')
            return -1
        if number == num1 or number == num2:#平局
            print('Computer chose ' +
                  str(num1)+' and '+
                  str(num2)+
                  ', you chose '+
                  str(number)+
                  '.')
            print('You Tie!')
            return 0
    
        
            
        
