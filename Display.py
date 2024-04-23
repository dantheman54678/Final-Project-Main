import pygame as p

#Variables
WIDTH, HEIGHT = 906,1000
B_WIDTH, B_HEIGHT = 900, 900
ROWS, COLS = 9,9
SQUARE_SIZE = B_WIDTH//COLS
FPS = 60

# define colors
White = (255, 255, 255)
Black = (0, 0, 0)
Blue = (173, 216, 230)
Red = (255, 0, 0)
Orange = (255,165,0)
Grey = (128,128,128)

#initialize pygame
p.font.init()
p.display.init()
screen = p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Sudoku")

#Start screen
def start_screen(win):
    #Init screen
    win.fill(White)

    #Init fonts
    title_font = p.font.Font(None, 100)
    game_select_font = p.font.Font(None, 70)
    button_font = p.font.Font(None, 50)

    #Init title
    title = title_font.render("Welcome to Sudoku",0,Black)
    title_space = title.get_rect(center = (WIDTH//2, HEIGHT // 4))

    #Init select text
    game_select = game_select_font.render("Select Game Mode:",0,Black)
    select_space = game_select.get_rect(center = (WIDTH // 2, (2*HEIGHT // 3)))

    #Init easy button
    easy_button = button_font.render("Easy", 0, White)
    easy_surface = p.Surface((easy_button.get_size()[0] + 30, easy_button.get_size()[1] + 30))
    easy_surface.fill(Orange)
    easy_surface.blit(easy_button, (15,15))
    easy_rect = easy_button.get_rect(center = (WIDTH//4, (HEIGHT // 4 + HEIGHT // 2)))

    #Init medium button
    medium_button = button_font.render("Medium", 0, White)
    medium_surface = p.Surface((medium_button.get_size()[0] + 30, medium_button.get_size()[1] + 30))
    medium_surface.fill(Orange)
    medium_surface.blit(medium_button, (15,15))
    medium_rect = medium_button.get_rect(center = (WIDTH//2, (HEIGHT // 4 + HEIGHT // 2)))

    #Init hard button
    hard_button = button_font.render("Hard", 0, White)
    hard_surface = p.Surface((hard_button.get_size()[0] + 30, hard_button.get_size()[1] + 30))
    hard_surface.fill(Orange)
    hard_surface.blit(hard_button, (15,15))
    hard_rect = hard_button.get_rect(center = ((WIDTH//2 + WIDTH // 4), (HEIGHT // 4 + HEIGHT // 2)))

    #Draws all
    screen.blit(title, title_space)
    screen.blit(game_select, select_space)
    screen.blit(easy_surface, easy_rect)
    screen.blit(medium_surface, medium_rect)
    screen.blit(hard_surface, hard_rect)

    #Screen start up
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                return "Quit"
            if event.type == p.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    removed = 30
                    return removed
                elif medium_rect.collidepoint(event.pos):
                    removed = 40
                    return removed
                elif hard_rect.collidepoint(event.pos):
                    removed = 50
                    return removed
            p.display.update()
            
#Creates board
class Board:
    def __init__(self):
        self.board = []
        self.selected_box = None

    #Draws base board
    def draw_squares(self,win):
        win.fill(White)
        for row in range(ROWS):
            for col in range(ROWS):
                if row == 3 or row == 6:
                    if col == 3 or col == 6:
                        p.draw.rect(win, Black, ((row*SQUARE_SIZE), (col*SQUARE_SIZE), SQUARE_SIZE+5, SQUARE_SIZE))
                        p.draw.rect(win, Blue, ((row*SQUARE_SIZE)+11 , (col*SQUARE_SIZE)+11, SQUARE_SIZE-6, SQUARE_SIZE-6))
                        
                    elif col == 8:
                        p.draw.rect(win, Black, ((row*SQUARE_SIZE), (col*SQUARE_SIZE), SQUARE_SIZE+6, SQUARE_SIZE+6))
                        p.draw.rect(win, Blue, ((row*SQUARE_SIZE)+11 , (col*SQUARE_SIZE)+6, SQUARE_SIZE-6, SQUARE_SIZE-6))
                        
                    else:
                        p.draw.rect(win, Black, ((row*SQUARE_SIZE), (col*SQUARE_SIZE), SQUARE_SIZE+5, SQUARE_SIZE))
                        p.draw.rect(win, Blue, ((row*SQUARE_SIZE)+11 , (col*SQUARE_SIZE)+6, SQUARE_SIZE-6, SQUARE_SIZE-6))

                elif col == 3 or col == 6:
                    if row == 8:
                        p.draw.rect(win, Black, ((row*SQUARE_SIZE), (col*SQUARE_SIZE), SQUARE_SIZE+6, SQUARE_SIZE+6))
                        p.draw.rect(win, Blue, ((row*SQUARE_SIZE)+6 , (col*SQUARE_SIZE)+11, SQUARE_SIZE-6, SQUARE_SIZE-6))
                    else:
                        p.draw.rect(win, Black, ((row*SQUARE_SIZE), (col*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE+5))
                        p.draw.rect(win, Blue, ((row*SQUARE_SIZE)+6 , (col*SQUARE_SIZE)+11, SQUARE_SIZE-6, SQUARE_SIZE-6))
                    
                elif row != 8 and col != 8:
                    p.draw.rect(win, Black, ((row*SQUARE_SIZE), (col*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
                    p.draw.rect(win, Blue, ((row*SQUARE_SIZE)+6 , (col*SQUARE_SIZE)+6, SQUARE_SIZE-6, SQUARE_SIZE-6))
                
                else:
                    p.draw.rect(win, Black, ((row*SQUARE_SIZE), (col*SQUARE_SIZE), SQUARE_SIZE+6, SQUARE_SIZE+6))
                    p.draw.rect(win, Blue, ((row*SQUARE_SIZE)+6 , (col*SQUARE_SIZE)+6, SQUARE_SIZE-6, SQUARE_SIZE-6))

    #draws numbers in correct locations
    def draw_numbers(self,grid, win):
        for row in range(ROWS):
            for col in range(COLS):
                value = grid[row][col]
                number = Cell(value,row,col)
                number.calc_position()
                number.draw_number(win)

     def draw_sketch(self, blank_grid, win):
        for row in range(ROWS):
            for col in range(COLS):
                value = blank_grid[row][col]
                number = Cell(value,row,col)
                number.draw_sketch(win)
                
    def draw_border(self, win, row=4, col=4):
        if row == 3 or row == 6:
            if col == 3 or col == 6:
                p.draw.rect(win, Red, ((SQUARE_SIZE*col)+11,(SQUARE_SIZE*row)+11,SQUARE_SIZE-9,SQUARE_SIZE-9), 3)
                        
            else:
                p.draw.rect(win, Red, ((SQUARE_SIZE*col)+6,(SQUARE_SIZE*row)+11,SQUARE_SIZE-6,SQUARE_SIZE-9), 3)
                
        elif col == 3 or col == 6:
            p.draw.rect(win, Red, ((SQUARE_SIZE*col)+11,(SQUARE_SIZE*row)+6,SQUARE_SIZE-9,SQUARE_SIZE-6), 3)
                
        else:
            p.draw.rect(win, Red, ((SQUARE_SIZE*col)+6,(SQUARE_SIZE*row)+6,SQUARE_SIZE-6,SQUARE_SIZE-6), 3)

class Cell:
    def __init__(self,value,row,col):
        self.value = value
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0

    def change_value(self,value):
        self.value = value
        
    def calc_position(self):
        self.x = (SQUARE_SIZE * self.col) + 38
        self.y = (SQUARE_SIZE * self.row) + 12

    def draw_number(self, win):
        font = p.font.SysFont('Times New Roman', 70)
        number_text = font.render(str(self.value), True, Black)
        if self.value != 0:
            win.blit(number_text, ((SQUARE_SIZE * self.col) + 38, (SQUARE_SIZE * self.row) + 12))
        

def get_cordinates(pos):
    x, y = pos
    global row
    row = y // SQUARE_SIZE
    global col
    col = x // SQUARE_SIZE

def check_completed(complete_board, grid):
    for row in range(ROWS):
        for col in range (COLS):
            if grid[row][col] == 0:
                return "pending"
    if completed_board == grid:
        return "winner"
    if completed_board != grid:
        return "game over" 

def main():
   run = True
    blank_grid = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    clock = p.time.Clock()
    board = Board()
    clock.tick(FPS)
    removed = start_screen(screen)
    if removed == "Quit":
        run = False
    else:
        complete_board, grid = generate_sudoku(removed,9)
    do_it = 'no'
    condition = True
    status = "pending"

    while run:
        value = 'None'

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                get_cordinates(pos)
                do_it = "yes"
                
            if event.type == p.KEYDOWN:
                 
                #Arrow key functions need to be added here!
                
                if event.key == p.K_1:
                    val = 1
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_2:
                    val = 2
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_3:
                    val = 3
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_4:
                    val = 4
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_5:
                    val = 5
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_6:
                    val = 6
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_7:
                    val = 7
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_8:
                    val = 8
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_9:
                    val = 9
                    if grid[row][col] == 0:
                        blank_grid[row][col] = val
                if event.key == p.K_RETURN:
                    value = blank_grid[row][col]
                    
        if value != 'None':
            grid[row][col]=value
            blank_grid[row][col] = 0

        status = check_completed(complete_board, grid)
        if status != "pending":
            if status == "winner":
                pass
                #Draw win screen
            else:
                pass
                #Draw game over screen
        
        
        board.draw_squares(screen)
        board.draw_numbers(grid, screen)
        board.draw_sketch(blank_grid, screen)
        if do_it == "yes":
            board.draw_border(screen, row, col)
            
        p.display.update()
    p.quit()

if __name__ == "__main__":
    main()
