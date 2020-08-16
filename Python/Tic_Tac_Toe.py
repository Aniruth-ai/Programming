class board:

    state = dict()

    def __init__(self):
        self.board_position_valid = False
        self.restart_game = True
        self.game_status = None
        self.move_count = 0

    def initialize_board(self):

        self.state = {

            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9'
        }

        return self.state

    def validate_position(self, current_player):
        
        while self.board_position_valid == False:

            current_player.move = input('\n{}, enter your move: '.format(current_player.name))

            if current_player.move in self.state.keys():

                if current_player.move != self.state[current_player.move]:

                    print('\n{} you cannot override the position {}. Enter your key at a different location.'.format(current_player.name, current_player.move))
                    self.board_position_valid = False
                
                else:
                    self.board_position_valid = True

            else:
                print('\n{} is not a valid board position. Re-enter a valid position!'.format(current_player.move))
                self.board_position_valid = False

    
    def update_position(self, current_player):

        self.state.update({'{}'.format(current_player.move): '{}'.format(current_player.player_key)})

        self.move_count += 1

        self.board_position_valid = False
        

    def compare_winning_position(self, current_player):

        # Positions 1 2 3 same player wins
        if current_player.player_key == self.state['1'] and current_player.player_key == self.state['2'] and current_player.player_key == self.state['3']:
            self.game_status = 'WIN'

        # Positions 4 5 6 same player wins
        if current_player.player_key == self.state['4'] and current_player.player_key == self.state['5'] and current_player.player_key == self.state['6']:
            self.game_status = 'WIN'        

        # Positions 7 8 9 same player wins
        if current_player.player_key == self.state['7'] and current_player.player_key == self.state['8'] and current_player.player_key == self.state['9']:
            self.game_status = 'WIN'


        # Positions 1 4 7 same player wins
        if current_player.player_key == self.state['1'] and current_player.player_key == self.state['4'] and current_player.player_key == self.state['7']:
            self.game_status = 'WIN'

        # Positions 2 5 8 same player wins
        if current_player.player_key == self.state['2'] and current_player.player_key == self.state['5'] and current_player.player_key == self.state['8']:
            self.game_status = 'WIN'        

        # Positions 3 6 9 same player wins
        if current_player.player_key == self.state['3'] and current_player.player_key == self.state['6'] and current_player.player_key == self.state['9']:
            self.game_status = 'WIN'


        # Positions 1 5 9 same player wins
        if current_player.player_key == self.state['1'] and current_player.player_key == self.state['5'] and current_player.player_key == self.state['9']:
            self.game_status = 'WIN'        

        # Positions 7 5 3 same player wins
        if current_player.player_key == self.state['7'] and current_player.player_key == self.state['5'] and current_player.player_key == self.state['3']:
            self.game_status = 'WIN'        

        else:
            if self.move_count > 7:
                self.game_status = 'DRAW'        


    def display_board_state(self):

        print('\n{}'.format(self.state.get('1').center(12)), '{}'.format(self.state.get('2').center(12)), '{}'.format(self.state.get('3').center(12)))
        print('{}'.format(self.state.get('4').center(12)), '{}'.format(self.state.get('5').center(12)), '{}'.format(self.state.get('6').center(12)))
        print('{}'.format(self.state.get('7').center(12)), '{}'.format(self.state.get('8').center(12)), '{}\n'.format(self.state.get('9').center(12)))        


    def display_initial_board(self):

        print("\n=======================================")
        print("\tWelcome to Tic Tac Toe \N{grinning face with smiling eyes}")
        print("=======================================\n") 
        print('{}'.format(self.state.get('1').center(12)), '{}'.format(self.state.get('2').center(12)), '{}'.format(self.state.get('3').center(12)))
        print('{}'.format(self.state.get('4').center(12)), '{}'.format(self.state.get('5').center(12)), '{}'.format(self.state.get('6').center(12)))
        print('{}'.format(self.state.get('7').center(12)), '{}'.format(self.state.get('8').center(12)), '{}\n'.format(self.state.get('9').center(12)))      

 
class player:

    display_dict = dict()

    def __init__(self):
        self.name = None
        self.move = None
        self.is_winner = False
        self.is_current = False
        self.player_key = None        

    def has_won(self):
        print('{} says Yayy I won!'.format(self.name))


def update_player_status(current_player, Player_1, Player_2):

    if current_player == Player_1 and Player_1.is_current:
        Player_1.is_current = False
        Player_2.is_current = True
        current_player = Player_2

    elif current_player == Player_2 and Player_2.is_current:
        Player_1.is_current = True
        Player_2.is_current = False
        current_player = Player_1    

    return current_player  



def main():

    Board = board()

    while Board.restart_game: 

        Board.initialize_board()

        Board.display_initial_board()     

        for players in range(1,3):

            if 'Player_{}'.format(players) == 'Player_1':
                Player_1 = player()
                Player_1.name = input('Enter player {} name : '.format(players))
                Player_1.player_key = input('{} enter your key: '.format(Player_1.name))
            else:
                Player_2 = player()
                Player_2.name = input('\nEnter player {} name : '.format(players))
                Player_2.player_key = input('{} enter your key: '.format(Player_2.name)) 

        Player_1.is_current = True

        if Player_1.is_current:
            current_player = Player_1

        
        while Board.game_status == None:
            
            Board.validate_position(current_player)
            Board.update_position(current_player)
            Board.display_board_state()
            Board.compare_winning_position(current_player)

            if Board.game_status == 'WIN':
                current_player.has_won()
                
            elif Board.game_status == 'DRAW':
                print('It\'s a DRAW!')

            else:
                current_player = update_player_status(current_player, Player_1, Player_2)


        Board.restart_game = input('\nDo you want to play the game again? Yes or No: ')

        if Board.restart_game == 'Yes':
            Board.game_status = None
            Board.move_count = 0
        
        elif Board.restart_game == 'No':
            print("\n===========================================================================")    
            print("\tThank you! It was pleasure playing with {} and {} \N{grinning face with smiling eyes}".format(Player_1.name, Player_2.name))
            print("=============================================================================")

            Board.restart_game = False        


if __name__ == '__main__':
    main()