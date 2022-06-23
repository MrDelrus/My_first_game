import random, pygame
from size import *

class Labyrinth:

    def __init__(self, screen, size):
        if size % 2 == 0:
            raise Exception("size must be odd!")
        if size < 3:
            raise Exception("size must be more than 2!")
        self.size = size
        self.screen = screen
        self.board = self.__generate__(size)
        self.board[1][0] = self.board[size][size + 1] = '+'
        self.r = 2

    def __generate__(self, size):
        board = [['-'] * (size + 2) for x in range(size + 2)]
        edges = set()
        edges.add((1, 2))
        edges.add((2, 1))
        fields = set()
        fields.add((1, 1))
        board[1][1] = '+'
        while len(fields) < ((size + 1) / 2) ** 2:
            self.__add_field__(board, edges, fields)
        return board

    def __get_vertexes_by_edge__(self, edge):
        x, y = edge[0], edge[1]
        if x % 2 == 0:
            return ((x - 1, y), (x + 1, y))
        else:
            return ((x, y - 1), (x, y + 1))

    def __get_edges_by_vertex__(self, vertex):
        (x, y) = vertex
        edges = list()
        if x > 1:
            edges.append((x - 1, y))
        if x < self.size:
            edges.append((x + 1, y))
        if y > 1:
            edges.append((x, y - 1))
        if y < self.size:
            edges.append((x, y + 1))
        return edges

    def __get_second_vertex_in_edge(self, edge, vertex):
        (v, w) = self.__get_vertexes_by_edge__(edge)
        if v == vertex:
            return w
        else:
            return v

    def __add_field__(self, board, edges, fields):
        edge = random.choice(list(edges))
        edges.discard(edge)
        (v, w) = self.__get_vertexes_by_edge__(edge)
        if v in fields and w in fields:
            return
        if w not in fields:
            v = w
        fields.add(v)
        new_edges = self.__get_edges_by_vertex__(v)
        for e in new_edges:
            w = self.__get_second_vertex_in_edge(e, v)
            if w not in fields:
                edges.add(e)
        board[edge[0]][edge[1]] = '+'
        board[v[0]][v[1]] = '+'

    def get_board(self):
        return self.board

    def draw(self, pos):
        if pos == [-1, -1]:
            for raw in range(self.size + 2):
                for col in range(self.size + 2):
                    if self.board[raw][col] == '-':
                        self.image = pygame.image.load('./images/block.png')
                        self.rectangle = self.image.get_rect()
                        self.rectangle.top = field_sz * raw
                        self.rectangle.left = field_sz * col
                        self.screen.blit(self.image, self.rectangle)
        else:
            y = int(pos[0])
            x = int(pos[1])

            for raw in range(self.size + 2):
                for col in list({0, self.size + 1}):
                    if self.board[raw][col] == '-':
                        self.image = pygame.image.load('./images/block.png')
                    else:
                        self.image = pygame.image.load('./images/white.png')
                    self.rectangle = self.image.get_rect()
                    self.rectangle.top = field_sz * raw
                    self.rectangle.left = field_sz * col
                    self.screen.blit(self.image, self.rectangle)
            for col in range(1, self.size + 1):
                for raw in list({0, self.size + 1}):
                    if self.board[raw][col] == '-':
                        self.image = pygame.image.load('./images/block.png')
                    else:
                        self.image = pygame.image.load('./images/white.png')
                    self.rectangle = self.image.get_rect()
                    self.rectangle.top = field_sz * raw
                    self.rectangle.left = field_sz * col
                    self.screen.blit(self.image, self.rectangle)

            for raw in range(y - self.r, y + self.r + 1):
                for col in range(x - self.r, x + self.r + 1):
                    if 0 <= raw and raw < self.size + 2 and 0 <= col and col < self.size + 2:
                        if self.board[raw][col] == '-':
                            self.image = pygame.image.load('./images/block.png')
                        else:
                            self.image = pygame.image.load('./images/white.png')
                        self.rectangle = self.image.get_rect()
                        self.rectangle.top = field_sz * raw
                        self.rectangle.left = field_sz * col
                        self.screen.blit(self.image, self.rectangle)
