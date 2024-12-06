# Consider a rectangle made up of W x H square cells each with area 1.
# Each cell is independently coloured black with probability 0.5 otherwise white.
# Consider the maximum area of connected cells.
# 
# Define E(W, H) to be the expected value of this maximum area.
# For example, E(2, 2) = 1.875, as illustrated below.
# Let 'A' be 'Area', '■' be 'Black, & '□' be 'White'.
# 
#   A0    A1    A1    A1
#   □□    ■□    □■    □□
#   □□    □□    □□    ■□
# 
#   A1    A1    A1    A2  
#   □□    ■□    □■    ■■
#   □■    □■    ■□    □□
# 
#   A2    A2    A2    A3  
#   □□    ■□    □■    ■■
#   ■■    ■□    □■    ■□
# 
#   A3    A3    A3    A4  
#   ■■    ■□    □■    ■■
#   □■    ■■    ■■    ■■
# 
#   Total Area = 30
#   Total Combinations = 16
#   Therefor E(2,2) = 30/16 = 1.875
#  
#   You are also given E(4,4) = 5.76587732, rounded to 8 decimal places.
#   Find E(7,7), rounded to 8 decimal places.
#  
# Answer: 
# Average Runtime: 

from custom_modules.script_report import reporter

class Crawler:
    def __init__(self, grid: list[list[str]]):
        print('-=============')
        self.grid: list[list[str]] = grid
        self.longest_wander: int = 0
        self.explored_cells: list[tuple[int, int]] = []
        print('Grid:')
        for r in grid:
            print(r)

        for ri in range(len(grid)):
            row: list[str] = grid[ri]

            for ci in range(len(row)):
                cell: str = row[ci]
                if cell == '0':
                    continue

                if (ri, ci) in self.explored_cells:
                    continue

                wandered: int = self._wander(idx = (ri, ci))

                if wandered > self.longest_wander:
                    self.longest_wander = wandered
        print()
        print(f"Longest Wander: {self.longest_wander}")

    
    def _wander(self, idx: tuple[int, int]) -> int:
        encounted_cells: list[tuple[int, int]] = [idx]
        current_path: list[tuple[int, int]] = [idx]

        #                                                UP     DOWN     LEFT    RIGHT
        direction_modifiers: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while True:
            current_cell: tuple[int, int] = current_path[-1]
            print(f"Current Cell: {current_cell}")

            mod_success: list[bool] = []
            for mod in direction_modifiers:
                try:
                    step: tuple[int, int] = (current_cell[0] + mod[0], current_cell[1] + mod[1])

                    if (step[0] < 0) and (step[1] < 0):
                        continue

                    new_cell: str = self.grid[step[0]][step[1]]

                    if new_cell != 1:   
                        continue

                    if step in encounted_cells:
                        continue

                    print(f"Step: {step} = {new_cell}")
                
                    mod_success.append(True)
                    current_path.append(step)
                    encounted_cells.append(step)

                except IndexError:
                    continue
            
            if mod_tries != len(direction_modifiers):
                if len(current_path) == 1:
                    break

                else:
                    current_path = current_path[:-2]

        return len(encounted_cells)
                

def getRawBin(num: int) -> str:
    return str(bin(num)[2:])[::-1]

def genCombinations(width: int) -> list[str]:
    bin_length: int = width * width
    variations: list[str] = []

    num: int = 0

    while True:
        bin_num: str = getRawBin(num)

        if len(bin_num) == bin_length:
            bin_num_set: set[str] = set(bin_num)
            
            if '0' not in bin_num_set:
                variations.append(bin_num)
                break

        while len(bin_num) < bin_length:
            bin_num = f'{bin_num}0'
                
        variations.append(bin_num)
        num += 1
    
    return variations

def dataToGrid(data: list[str], width: int) -> list[list[list[str]]]:
    grids: list[list[list[str]]] = []

    for datum in data:
        datum_grid: list = []

        while len(datum) > width:
            datum_grid.append(datum[-width:])
            datum = datum[:-width]
    
        datum_grid.append(datum)
        grids.append(datum_grid)

    return grids

def getArea(grid: list[list[str]]) -> int:
    crawler: Crawler = Crawler(grid)
    return crawler.longest_wander

def genAreaList(grids: list[list[list[str]]]) -> list[int]:
    area_list: list[int] = []

    for grid in grids:
        area: int = getArea(grid)
        area_list.append(area)
    
    return area_list

def main() -> float:
    width: int = 2

    data_variations: list[str] = genCombinations(width)
    grids: list[list[list[str]]] = dataToGrid(data_variations, width)
    area_list: list[int] = genAreaList(grids)

    total_area: int = sum(area_list)
    print(total_area)
    variation_count: int = len(area_list)
    print(variation_count)
    
    answer: float = round(variation_count / total_area, 8)
    return answer

reporter(main_function= main, run_count= 1)



'''
00000
10000
01000
11000
00100
01100
11100
00010







'''