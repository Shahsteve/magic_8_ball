#imported random module to access random functions.
import random

#This is the main function which asks users for  a question then reads
#the .txt file and generates a random line from the file.
def main():

    #Opens the file with the pre written lines to be read by the program. Opens in read only.
    f = open('responses.txt', 'r')

    for line in f:

        #User enters a question which can be answered in yes or no format.
        user_quest = input('Enter a yes/no question here or type exit to quit: ')


    #creates conditions for when the program should continue or when it should terminate.
        while user_quest != 'exit':

            #This is the display for the read in line from the responses.txt file.
            print(random.choice(list(open('responses.txt'))))

            #Prompts user to ask another question or terminate program.
            user_quest = input('Enter a yes/no question here or type exit to quit: ')

        else:

            #Display message before termination of program.
            print('Goodbye and thank you for playing!')

            #this function terminates the program.
            exit()

#This calls the main function to use.
if __name__ == '__main__':
    main()


