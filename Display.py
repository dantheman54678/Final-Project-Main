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

#initialize pygame
p.font.init()
p.display.init()
screen = p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("Sudoku")

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

    def draw_number(self, row, col, value, win):
        font = p.font.SysFont('Times New Roman', 70)
        number_text = font.render(str(value), True, Black)
        win.blit(number_text, ((SQUARE_SIZE * col) + 38, (SQUARE_SIZE * row) + 12))
        

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
        

    

def main():
    run = True
    clock = p.time.Clock()
    board = Board()
    grid = generate_sudoku(30,9)
    condition = True
    
    
    while run:
        value = 'None'
        
        clock.tick(FPS)

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                get_cordinates(pos)

            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    value = 1
                if event.key == p.K_2:
                    value = 2
                if event.key == p.K_3:
                    value = 3
                if event.key == p.K_4:
                    value = 4
                if event.key == p.K_5:
                    value = 5
                if event.key == p.K_6:
                    value = 6
                if event.key == p.K_7:
                    value = 7
                if event.key == p.K_8:
                    value = 8
                if event.key == p.K_9:
                    value = 9
                if event.key == p.K_BACKSPACE:
                    value = 0
        if value != 'None':
            grid[row][col]=value
        
        board.draw_squares(screen)
        board.draw_numbers(grid, screen)
        p.display.update()
    p.quit()

if __name__ == "__main__":
    main()
