import pygame
import sys
from src.chess.color import Color


class Gui:
    def __init__(self, chess_game):
        self.game = chess_game
        self.cell_width = 50
        self.board_size = 8
        self.selected_cell = None
        self.running = True
        self.window_width = 400
        self.screen = pygame.display.set_mode((self.window_width, self.window_width))
        pygame.init()
        pygame.display.set_caption('Chess GUI')

    def start(self):
        while self.running:
            self.frame()
        pygame.quit()
        sys.exit()

    def frame(self):
        for event in pygame.event.get():
            self.handle_event(event)

        white = (255, 255, 255)
        self.screen.fill(white)
        self.draw_board()
        self.draw_figures()
        pygame.display.flip()
        
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_click(*event.pos)
                
    def handle_click(self, x, y):
        col = x // self.cell_width
        row = y // self.cell_width
        clicked_cell = (chr(col + ord('a')), 8 - row)
        print(f'clicked: {clicked_cell}, selected: {self.selected_cell}')
        
        if self.selected_cell is None:
            self.selected_cell = clicked_cell
        else:
            if clicked_cell != self.selected_cell:
                print(f'moving piece from {clicked_cell} to {self.selected_cell}')
                self.game.turn(self.selected_cell, clicked_cell)
                self.selected_cell = clicked_cell

            self.selected_cell = None
        
        
    def draw_board(self):
        def rectangle(col, row):
            return col * self.cell_width, row * self.cell_width, \
                self.cell_width, self.cell_width

        def color(col, row):
            cell_white = (216, 216, 216)
            cell_black = (64, 64, 64)
            return cell_white if (row + col) % 2 == 0 else cell_black

        def draw_cell(color, rectangle_props):
            pygame.draw.rect(self.screen, color, rectangle_props)

        for row in range(self.board_size):
            for col in range(self.board_size):
                draw_cell(color(col, row), rectangle(col, row))

                if self.selected_cell:
                    figure = self.game.get_board().cell(self.selected_cell[0], int(self.selected_cell[1]))
                    if (chr(col + ord('a')), 8 - row) == self.selected_cell:
                        figure_highlight_color = (0, 0, 255)  # Green
                        pygame.draw.rect(self.screen, figure_highlight_color, rectangle(col, row), 3)
                    if figure:
                        possible_moves = figure.turns(self.game.get_board().figures)
                        print(f'moves {possible_moves}')
                        if (chr(col + ord('a')), 8 - row) in possible_moves:
                            highlight_color = (0, 255, 0)  # Green
                            pygame.draw.rect(self.screen, highlight_color, rectangle(col, row), 3)

    def draw_figures(self):
        figure_white = (255, 255, 255)
        figure_black = (0, 0, 0)
        font_filename = "./ui/segoe-ui.ttf"
        font = pygame.font.Font(font_filename, 48)

        def color(fig_color):
            return figure_white if fig_color is Color.WHITE else figure_black

        def cell_coordinates(fig_position):
            pos_literal, pos_numeral = fig_position
            return ord(pos_literal) - ord('a'), 8 - pos_numeral

        def cell_center(cell_coordinates):
            cell_x, cell_y = cell_coordinates
            return (cell_x * self.cell_width + self.cell_width / 2,
                    cell_y * self.cell_width + self.cell_width / 2)

        def draw_figure(figure):
            text_surface = font.render(figure.symbol(), True, color(figure.color))
            text_rect = text_surface.get_rect()
            text_rect.center = cell_center(cell_coordinates(figure.position))
            self.screen.blit(text_surface, text_rect)

        for figure in self.game.get_board().figures:
            draw_figure(figure)
