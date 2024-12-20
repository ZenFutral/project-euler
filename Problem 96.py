# Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. 
# Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. 
# The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. 
#           
#           EMPTY                                    SOLVED
#   _ _ 3 | _ 2 _ | 6 _ _                    4 8 3 | 9 2 1 | 6 5 7
#   9 _ _ | 3 _ 5 | _ _ 1                    9 6 7 | 3 4 5 | 8 2 1
#   _ _ 1 | 8 _ 6 | 4 _ _                    2 5 1 | 8 7 6 | 4 9 3
#  -----------------------                   ---------------------
#   _ _ 8 | 1 _ 2 | 9 _ _                    5 4 8 | 1 3 2 | 9 7 6
#   7 _ _ | _ _ _ | _ _ 8                    7 2 9 | 5 6 4 | 1 3 8
#   _ _ 6 | 7 _ 8 | 2 _ _                    1 3 6 | 7 9 8 | 2 4 5
#  -----------------------                   ---------------------
#   _ _ 2 | 6 _ 9 | 5 _ _                    3 7 2 | 6 8 9 | 5 1 4
#   8 _ _ | 2 _ 3 | _ _ 9                    8 1 4 | 2 5 3 | 7 6 9
#   _ _ 5 | _ 1 _ | 3 _ _                    6 9 5 | 4 1 7 | 3 8 2
#  
# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). 
# The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.
# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
# 
# Answer: 
# Average Runtime: 

sudoku_puzzles: dict[str, list[list[int]]] = {
    "Grid 01": [
        [0, 0, 3, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0]], 
    "Grid 02": [
        [2, 0, 0, 0, 8, 0, 3, 0, 0],
        [0, 6, 0, 0, 7, 0, 0, 8, 4],
        [0, 3, 0, 5, 0, 0, 2, 0, 9],
        [0, 0, 0, 1, 0, 5, 4, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 2, 7, 0, 6, 0, 0, 0],
        [3, 0, 1, 0, 0, 7, 0, 4, 0],
        [7, 2, 0, 0, 4, 0, 0, 6, 0],
        [0, 0, 4, 0, 1, 0, 0, 0, 3]],
    "Grid 03": [
        [0, 0, 0, 0, 0, 0, 9, 0, 7],
        [0, 0, 0, 4, 2, 0, 1, 8, 0],
        [0, 0, 0, 7, 0, 5, 0, 2, 6],
        [1, 0, 0, 9, 0, 4, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 9],
        [9, 2, 0, 1, 0, 8, 0, 0, 0],
        [0, 3, 4, 0, 5, 9, 0, 0, 0],
        [5, 0, 7, 0, 0, 0, 0, 0, 0]],
    "Grid 04": [ 
        [0, 3, 0, 0, 5, 0, 0, 4, 0],
        [0, 0, 8, 0, 1, 0, 5, 0, 0],
        [4, 6, 0, 0, 0, 0, 0, 1, 2],
        [0, 7, 0, 5, 0, 2, 0, 8, 0],
        [0, 0, 0, 6, 0, 3, 0, 0, 0],
        [0, 4, 0, 1, 0, 9, 0, 3, 0],
        [2, 5, 0, 0, 0, 0, 0, 9, 8],
        [0, 0, 1, 0, 2, 0, 6, 0, 0],
        [0, 8, 0, 0, 6, 0, 0, 2, 0]],
    "Grid 05": [
        [0, 2, 0, 8, 1, 0, 7, 4, 0],
        [7, 0, 0, 0, 0, 3, 1, 0, 0],
        [0, 9, 0, 0, 0, 2, 8, 0, 5],
        [0, 0, 9, 0, 4, 0, 0, 8, 7],
        [4, 0, 0, 2, 0, 8, 0, 0, 3],
        [1, 6, 0, 0, 3, 0, 2, 0, 0],
        [3, 0, 2, 7, 0, 0, 0, 6, 0],
        [0, 0, 5, 6, 0, 0, 0, 0, 8],
        [0, 7, 6, 0, 5, 1, 0, 9, 0]],
    "Grid 06": [
        [1, 0, 0, 9, 2, 0, 0, 0, 0],
        [5, 2, 4, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 5, 0, 0, 0, 8, 1, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 2, 7, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 9, 4, 5],
        [0, 0, 0, 0, 7, 1, 0, 0, 6]],
    "Grid 07": [
        [0, 4, 3, 0, 8, 0, 2, 5, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 9, 4],
        [9, 0, 0, 0, 0, 4, 0, 7, 0],
        [0, 0, 0, 6, 0, 8, 0, 0, 0],
        [0, 1, 0, 2, 0, 0, 0, 0, 3],
        [8, 2, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 3, 4, 0, 9, 0, 7, 1, 0]],
    "Grid 08": [
        [4, 8, 0, 0, 0, 6, 9, 0, 2],
        [0, 0, 2, 0, 0, 8, 0, 0, 1],
        [9, 0, 0, 3, 7, 0, 0, 6, 0],
        [8, 4, 0, 0, 1, 0, 2, 0, 0],
        [0, 0, 3, 7, 0, 4, 1, 0, 0],
        [0, 0, 1, 0, 6, 0, 0, 4, 9],
        [0, 2, 0, 0, 8, 5, 0, 0, 7],
        [7, 0, 0, 9, 0, 0, 6, 0, 0],
        [6, 0, 9, 2, 0, 0, 0, 1, 8]],
    "Grid 09": [
        [0, 0, 0, 9, 0, 0, 0, 0, 2],
        [0, 5, 0, 1, 2, 3, 4, 0, 0],
        [0, 3, 0, 0, 0, 0, 1, 6, 0],
        [9, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 5],
        [0, 9, 1, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 4, 3, 9, 0, 2, 0],
        [4, 0, 0, 0, 0, 7, 0, 0, 0]],
    "Grid 10": [
        [0, 0, 1, 9, 0, 0, 0, 0, 3],
        [9, 0, 0, 7, 0, 0, 1, 6, 0],
        [0, 3, 0, 0, 0, 5, 0, 0, 7],
        [0, 5, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 4, 3, 0, 2, 6, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 7, 0],
        [6, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 4, 2, 0, 0, 7, 0, 0, 6],
        [5, 0, 0, 0, 0, 6, 8, 0, 0]],
    "Grid 11": [
        [0, 0, 0, 1, 2, 5, 4, 0, 0],
        [0, 0, 8, 4, 0, 0, 0, 0, 0],
        [4, 2, 0, 8, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 5],
        [0, 6, 0, 9, 0, 2, 0, 1, 0],
        [5, 1, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 3, 0, 4, 9],
        [0, 0, 0, 0, 0, 7, 2, 0, 0],
        [0, 0, 1, 2, 9, 8, 0, 0, 0]],
    "Grid 12": [
        [0, 6, 2, 3, 4, 0, 7, 5, 0],
        [1, 0, 0, 0, 0, 5, 6, 0, 0],
        [5, 7, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 9, 4, 8, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 5, 8, 3, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 1],
        [0, 0, 6, 4, 0, 0, 0, 0, 7],
        [0, 5, 9, 0, 8, 3, 2, 6, 0]],
    "Grid 13": [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 9, 0, 0, 0],
        [2, 0, 0, 5, 0, 4, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 7, 0, 0],
        [1, 6, 0, 0, 0, 0, 0, 5, 8],
        [7, 0, 4, 3, 1, 0, 6, 0, 0],
        [0, 0, 0, 8, 9, 0, 1, 0, 0],
        [0, 0, 0, 0, 6, 7, 0, 8, 0],
        [0, 0, 0, 0, 0, 5, 4, 3, 7]],
    "Grid 14": [
        [6, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 8],
        [0, 0, 5, 6, 7, 4, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 3, 4, 0, 1, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 3, 4, 5],
        [0, 0, 0, 0, 0, 7, 0, 0, 4],
        [0, 8, 0, 3, 0, 0, 9, 0, 2],
        [9, 4, 7, 1, 0, 0, 0, 8, 0]],
    "Grid 15": [
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 8, 0, 3, 5, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 6, 0, 2],
        [0, 3, 1, 0, 4, 6, 9, 7, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 1, 2, 0, 3],
        [0, 4, 9, 0, 0, 0, 7, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [8, 0, 0, 0, 0, 4, 0, 0, 0]],
    "Grid 16": [
        [3, 6, 1, 0, 2, 5, 9, 0, 0],
        [0, 8, 0, 9, 6, 0, 0, 1, 0],
        [4, 0, 0, 0, 0, 0, 0, 5, 7],
        [0, 0, 8, 0, 0, 0, 4, 7, 1],
        [0, 0, 0, 6, 0, 3, 0, 0, 0],
        [2, 5, 9, 0, 0, 0, 8, 0, 0],
        [7, 4, 0, 0, 0, 0, 0, 0, 5],
        [0, 2, 0, 0, 1, 8, 0, 6, 0],
        [0, 0, 5, 4, 7, 0, 3, 2, 9]],
    "Grid 17": [
        [0, 5, 0, 8, 0, 7, 0, 2, 0],
        [6, 0, 0, 0, 1, 0, 0, 9, 0],
        [7, 0, 2, 5, 4, 0, 0, 0, 6],
        [0, 7, 0, 0, 2, 0, 3, 0, 1],
        [5, 0, 4, 0, 0, 0, 9, 0, 8],
        [1, 0, 3, 0, 8, 0, 0, 7, 0],
        [9, 0, 0, 0, 7, 6, 2, 0, 5],
        [0, 6, 0, 0, 9, 0, 0, 0, 3],
        [0, 8, 0, 1, 0, 3, 0, 4, 0]],
    "Grid 18": [
        [0, 8, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 4, 5, 7],
        [0, 0, 0, 0, 7, 0, 8, 0, 9],
        [0, 6, 0, 4, 0, 0, 9, 0, 3],
        [0, 0, 7, 0, 1, 0, 5, 0, 0],
        [4, 0, 8, 0, 0, 7, 0, 2, 0],
        [9, 0, 1, 0, 2, 0, 0, 0, 0],
        [8, 4, 2, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 0]],
    "Grid 19": [
        [0, 0, 3, 5, 0, 2, 9, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [1, 0, 6, 0, 0, 0, 3, 0, 5],
        [9, 0, 0, 2, 5, 1, 0, 0, 8],
        [0, 7, 0, 4, 0, 8, 0, 3, 0],
        [8, 0, 0, 7, 6, 3, 0, 0, 1],
        [3, 0, 8, 0, 0, 0, 1, 0, 4],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 5, 1, 0, 4, 8, 0, 0]],
    "Grid 20": [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 5, 1, 0, 0],
        [0, 5, 1, 9, 0, 7, 4, 2, 0],
        [2, 9, 0, 4, 0, 1, 0, 6, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 4, 0, 5, 0, 8, 0, 9, 3],
        [0, 2, 6, 7, 0, 9, 5, 8, 0],
        [0, 0, 5, 1, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    "Grid 21": [
        [0, 2, 0, 0, 3, 0, 0, 9, 0],
        [0, 0, 0, 9, 0, 7, 0, 0, 0],
        [9, 0, 0, 2, 0, 8, 0, 0, 5],
        [0, 0, 4, 8, 0, 6, 5, 0, 0],
        [6, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 3, 1, 0, 2, 9, 0, 0],
        [8, 0, 0, 6, 0, 5, 0, 0, 7],
        [0, 0, 0, 3, 0, 9, 0, 0, 0],
        [0, 3, 0, 0, 2, 0, 0, 5, 0]],
    "Grid 22": [
        [0, 0, 5, 0, 0, 0, 0, 0, 6],
        [0, 7, 0, 0, 0, 9, 0, 2, 0],
        [0, 0, 0, 5, 0, 0, 1, 0, 7],
        [8, 0, 4, 1, 5, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 9, 2, 8, 0, 5],
        [9, 0, 7, 0, 0, 6, 0, 0, 0],
        [0, 3, 0, 4, 0, 0, 0, 1, 0],
        [2, 0, 0, 0, 0, 0, 6, 0, 0]],
    "Grid 23": [
        [0, 4, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 1, 9, 4, 3, 6, 0, 0],
        [0, 0, 9, 0, 0, 0, 3, 0, 0],
        [6, 0, 0, 0, 5, 0, 0, 0, 2],
        [1, 0, 3, 0, 0, 0, 5, 0, 6],
        [8, 0, 0, 0, 2, 0, 0, 0, 7],
        [0, 0, 5, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 4, 3, 6, 7, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 4, 0]],
    "Grid 24": [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 2],
        [3, 9, 0, 7, 0, 0, 0, 8, 0],
        [4, 0, 0, 0, 0, 9, 0, 0, 1],
        [2, 0, 9, 8, 0, 1, 3, 0, 7],
        [6, 0, 0, 2, 0, 0, 0, 0, 8],
        [0, 1, 0, 0, 0, 8, 0, 5, 3],
        [9, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0]],
    "Grid 25": [
        [3, 6, 0, 0, 2, 0, 0, 8, 9],
        [0, 0, 0, 3, 6, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 0, 0, 6, 0, 2],
        [4, 0, 0, 6, 0, 3, 0, 0, 7],
        [6, 0, 7, 0, 0, 0, 1, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 1, 8, 0, 0, 0],
        [9, 7, 0, 0, 3, 0, 0, 1, 4]],
    "Grid 26" :[
        [5, 0, 0, 4, 0, 0, 0, 6, 0],
        [0, 0, 9, 0, 0, 0, 8, 0, 0],
        [6, 4, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 8],
        [2, 0, 8, 0, 0, 0, 5, 0, 1],
        [7, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 8, 4],
        [0, 0, 3, 0, 0, 0, 6, 0, 0],
        [0, 6, 0, 0, 0, 3, 0, 0, 2]],
    "Grid 27" :[
        [0, 0, 7, 2, 5, 6, 4, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 1, 0, 0, 3, 0, 0, 6, 0],
        [0, 0, 0, 5, 0, 8, 0, 0, 0],
        [0, 0, 8, 0, 6, 0, 2, 0, 0],
        [0, 0, 0, 1, 0, 7, 0, 0, 0],
        [0, 3, 0, 0, 7, 0, 0, 9, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 6, 3, 1, 2, 7, 0, 0]],
    "Grid 28" :[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 9, 0, 5, 0, 1, 8, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 3, 0, 6, 8, 0, 0],
        [4, 5, 0, 7, 0, 8, 0, 9, 6],
        [0, 0, 3, 5, 0, 2, 7, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 1, 6, 0, 3, 0, 4, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]],
    "Grid 29" :[
        [0, 3, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 9, 0, 0, 0, 5, 0, 0],
        [0, 0, 7, 5, 0, 9, 2, 0, 0],
        [7, 0, 0, 1, 0, 5, 0, 0, 8],
        [0, 2, 0, 0, 9, 0, 0, 3, 0],
        [9, 0, 0, 4, 0, 2, 0, 0, 1],
        [0, 0, 4, 2, 0, 7, 1, 0, 0],
        [0, 0, 2, 0, 0, 0, 8, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 9, 0]],
    "Grid 30" :[
        [2, 0, 0, 1, 7, 0, 6, 0, 3],
        [0, 5, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 7, 9],
        [0, 0, 0, 0, 4, 0, 7, 0, 0],
        [0, 0, 0, 8, 0, 1, 0, 0, 0],
        [0, 0, 9, 0, 5, 0, 0, 0, 0],
        [3, 1, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 6, 0],
        [9, 0, 6, 0, 3, 7, 0, 0, 2]],
    "Grid 31" :[
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [8, 0, 0, 7, 0, 1, 0, 4, 0],
        [0, 4, 0, 0, 2, 0, 0, 3, 0],
        [3, 7, 4, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 3, 2, 1],
        [0, 1, 0, 0, 6, 0, 0, 5, 0],
        [0, 5, 0, 8, 0, 2, 0, 0, 6],
        [0, 8, 0, 0, 0, 0, 0, 0, 0]],
    "Grid 32" :[
        [0, 0, 0, 0, 0, 0, 0, 8, 5],
        [0, 0, 0, 2, 1, 0, 0, 0, 9],
        [9, 6, 0, 0, 8, 0, 1, 0, 0],
        [5, 0, 0, 8, 0, 0, 0, 1, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 9, 0, 0, 0, 6, 0, 0, 7],
        [0, 0, 9, 0, 7, 0, 0, 5, 2],
        [3, 0, 0, 0, 5, 4, 0, 0, 0],
        [4, 8, 0, 0, 0, 0, 0, 0, 0]],
    "Grid 33" :[
        [6, 0, 8, 0, 7, 0, 5, 0, 2],
        [0, 5, 0, 6, 0, 8, 0, 7, 0],
        [0, 0, 2, 0, 0, 0, 3, 0, 0],
        [5, 0, 0, 0, 9, 0, 0, 0, 6],
        [0, 4, 0, 3, 0, 2, 0, 5, 0],
        [8, 0, 0, 0, 5, 0, 0, 0, 3],
        [0, 0, 5, 0, 0, 0, 2, 0, 0],
        [0, 1, 0, 7, 0, 4, 0, 9, 0],
        [4, 0, 9, 0, 6, 0, 7, 0, 1]],
    "Grid 34" :[
        [0, 5, 0, 0, 1, 0, 0, 4, 0],
        [1, 0, 7, 0, 0, 0, 6, 0, 2],
        [0, 0, 0, 9, 0, 5, 0, 0, 0],
        [2, 0, 8, 0, 3, 0, 5, 0, 1],
        [0, 4, 0, 0, 7, 0, 0, 2, 0],
        [9, 0, 1, 0, 8, 0, 4, 0, 6],
        [0, 0, 0, 4, 0, 1, 0, 0, 0],
        [3, 0, 4, 0, 0, 0, 7, 0, 9],
        [0, 2, 0, 0, 6, 0, 0, 1, 0]],
    "Grid 35" :[
        [0, 5, 3, 0, 0, 0, 7, 9, 0],
        [0, 0, 9, 7, 5, 3, 4, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 9, 0, 0, 8, 0, 0, 1, 0],
        [0, 0, 0, 9, 0, 7, 0, 0, 0],
        [0, 8, 0, 0, 3, 0, 0, 7, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 7, 6, 4, 1, 2, 0, 0],
        [0, 6, 1, 0, 0, 0, 9, 4, 0]],
    "Grid 36" :[
        [0, 0, 6, 0, 8, 0, 3, 0, 0],
        [0, 4, 9, 0, 7, 0, 2, 5, 0],
        [0, 0, 0, 4, 0, 5, 0, 0, 0],
        [6, 0, 0, 3, 1, 7, 0, 0, 4],
        [0, 0, 7, 0, 0, 0, 8, 0, 0],
        [1, 0, 0, 8, 2, 6, 0, 0, 9],
        [0, 0, 0, 7, 0, 2, 0, 0, 0],
        [0, 7, 5, 0, 4, 0, 1, 9, 0],
        [0, 0, 3, 0, 9, 0, 6, 0, 0]],
    "Grid 37" :[
        [0, 0, 5, 0, 8, 0, 7, 0, 0],
        [7, 0, 0, 2, 0, 4, 0, 0, 5],
        [3, 2, 0, 0, 0, 0, 0, 8, 4],
        [0, 6, 0, 1, 0, 5, 0, 4, 0],
        [0, 0, 8, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 8, 0, 3, 0, 1, 0],
        [4, 5, 0, 0, 0, 0, 0, 9, 1],
        [6, 0, 0, 5, 0, 8, 0, 0, 7],
        [0, 0, 3, 0, 1, 0, 6, 0, 0]],
    "Grid 38" :[
        [0, 0, 0, 9, 0, 0, 8, 0, 0],
        [1, 2, 8, 0, 0, 6, 4, 0, 0],
        [0, 7, 0, 8, 0, 0, 0, 6, 0],
        [8, 0, 0, 4, 3, 0, 0, 0, 7],
        [5, 0, 0, 0, 0, 0, 0, 0, 9],
        [6, 0, 0, 0, 7, 9, 0, 0, 8],
        [0, 9, 0, 0, 0, 4, 0, 1, 0],
        [0, 0, 3, 6, 0, 0, 2, 8, 4],
        [0, 0, 1, 0, 0, 7, 0, 0, 0]],
    "Grid 39" :[
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 5, 4],
        [0, 9, 5, 0, 0, 0, 8, 1, 0],
        [0, 0, 9, 8, 0, 6, 4, 0, 0],
        [0, 2, 0, 4, 0, 3, 0, 6, 0],
        [0, 0, 6, 9, 0, 5, 1, 0, 0],
        [0, 1, 7, 0, 0, 0, 6, 2, 0],
        [4, 6, 0, 0, 0, 0, 0, 3, 8],
        [0, 0, 0, 0, 9, 0, 0, 0, 0]],
    "Grid 40" :[
        [0, 0, 0, 6, 0, 2, 0, 0, 0],
        [4, 0, 0, 0, 5, 0, 0, 0, 1],
        [0, 8, 5, 0, 1, 0, 6, 2, 0],
        [0, 3, 8, 2, 0, 6, 7, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 9, 4, 0, 7, 3, 5, 0],
        [0, 2, 6, 0, 4, 0, 5, 3, 0],
        [9, 0, 0, 0, 2, 0, 0, 0, 7],
        [0, 0, 0, 8, 0, 9, 0, 0, 0]],
    "Grid 41" :[
        [0, 0, 0, 9, 0, 0, 0, 0, 2],
        [0, 5, 0, 1, 2, 3, 4, 0, 0],
        [0, 3, 0, 0, 0, 0, 1, 6, 0],
        [9, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 5],
        [0, 9, 1, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 4, 3, 9, 0, 2, 0],
        [4, 0, 0, 0, 0, 7, 0, 0, 0]],
    "Grid 42" :[
        [3, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 7, 8, 5],
        [0, 0, 9, 0, 2, 0, 3, 0, 0],
        [0, 6, 0, 0, 9, 0, 0, 0, 0],
        [8, 0, 0, 3, 0, 2, 0, 0, 9],
        [0, 0, 0, 0, 4, 0, 0, 7, 0],
        [0, 0, 1, 0, 7, 0, 5, 0, 0],
        [4, 9, 5, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 2]],
    "Grid 43" :[
        [0, 0, 0, 1, 5, 8, 0, 0, 0],
        [0, 0, 2, 0, 6, 0, 8, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 4, 0],
        [0, 2, 7, 0, 3, 0, 5, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 6, 0, 8, 0, 7, 9, 0],
        [0, 5, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 4, 0, 7, 0, 1, 0, 0],
        [0, 0, 0, 3, 2, 5, 0, 0, 0]],
    "Grid 44" :[
        [0, 1, 0, 5, 0, 0, 2, 0, 0],
        [9, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 2, 0, 0, 8, 0, 3, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 7],
        [0, 0, 8, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 8, 0, 0, 0, 4],
        [0, 4, 0, 1, 0, 0, 7, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 6],
        [0, 0, 3, 0, 0, 4, 0, 5, 0]],
    "Grid 45" :[
        [0, 8, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 4, 6, 9, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 5, 9, 0, 4, 6, 0, 0],
        [0, 7, 0, 6, 0, 8, 0, 3, 0],
        [0, 0, 8, 5, 0, 2, 1, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 7, 8, 1, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 1, 0]],
    "Grid 46" :[
        [9, 0, 4, 2, 0, 0, 0, 0, 7],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 6, 5, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 9, 0],
        [0, 2, 0, 9, 0, 4, 0, 6, 0],
        [0, 4, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 6, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [3, 0, 0, 0, 0, 5, 7, 0, 2]],
    "Grid 47" :[
        [0, 0, 0, 7, 0, 0, 8, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 3, 1],
        [0, 4, 0, 0, 0, 2, 0, 0, 0],
        [0, 2, 4, 0, 7, 0, 0, 0, 0],
        [0, 1, 0, 0, 3, 0, 0, 8, 0],
        [0, 0, 0, 0, 6, 0, 2, 9, 0],
        [0, 0, 0, 8, 0, 0, 0, 7, 0],
        [8, 6, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 2, 0, 0, 6, 0, 0, 0]],
    "Grid 48" :[
        [0, 0, 1, 0, 0, 7, 0, 9, 0],
        [5, 9, 0, 0, 8, 0, 0, 0, 1],
        [0, 3, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 5, 8, 0, 0],
        [0, 5, 0, 0, 6, 0, 0, 2, 0],
        [0, 0, 4, 1, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 3, 0],
        [1, 0, 0, 0, 2, 0, 0, 7, 9],
        [0, 2, 0, 7, 0, 0, 4, 0, 0]],
    "Grid 49" :[
        [0, 0, 0, 0, 0, 3, 0, 1, 7],
        [0, 1, 5, 0, 0, 9, 0, 0, 8],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [5, 0, 0, 6, 0, 0, 3, 4, 0],
        [3, 4, 0, 2, 0, 0, 0, 0, 0]],
    "Grid 50" :[
        [3, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 7, 0, 0, 0],
        [7, 0, 6, 0, 3, 0, 5, 0, 0],
        [0, 7, 0, 0, 0, 9, 0, 8, 0],
        [9, 0, 0, 0, 2, 0, 0, 0, 4],
        [0, 1, 0, 8, 0, 0, 0, 5, 0],
        [0, 0, 9, 0, 4, 0, 3, 0, 1],
        [0, 0, 0, 7, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 6]],
}

from custom_modules.script_report import reporter

class Grid:
    '''        LABELING SCHEME

        c1 c2 c3  c4 c5 c6  c7 c8 c9
        ------------------------------
    r1 | _  _  _ | _  _  _ | _  _  _     
    r2 | _  b1 _ | _  b2 _ | _  b3 _ 
    r3 | _  _  _ | _  _  _ | _  _  _ 
        |-----------------------------
    r4 | _  _  _ | _  _  _ | _  _  _ 
    r5 | _  b4 _ | _  b5 _ | _  b6 _ 
    r6 | _  _  _ | _  _  _ | _  _  _ 
        |-----------------------------
    r7 | _  _  _ | _  _  _ | _  _  _ 
    r8 | _  b7 _ | _  b8 _ | _  b9 _ 
    r9 | _  _  _ | _  _  _ | _  _  _ 


    '''

    def __init__(self, puzzle: list[list[int]]) -> None:
        self.grid: list[list[Cell]] = self._initializeGrid(puzzle)

        self.value_grid: list[list[int]]
        self.getGridValues()

    def _initializeGrid(self, puzzle: list[list[int]]) -> list[list]: 
        grid: list[list[Cell]] = []

        for ri in range(len(puzzle)):   # Row Idx
            row: list[int] = puzzle[ri]
            new_row: list[Cell] = []

            for ci in range(len(row)):  # Colum Idx
                cell_value: int = row[ci]
                cell_idx = (ri, ci)
                new_row.append(Cell(idx= cell_idx, grid= self, value= cell_value))
            
            grid.append(new_row)

        return grid           

    def updatePossibleCellValues(self):
        for r in self.grid: # Row in grid
            for c in r:     # Cell in row
                c.getPossibleValues()
        
        self.getGridValues()

    def getGridValues(self) -> None:
        value_grid: list[list[int]] = []

        for r in self.grid:
            new_row: list[int] = []
            for c in r:
                new_row.append(c.value)
            
            value_grid.append(new_row)
        
        self.value_grid = value_grid

    def getPuzzleCode(self) -> int:
        return 123

class Cell:
    def __init__(self, idx: tuple[int, int], grid: Grid, value: int) -> None:
        self.idx:               tuple[int, int] = idx
        self.square:            int             = self._getSquareID()
        self.grid:              Grid            = grid
        self.value:             int             = value
        self.possible_values:   set[int]
    
        # If cell is initialized with a value, assume it is part of the puzzle problem
        if self.value != 0:
            self.locked = True
        else:
            self.locked = False

    def _getSquareID(self) -> int:
        row: int = self.idx[0]
        col: int = self.idx[1]

        # Offsets for division logic
        row += 3
        col += 3

        r_id = row // 3
        c_id = col // 3
        
        return r_id * c_id 

    def getPossibleValues(self) -> None:
        if self.value != 0:
            return

        values_in_sqr: list[int] = self._getCellSqr()
        values_in_col: list[int] = self._getCellCol()
        values_in_row: list[int] = self._getCellRow()

        all_neighbors: list[int] = []
        all_neighbors.extend(values_in_sqr)
        all_neighbors.extend(values_in_col)
        all_neighbors.extend(values_in_row)
        all_neighbors_set: set[int] = set(all_neighbors)

        possible_values_list: list = []

        for v in range(1, 10):
            if v in all_neighbors_set:
                continue

            possible_values_list.append(v)
        
        self.possible_values = set(possible_values_list)

        if len(self.possible_values) == 1:
            for value in self.possible_values:
                self.value = value
        
    
    def _getCellSqr(self) -> list[int]:
        sqr_values: list[int] = []

        for r in self.grid.grid:
            for c in r: 
                if c.square == self.square:
                    sqr_values.append(c.value)

        return sqr_values

    def _getCellCol(self) -> list[int]:
        col_values: list[int] = []

        for r in self.grid.grid:    # Row in grid
            col_values.append(r[self.idx[1]].value)

        return col_values

    def _getCellRow(self) -> list[int]:
        row_values: list[int] = []
        row: list[Cell] = self.grid.grid[self.idx[0]]

        for c in row:   # Cell in row
            row_values.append(c.value)

        return row_values

def solvePuzzle(grid: Grid) -> Grid:
    solving: bool = True
    old_state: list[list[int]] = grid.value_grid

    while solving:
        printPuzzle(grid)
        print('=============================')

        grid.updatePossibleCellValues()
        
        new_state: list[list[int]] = grid.value_grid

        if new_state == old_state:
            solving = False
        
        else:
            old_state = new_state
        
    

    return grid

def printPuzzle(grid: Grid) -> None:
    puzzle: list[list[Cell]] = grid.grid

    for r in puzzle:
        row: list[int] = []
        
        for c in r:
            row.append(c.value)
        
        print(row)

def main() -> int:
    grid_list: list[list[list[int]]] = list(sudoku_puzzles.values())
    list_of_codes: list[int] = []
    from time import time
    start = time()

    for g in grid_list:
        grid: Grid = Grid(puzzle= g)
        solved_puzzle: Grid = solvePuzzle(grid)
        print("=========FINISHED===========")
        printPuzzle(solved_puzzle)

        break       # ONLY DOING FIRST PUZZLE FOR TESTING ==============================

    print(time() - start)
    answer: int = sum(list_of_codes)
    return answer

main()

#reporter(main_function= main, run_count= 1)