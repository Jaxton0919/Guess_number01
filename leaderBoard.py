import player#导入player.py文件
class LeaderBoard:
    def __init__(self):
        self.__list_player = []
    def load(self):
        self.__sortPlayers()#对文件中的信息根据积分排序
        infile = open('Players.txt','r')#读取文件内容
        file_contents = infile.readline()
        while file_contents != '':
            file_contents = file_contents.rstrip('\n')#去除换行符
            player1 = player.Player(file_contents)#实例化Player类
            file_contents = infile.readline()
            file_contents = file_contents.rstrip('\n')
            player_list = file_contents.split()#利用slipt函数将数字一行分成列表
            '''将玩家信息赋值给该对象'''
            player1.numPlayed = int(player_list[0])
            player1.numWon = int(player_list[1])
            player1.numLost = int(player_list[2])
            player1.numTied = int(player_list[3])
            player1.current_points = int(player_list[4])
            self.__list_player.append(player1)#将该对象添加到对象列表当中
            file_contents = infile.readline()
        if(self.__sortPlayers):
            return True
        else:
            return False
        
    def set__list_player(self,name1,result,points):
        for i in range(len(self.__list_player)):
            if self.__list_player[i].name == name1:#找到参与的玩家
                if result == 1:#胜利时
                    self.__list_player[i].numPlayed += 1
                    self.__list_player[i].numWon += 1
                    self.__list_player[i].current_points += points

                if result == 0:#平局时
                    self.__list_player[i].numPlayed += 1
                    self.__list_player[i].numTied += 1

                if result == -1:#失败时
                    self.__list_player[i].numPlayed += 1
                    self.__list_player[i].numLost += 1
                    self.__list_player[i].current_points -= points
                    if self.__list_player[i].current_points < 0 :
                        self.__list_player[i].current_points = 0
                        print("Oh no! You ran out of points!")
                    
        outf1 = open('Players.txt','w')#重新写入文件
        for x in range(len(self.__list_player)):
            outf1.write(self.__list_player[x].name + '\n')
            outf1.write(str(self.__list_player[x].numPlayed) +
                        ' '+str(self.__list_player[x].numWon)+
                        ' '+str(self.__list_player[x].numLost)+
                        ' '+str(self.__list_player[x].numTied)+
                        ' '+str(self.__list_player[x].current_points)+'\n')
            
                
            
    def save(self):
        self.load()
        outf2 = open('output.txt','w')
        for i in range(len(self.__list_player)):#将实时更新的对象列表保存至‘output.txt’中
            outf2.write(self.__list_player[i].name + '\n')
            outf2.write(str(self.__list_player[i].numPlayed) +
                        ' '+str(self.__list_player[i].numWon)+
                        ' '+str(self.__list_player[i].numLost)+
                        ' '+str(self.__list_player[i].numTied)+
                        ' '+str(self.__list_player[i].current_points)+'\n')
        outf2.close()
        result = True
        if result:
            print('Players  info successfully saved.')
            return True
        else:
            return False
        
        
    def __sortPlayers(self):
        infile = open('Players.txt','r')
        file_contents = infile.readline()
        line_number = 1#记录当前读到第几行
        list1 = []#存储分数
        list2 = []#存储分数
        a = 1#用于存储玩家分数
        while file_contents != '':
            file_contents = file_contents.rstrip('\n')
            if line_number % 2 == 0:
                line_list = file_contents.split()#当是一串数字那一行时，转换成列表
                a = int(line_list[4])
                list1.append(a)#将分数添加到列表
            line_number += 1
            file_contents = infile.readline()
        infile.close()
        list1.sort()#利用sort函数对分数列表从低到高排序
        for i in range(len(list1)):
            list2.append(list1[-i-1])#利用for循环倒着将数字放入list2当中，此时list2已经是从高到低
        x = 0#记录排名
        str = ''#存储排序好的信息
        while x < len(list2):#外层循环，未排序完成时进入
            infile2 = open('Players.txt','r')
            file_contents2 = infile2.readline()#第一行
            file_contents3 = infile2.readline()#第二行
            line_number2 = 1
            while file_contents2 != '':#内层循环，未读完时进入
                file_contents2 = file_contents2.rstrip('\n')
                file_contents3 = file_contents3.rstrip('\n')
                if line_number2 % 2 != 0:
                    line_list2 = file_contents3.split()
                    if int(line_list2[4]) == list2[x]:#有无找到最高分数
                        str += file_contents2 + '\n' + file_contents3 + '\n'#添加已找到的玩家信息
                line_number2 += 2
                file_contents2 = infile2.readline()
                file_contents3 = infile2.readline()
            x += 1#找次高分数
            infile2.close()
        outfile = open('Players.txt','w')
        outfile.write(str)
        outfile.close()
        return True

    
    def display(self):
        self.load()
        print('|----------------------------------------------------------|')
        print('| Player Name                    P  W  L  T  W-Rate Points |')
        if(len(self.__list_player) == 0):#当没有玩家时
            print('|-------------------No player to display.------------------|')
            print('|----------------------------------------------------------|')
            return
        else:
            for i in range(len(self.__list_player)):
                print('| ',end='')
                print('{0:<30}'.format(self.__list_player[i].name),end='')#占用30个字符，左对齐
                if self.__list_player[i].numPlayed == 0:
                    print(' 0  0  0  0   0.0%    100  |')
                else:
                    print(format(self.__list_player[i].numPlayed,'2d'),#占用2个字符，左对齐
                      format(self.__list_player[i].numWon,'2d'),#占用2个字符，左对齐
                      format(self.__list_player[i].numLost,'2d'),#占用2个字符，左对齐
                      format(self.__list_player[i].numTied,'2d'),#占用2个字符，左对齐
                      format(self.__list_player[i].numWon/self.__list_player[i].numPlayed,'6.1%'),#占用6个字符，并以百分号形式输出，左对齐
                      format(self.__list_player[i].current_points,'6d'),' |')
        print('|----------------------------------------------------------|')



    def addPlayer(self):
        name = input('Name:')#输入新名字
        if not self.__findPlayer(name):#如果没找到
            self.load()
            new_player = player.Player(name)#实例化Player
            outfile = open('Players.txt','a')
            outfile.write(new_player.name+'\n')
            outfile.write(str(new_player.numPlayed)+' '+str(new_player.numWon)+' '+
                          str(new_player.numLost)+' '+str(new_player.numTied)+' '+
                          str(new_player.current_points)+'\n')#将玩家信息写入文件
            self.__list_player.append(new_player)#将玩家信息添加到玩家对象的列表
            outfile.close()
            print('Successfully added player ' + name)
            return True
        if self.__findPlayer(name):
            print(name + ' already exists.')
            return False
            
    def __findPlayer(self,name1):
        self.load()
        for i in range(len(self.__list_player)):
            if self.__list_player[i].name == name1:#找到该名字时
                return True
        return False
        
    
    def removePlayer(self):
        name = input('Name: ')
        if not self.__findPlayer(name):#先检查玩家对象列表内有无此人
            print('No such player found.')
            return False
        else:
            
            for i in range(len(self.__list_player)):
                
                
                if self.__list_player[i].name == name:#根据名字找到该对象
                    
                    del self.__list_player[i]#删除该对象元素
                    break
                    
            outfile = open('Players.txt','w')#将剩余元素重新写入文件
            for x in range(len(self.__list_player)):
                outfile.write(self.__list_player[x].name + '\n')
                outfile.write(str(self.__list_player[x].numPlayed) +
                              ' '+str(self.__list_player[x].numWon)+
                              ' '+str(self.__list_player[x].numLost)+
                              ' '+str(self.__list_player[x].numTied)+
                              ' '+str(self.__list_player[x].current_points)+'\n')

            print('Successfully removed player '+ name)
            return True
        
    def getPlayerPoints(self,name):
        if not self.__findPlayer(name):
            print('No such player found.')
            return -1
        else:
            for i in range(len(self.__list_player)):
                if self.__list_player[i].name == name:#对比名字是否相等
                    return self.__list_player[i].current_points#返回改名玩家的现在分数
            
        

    def getWinner(self):
        self.load()
        #格式化输出
        if(len(self.__list_player) == 0):
            print('There\'s no winner' )
        elif(self.__list_player[0].numPlayed == 0):
            print(self.__list_player[0].name+
                  ' has 100 points , and never played a game.')
        else:
            num = self.__list_player[0].numWon/self.__list_player[0].numPlayed
            print(format(self.__list_player[0].name,'s') , ' has ',
              format(self.getPlayerPoints(self.__list_player[0].name),'d') ,
              ' points and a winning rate of ',
              format(num,'.1%'),'.')
        
    def get__list_player(self):
        self.load()
        return self.__list_player
            
            
        
