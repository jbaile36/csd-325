#Joshua Bailey 3/22/2026 Module 1 Assignment 1_3
#This program runs through the classic song 99 bottles of beer,
#removing a bottle from the count until bottles hits 0.
#Where it prompts that there is no more beer and more should be bought.

#*Note* I did not want the user to be able to enter an absurdly large
#number and allow the program to run idenfinitely, so I added input
#sanitation to limit input to intergers between 1 and 99.

#Count function.
def count(bottles):
    #Checks to see if there are bottles.
    while bottles > 0:
        #Checks if there is 1 bottle, applies correct lyric.
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            #Removes a bottle from count.
            bottles -= 1

            #Checks if there is 1 bottle, applies correct lyric.
            if bottles == 1:
                print("Take one down, pass it around, 1 bottle of beer on the wall")
            else:
                print(f"Take one down, pass it around, {bottles} bottles of beer on the wall")
            continue
        bottles -= 1
#Main input function with sanitation.
def main():

    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? (1-99): "))
            #Checks if the number entered is between 1 and 99.
            if 1 <= bottles <= 99:
                break
            print("Please enter a whole number between 1 and 99.")
        #If input is not a whole number, shows error, and asks for a whole numer.
        except ValueError:
            print("Invalid Input. Please input a whole number between 1 and 99.")
    
    #Starts count function.
    count(bottles)

    #Prompts to buy more beer when count ends.
    print("You should probably buy more beer!")

#Starts Main function
main()


