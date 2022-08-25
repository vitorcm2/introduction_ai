from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State
import sys

class ProblemSpecification(State):

    def __init__(self, op, vacuumPosition, Room):
        self.operator = op
        self.vacuumPosition = vacuumPosition # [vacuumX, vacuumY]
        self.Room = Room #[['L', 'S', 'S', 'S'], ['L', 'L', 'L', 'L'], ['S', 'S', 'S', 'S']]
        self.x = len(Room[0])
        self.y = len(Room)

    def env(self):
        return str(self.vacuumPosition)+";"+self.Room

    def sucessors(self):
        sucessors = []
        clean_room = self.Room
        clean_room[self.vacuumPosition[0]][self.vacuumPosition[1]] = "L"
        sucessors.append(ProblemSpecification('clean',self.vacuumPosition,clean_room))

        if self.vacuumPosition[0] < self.x and self.vacuumPosition[0] != 0:
            newPosition = [self.vacuumPosition[0] - 1,self.vacuumPosition[1]]
            sucessors.append(ProblemSpecification('Move Right',newPosition,clean_room))

        elif self.vacuumPosition[0] >= 0 and self.vacuumPosition[0] != (self.x-1):
            newPosition = [self.vacuumPosition[0] + 1,self.vacuumPosition[1]]
            sucessors.append(ProblemSpecification('Move Left',newPosition,clean_room))
        
        elif self.vacuumPosition[1] < self.y and self.vacuumPosition[1] != 0:
            newPosition = [self.vacuumPosition[0],self.vacuumPosition[1] + 1]
            sucessors.append(ProblemSpecification('Move Down',newPosition,clean_room))

        elif self.vacuumPosition[1] >= 0 and self.vacuumPosition[1] != (self.y-1):
            newPosition = [self.vacuumPosition[0],self.vacuumPosition[1] - 1]
            sucessors.append(ProblemSpecification('Move Up',newPosition,clean_room))

        return sucessors
    
    def is_goal(self):

        for i in self.Room:
            for j in i:
                if j == "S":
                    return False

        return True
    
    def description(self):
        return "Problema do aspirador de pó, realizando a leitura de um arquivo genérico"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

def main(list_position,actualroom):
    print('Busca em profundidade iterativa')
    state = ProblemSpecification(' ',list_position,actualroom)
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

def leitura(path):
    matriz = []
    with open(path) as f:
        lines = f.readlines() 
        for linha in lines:
            linha = linha.strip()
            linha = linha.split(";")
            matriz.append(linha)

    return matriz

if __name__ == '__main__':
    path = sys.argv[0]
    positionx = sys.argv[1]
    positiony = sys.argv[2]

    actualroom = leitura(path)
    main([positionx,positiony],actualroom)
