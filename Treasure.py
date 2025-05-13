# 1. create the map
def create_map(grid):
    # print the top border
    print('-------------------------------')
    # print each row
    for row in grid:
        # Build and print the row string
        line='|'
        for cell in row:
            line+=f' {cell} |'
        # End of a line
        print(line)
        # Print a separator line
        print('-------------------------------')


# 2. create the Player Class
class Player:
    # track the player's position and treasure counts.
    def __init__(self):
        self.x=0           # current row
        self.y=0           # current column
        self.count_A=0     # number of 🌸 collected
        self.count_B=0     # number of 💎 collected
    
    def move(self, direction):
        ''' 
        Player moves in w/a/s/d.
        Returns True if moved, False if out of bounds.
        '''
        # move
        dx=0
        dy=0
        if direction=='w':
            dx=-1
        elif direction=='a':
            dy=-1
        elif direction=='s':
            dx=1
        elif direction=='d':
            dy=1
        
        new_x=self.x+dx
        new_y=self.y+dy

        # check if out of bounds
        if not(0<=new_x<6 and 0<=new_y<6):
            print('You can\'t move outside the map!')
            return False
        
        self.x=new_x
        self.y=new_y
        return True

    def collect(self, grid):
        '''
        Collects treasure on the current cell.
        Turns it back into grassland.
        '''
        # collect
        cell=grid[self.x][self.y]
        if cell=='🌸':
            self.count_A+=1
            grid[self.x][self.y]='🟩'
            print(f'\nCongrats:)! Collected a 🌸! Total 🌸: {self.count_A}')
        elif cell=='💎':
            self.count_B+=1
            grid[self.x][self.y]='🟩'
            print(f'\nCongrats:)! Collected a 💎! Total 💎: {self.count_B}')
        
    def status(self):
         # print current treasure counts
         print(f'\nUntil now, you have:\n🌸: {self.count_A}\n💎: {self.count_B}')
        
def print_map(grid, player):
    ''' 
    this function just like create_map, 
    but it marked the player's position by 🚶
    '''
    # print the top border
    print('-------------------------------')
    # print each row
    for i, row in enumerate(grid):
    # Build and print the row string
        line='|'
        for j, cell in enumerate(row):
            if i==player.x and j==player.y:
                line+=f' 🚶 |'
            else:
                line+=f' {cell} |'
        # End of a line
        print(line)
        # Print a separator line
        print('-------------------------------')

def main():
    # 1. show the map
    print('Welcome to this treasure hunting game! Here\'s the map!')
    grid=[
    ['🎯', '🟩', '🌸', '🟩', '🟩', '🟩'],
    ['🟩', '🌸', '🟩', '💎', '🟩', '🟩'],
    ['🟩', '🟩', '🌸', '🟩', '💎', '🟩'],
    ['💎', '🟩', '🟩', '🟩', '🟩', '🌸'],
    ['🟩', '💎', '🟩', '🟩', '🌸', '🟩'],
    ['🟩', '🟩', '🟩', '💎', '🟩', '🏁']
]
    create_map(grid)

    # 2. player enter the command
    player=Player()

    while True:
        command=input('\nPlease enter your command (w/a/s/d/status/STOP): ')     
        # command: STOP
        if command=='STOP':
            print('\nYou stop the game!')
            player.status()
            break

        # command: status
        elif command=='status':
            player.status()
            continue
        
        # command: w/a/s/d
        elif command in ('w', 'a', 's', 'd'):
            # try to move, and ensure it isn't out of bounds
            if not player.move(command):
                continue

            # move successfully, collect the treasure
            player.collect(grid)

            # show the current map
            print_map(grid, player)

        # invalid command
        else:
            print('Invalid command! You should enter w/a/s/d/status/STOP! ')
        
        # check win/lose if the player arrives at 🏁
        if player.x==5 and player.y==5:
            player.status()
            if player.count_A>=3 and player.count_B>=3:
                print('\n🎉Congrats! You have arrived at 🏁 and collected enough treasures! You win! 🎉\n')
            else:
                print('\nYou made it to 🏁, but your treasure bag feels empty…Try again😢\n')
            break

if __name__ == "__main__":
    main()

