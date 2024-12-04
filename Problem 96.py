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
        [0, 0, 5, 0, 1, 0, 3, 0, 0] 
    ], 
    "Grid 02": [
        [2, 0, 0, 0, 8, 0, 3, 0, 0],
        [0, 6, 0, 0, 7, 0, 0, 8, 4],
        [0, 3, 0, 5, 0, 0, 2, 0, 9],
        [0, 0, 0, 1, 0, 5, 4, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 2, 7, 0, 6, 0, 0, 0],
        [3, 0, 1, 0, 0, 7, 0, 4, 0],
        [7, 2, 0, 0, 4, 0, 0, 6, 0],
        [0, 0, 4, 0, 1, 0, 0, 0, 3]
    ],
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

def getCellSqr(cell_idx: tuple[int, int], grid: list[list[int]]) -> list[int]:
    sqr_values: list[int] = []

    # To-Do

    return sqr_values

def getCellCol(cell_idx: tuple[int, int], grid: list[list[int]]) -> list[int]:
    col_values: list[int] = []

    # To-Do

    return col_values

def getCellRow(cell_idx: tuple[int, int], grid: list[list[int]]) -> list[int]:
    row_values: list[int] = []

    # To-Do

    return row_values

def getCellOptions(grid: list[list[int]]) -> dict[tuple[int, int], list[int]]:
    cell_option_dict: dict[tuple[int, int], list[int]] = dict({})       # (row_idx, col_idx): [1, 2, 3, ...]

    # To-Do

    return cell_option_dict

def solvePuzzle(grid: list[list[int]]) -> list[list[int]]:
    
    # To-Do

    return [[1]]

def getPuzzleCode(grid: list[list[int]]) -> int:

    # To-Do

    return 0

def main() -> int:
    grid_list: list[list[list[int]]] = list(sudoku_puzzles.values())
    list_of_codes: list[int] = []

    for puzzle in grid_list:
        solution: list[list[int]] = solvePuzzle(grid= puzzle)
        puzzle_code: int = getPuzzleCode(grid= solution)
        list_of_codes.append(puzzle_code)

    answer: int = sum(list_of_codes)
    return answer

reporter(main_function= main)