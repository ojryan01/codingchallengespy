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

plots_eaten([4,5,3,5])       
    