from Stack import Stack

def solveMaze(maze, startX, startY):
    s = Stack()
    coord = [startX, startY]
    s.push(coord) 
    i = 1
    while s.isEmpty() is False:
        c = s.peek()
        if  maze[c[0]][c[1]] == " ":
            maze[c[0]][c[1]] = i 
            i+= 1
        if c[0]-1 >= 0 and maze[c[0]-1][c[1]] == "G":
            return True
        if c[1]-1 >= 0 and maze[c[0]][c[1]-1] == "G":
            return True 
        if c[0]+1 < len(maze) and maze[c[0]+1][c[1]] == "G":
            return True 
        if c[1]+1 < len(maze[c[0]]) and maze[c[0]][c[1]+1] == "G":
            return True   
       
        if c[0]+1 < len(maze) and maze[c[0]+1][c[1]] == " ":
            s.push([c[0]+1, c[1]])
            continue
        if c[0]-1 >= 0 and maze[c[0]-1][c[1]] == " ":
            s.push([c[0]-1, c[1]])
            continue
        if c[1]+1 < len(maze[c[0]]) and maze[c[0]][c[1]+1] == " ":
            s.push([c[0], c[1]+1])    
            continue
        if c[1]-1 >= 0 and maze[c[0]][c[1]-1] == " ":
            s.push([c[0], c[1]-1])
            continue 
        s.pop()
    return False
#         printMaze(maze)

# def printMaze(maze):
#  	for row in range(len(maze)):
#  		for col in range(len(maze[0])):
#  			print("|{:<2}".format(maze[row][col]), sep='',end='')
#  		print("|")
		
	



