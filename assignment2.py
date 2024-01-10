import leaderBoard
import inbetweengame
def main():
    print('Players info successfully loaded.')
    print()
    con = True
    while(con):
        print('Please enter a command [list, add, remove, play, winner, \nquit]: ',end='')
        command = input()
        if command == 'list':
            leader_board = leaderBoard.LeaderBoard()
            leader_board.display()
        elif command == 'add':
            leader_board = leaderBoard.LeaderBoard()
            leader_board.addPlayer()
        elif command == 'remove':
            leader_board = leaderBoard.LeaderBoard()
            leader_board.removePlayer()
        elif command == 'play':
            name = input('Name:')
            leader_board = leaderBoard.LeaderBoard()
            list1 = leader_board.get__list_player()
            print(len(list1))
            not_enough = False
            for i in range(len(list1)):
                if list1[i].name == name:
                    if list1[i].current_points == 0:
                        print("Not enough points to play.")
                        not_enough = True
            if not_enough:
                continue
            points = int(input('How many points to bid (1-100):'))
            while points < 1 or points > 100:
                points = int(input('How many points to bid (1-100):'))
            game_type = input('Which game([r]Rock-Paper-Scissors,[i]In-between)')
            if game_type == 'i':
                game_object2 = inbetweengame.Game()
                game_object1 = inbetweengame.Inbetween()
                result = game_object1.play()
            leader_board2 = leaderBoard.LeaderBoard()
            leader_board2.load()
            leader_board2.set__list_player(name,result,points)
        elif command == 'winner':
            leader_board = leaderBoard.LeaderBoard()
            leader_board.getWinner()
        else:
            print('Thank you for playing!')
            leader_board = leaderBoard.LeaderBoard()
            leader_board.save()
            con = False
main()
