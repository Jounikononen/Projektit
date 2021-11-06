'''
Maze -task
Jouni Kononen
'''

file = 'maze-task-first.txt'    #set file here
a = []          #temporary list
maze = []       #file in an easier to read format
index1 = 0      #helps to find the coordinates
index2 = 0      #helps to find the coordinates
end = []        #coordinates for exits

#open the file, edit and find the coordinates
with open(file) as f:
        while True:
                c = f.read(1)   #Read the file character by character
                if not c:       #break if no more characters are found    
                        break   
                if c == "\n":   #if character '\n' 
                        l = len(a)      #Read the line length
                        a = [sub.replace(" ", "0") for sub in a]        #Replace spaces
                        a = [sub.replace("#", "1") for sub in a]        #Replace blocks
                        for i in a:
                                if i == "E":    #If exit
                                        #Search for coordinates
                                        numbers = index2, index1        #Coordinates to the exit
                                        end.append(numbers)             #Set coordinates to end[]
                                if i == "^":    #If starting position
                                        start = index2, index1          #Coordinates to start
                                index1 += 1     #This helps to find the coordinate
                        a = [sub.replace("E", "0") for sub in a]        #Replace exits   
                        a = [sub.replace("^", "0") for sub in a]        #Replace starting position
                        for i in range(0, l):           #Read line
                                a[i] = int(a[i])        #Data type to integer
                        
                        maze.append(a[0:l])     #Append data to Maze[]
                        print(a)     
                        a.clear()               #Clear a [] for the next line
                        index2 += 1             #This helps to find the coordinate
                        index1 = 0              #This helps to find the coordinate
                if c != "\n":
                        a.append(c)             #If other than '\n', append data to a[]
print("")
print("-----number of exits: ", len(end),"-----(",end,")")
print("-----Pentti can be found: ",start)


#Create maze2 full of zeros (except start. Pentti is standing there at the moment)
maze2 = []
for i in range(len(maze)):      #the same size as the first maze
    maze2.append([])            
    for j in range(len(maze[i])):
        maze2[-1].append(0)
i = start[0]    #coordinate
p = start[1]    #coordinate
maze2[i][p] = 1 #set start


move = 0
x = range(len(maze2))
y = range(len(maze2[i]))

''' here I tried to make some more sensible solution to the exits...
v = 0
for x in range(len(end)):
        maze2[end[v][0]][end[v][1]]
        v += 1
'''
#Scanning maze. 
#If Pentti visits the exit, the scan will end
while maze2[end[0][0]][end[0][1]] == 0: #this would need a better solution due to several exits
        move += 1       #Pentti stands here and sets off
        for i in x:     
                for p in y:
                        '''
                        here are many if-statements that Pentti can use to navigate
                        '''
                        if maze2[i][p] == move: #Scanning
                                if i > 0 and maze2[i-1][p] == 0 and maze[i-1][p] == 0: #Pentti moves up if possible
                                        maze2[i-1][p] = move + 1        #Pentti takes a step
                                if i < len(maze2)-1 and maze2[i+1][p] == 0 and maze[i+1][p] == 0: #Pentti moves down if possible
                                        maze2[i+1][p] = move + 1        #Pentti takes a step
                                if p > 0 and maze2[i][p-1] == 0 and maze[i][p-1] == 0: #Pentti moves left if possible
                                         maze2[i][p-1] = move + 1       #Pentti takes a step
                                if p < len(maze2[i])-1 and maze2[i][p+1] == 0 and maze[i][p+1] == 0: #Pentti moves right if possible
                                        maze2[i][p+1] = move + 1        #Pentti takes a step

print("-----Pentti walked ", move, " steps to exit (only for the first exit because of problems with exits on line 72)") #Pentti has found the first exit
print("")

#here the shortest route to the exit
i = end[0][0]   #Coordinate
p = end[0][1]   #Coordinate
x = maze2[i][p] #Exit
route = [(i,p)] 
while x > 1:    #While no starting point
                #here are many if statements to find the shortest route
        if i > 0 and maze2[i - 1][p] == x-1:    
                i, p = i-1, p           #Up
                route.append((i, p))    #Append coordinates
                x-=1
        elif i < len(maze2) - 1 and maze2[i + 1][p] == x-1:
                i, p = i+1, p           #down
                route.append((i, p))    #Append coordinates
                x-=1
        elif p > 0 and maze2[i][p - 1] == x-1:
                i, p = i, p-1           #left
                route.append((i, p))    #Append coordinates
                x-=1
        elif p < len(maze2[i]) - 1 and maze2[i][p + 1] == x-1:
                i, p = i, p+1           #right
                route.append((i, p))    #Append coordinates
                x -= 1
print(route) #the shortest route (Only coordinates)

#little visualization
