#Levret Munch
#Baby leverets can only eat a total of 10 carrots, and not any more.
#Write a function that takes in an array of integers that represent the number of carrots in each plot in a garden trail. 
#This function should return the number of plots a baby leveret will eat, only counting plots that can be eaten in completion. 
# (A leveret can’t eat part of a plot.)


def plots_eaten(garden):

        max_carrots = 10

        carrot_count = 0

        plots_eaten = 0

        for plot in garden:

            if carrot_count < max_carrots:
                if plot < max_carrots:
                    
                    if carrot_count + plot < max_carrots:
                        carrot_count = carrot_count + plot 
                        plots_eaten = plots_eaten + 1
                        print("carrot count: " + str(carrot_count))
                        print("plots_eaten: " + str(plots_eaten))
                    else: 
                        print("Stop, too many!")
                        break
            else:
                print(plots_eaten)
                return plots_eaten

#plots_eaten([4,5,3,5])  


#Leveret Level 2
#Start at D2
#Then looks for largest number starting left, up, right, down
#if there is a tie, the first number searched is selected
#If all neighboring numbers are zero, exit program

#Write a function that takes in a 2-dimensional array that represents garden plots and the amount of carrots each plot contains. 
#This function should return the number of carrots eaten by Baby Leveret.


plot = [
    #A  B  C  D  E  F  G 
#1
    [2, 3, 1, 4, 2, 2, 3 ], 
#2
    [2, 3, 0, 4, 0, 3, 0 ],
#3
    [1, 7, 0, 2, 1, 2, 3 ],
#4  
    [9, 3, 0, 4, 2, 0, 3 ]
]

print("Initial carrot count: " + str(plot[1][3]))

#initial conditions

column = 1

row = 3

carrot_count = plot[1][3]

for i in plot:

    #check left

    west = plot[column][row-1]

    print("Number to the west: " + str(west))

    #check up

    north = plot[column-1][row]

    print("Number to the north: " + str(north))

    #check right

    east = plot[column][row+1]

    print("Number to the east: " + str(east))

    #check down

    south = plot[column+1][row]

    print("Number to the south: " + str(south))

    #if west is a max, west is the destination:
    if west >= north and west >= east and west >= south:       
        plot[column][row] = 0
        column = column
        row = row -1
        direction = "West"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if the north is a max and it is not equal to west, north is the destination
    elif north >= west and north >= east and north >= south and north != west:
        plot[column][row] = 0
        column = column - 1
        row = row
        direction = "North"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if the north is a max and it is equal to west, west is the destination
    elif north >= east and north >= south and north == west:
        plot[column][row] = 0
        column = column
        row = row -1
        direction = "West"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if east is a max and it is not equal to west or north, then east is the destination
    elif east >= west and east >= north and east >= south and east != west and east != north:
        plot[column][row] = 0
        column = column
        row = row + 1
        direction = "East"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if east is a max and it equal to west, then west is the destination
    elif east >= west and east >= north and east >= south and east == west:
        plot[column][row] = 0
        column = column
        row = row -1
        direction = "West"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if east is a max and it is equal to north but not west, then north is the destination
    elif east >= west and east >= north and east >= south and east != west and east == north:
        plot[column][row] = 0
        column = column - 1
        row = row
        direction = "North"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if south is a max and it is not equal to east, north or west, then south is the destination
    elif south > west and south > east and south > north and south != west and south != north and south != east:
        plot[column][row] = 0
        column = column + 1
        row = row
        direction = "South"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if south is a max and it is equal to west, then west is the destination
    elif south >= west and south >= east and south >= north and south == west:
        plot[column][row] = 0
        column = column
        row = row -1
        direction = "West"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if south is a max and it is equal to north but not west, then north is the destination
    elif south > west and south >= east and south >= north and south == north:
        plot[column][row] = 0
        column = column - 1
        row = row
        direction = "North"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if south is a max and it is equal to east but not west or north, then east is the destination
    elif south > west and south > north and south == east:
        plot[column][row] = 0
        column = column
        row = row + 1
        direction = "East"
        print("Leveret travels: " + direction)
        print("Number of carrots at new location: " + str(plot[column][row]))
        carrot_count = carrot_count + plot[column][row]
        print("New carrot count: " + str(carrot_count))

    #if all destinations are zero, exit the game
    elif west == 0 and north == 0 and east == 0 and south == 0:
        print('Time to take a nap!')
        break
    
    





    