# Advent of Code 2022, Day 12, Part 1
# https://adventofcode.com/2022/day/12

from collections import deque

graph = [list(i) for i in open("Day 12/in.txt").read().splitlines()] # Testinput
#graph = [list(i) for i in open("Day 12/input.txt").read().splitlines()]

ord_graph = [[(ord(character) - 96) for character in sublist] for sublist in graph]

for r, row in enumerate(ord_graph):
    for c, height_info in enumerate(row):
        if height_info == (ord("S") - 96):
            startRow = r
            startColumn = c
            ord_graph[r][c] = (ord("a") - 96)
        elif height_info == (ord("E") - 96):
            endRow = r
            endColumn = c
            ord_graph[r][c] = (ord("z") - 96)

queue = deque()

start = (0, startRow, startColumn)
queue.append(start)

visited = {(startRow, startColumn)}

while queue:
    distance, row, column = queue.popleft()
    for nextRow, nextColumn in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
        if (nextRow < 0 or nextColumn < 0 
           or nextRow >= len(ord_graph) 
           or nextColumn >= len(ord_graph[0])):
            continue
        if (nextRow, nextColumn) in visited:
            continue
        if ord_graph[nextRow][nextColumn] - ord_graph[row][column] > 1:
            continue
        if (nextRow, nextColumn) == (endRow, endColumn):
            print(distance+1)
        queue.append((distance + 1, nextRow, nextColumn))
        visited.add((nextRow, nextColumn))
