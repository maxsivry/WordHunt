#Max Ivry and Shea Gilmour
#program for creating word game with multiple players to find all words from random letter generator

#import random function
import random
#define main function that finds all scores (Shea Gilmour)
def main():

    #begin accumulators
    totalcomputer = 0
    round_count = 0
    totalplayer = 0
    #print opening message displaying rules
    print('''Hello! Welcome to Max and Shea's Word Hunt! Try to find as many three to five letter words as you can from five random letters!
You are allowed to use any letter more than once.''')

    #prompt user to start round or print results to outfile ('q' to quit)
    beginround = input("\nTo begin the round enter any letter, to quit and receive results enter 'q'.\n")
    beginround = beginround.lower()

    #while beginround does not equal 'q'
    while beginround != 'q':
        
        #call random_letters_function that displays eight random letters
        randomletters = random_letters_function()
        print(randomletters)
        
        #prompt user for list of words input, divided by commas, not case sensitive
        userinput = input("Go! Enter as many words as possible and separate them with commas. DO NOT INCLUDE SPACES IN BETWEEN YOUR WORDS, ONLY COMMA. When you are done hit enter.\n")
        #if space is found in input
        while ' ' in userinput:
            print("oops! no spaces allowed! try again:")
            print(randomletters)
            userinput = input()
            
        
        #assign words to list with multiple words
        if ',' in userinput:
            userwords = userinput.split(',')
        #if only one word or no words 
        elif ',' not in userinput:
            userwords = []
            userwords.append(userinput)
        
        #call determine_computer_score function with parameter of random letters, returns all possible words set and computer score
        (allpossiblewords, computer_score)= determine_computer_score(randomletters)
        
        #call determine_player_score function with parameters of user word set and all possible words set, returns player score
        player_score = determine_player_score(userwords, allpossiblewords)
        #call round_results function that takes parameters of user word set and all possible words set, displays words players missed to screen
        round_results(userwords,allpossiblewords)
        #display computer score and player score for round to screen
        
        print("The computer's score for this round is:", computer_score)
        print("Your round score is:",player_score)
    
        #add score to player score accumulator
        totalcomputer += computer_score
        totalplayer += player_score

        #add one to round count
        round_count +=1
        #re prompt user to start round or print results to outfile ('' to play or 'q' to quit)
        print('\n')
        beginround = input("To begin the round enter any letter, to quit and receive results enter 'q'.")
        beginround = beginround.lower()

    #if beginround equals 'q'
    if beginround == 'q':
        print("View the game results in final_results.txt! Thank you for playing hehe! :)")
        #call final_results function that takes parameters computer score, player score, and round count and prints results to outfile
        final_results(totalcomputer,totalplayer,round_count)


#define random_letters_function that returns eight random letters to user from alphabet (Shea)
def random_letters_function():
    #list of all letters and vowel list
    alphabetlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vowellist = ['a','e','i','o','u']
    #number of random letters returned
    NUMOFLETTERS = 5
    lengthofalphabet = 25
    #create list of random letters
    randomletters = []
    #for loop that iterates once per each 5 letters
    for i in range(NUMOFLETTERS):
        #random number that corresponds with letter in alphabet
        index = random.randint(0,lengthofalphabet)
        #pop the random corresponding letter from alphabet
        letter = alphabetlist.pop(index)
        #length of list decreases by one
        lengthofalphabet -= 1
        #append letter to randomletters list
        randomletters.append(letter)
    #if list has no vowel
    if len(set(vowellist).intersection(set(randomletters))) == 0:
        #random number in randomletters list
        index = random.randint(0,NUMOFLETTERS-1)
        #remove random consenant from random letters list
        randomletters.pop(index)
        #add vowel
        randomletters.append(vowellist[index])
        
    #return random letters list
    return(randomletters)

#define determine_computer_score function that reads infile, determines all possible words that can be created from random letters, and returns set of all possible words and corresponding score (Max) 
def determine_computer_score(randomletters):
    #begin accumulator for computer score
    computer_score = 0
    #create list of all possible words
    allpossiblewords = []
    #make random letters into set
    randomletters = set(randomletters)
    #try open three letter word file in read mode
    try:
        infile = open('three_letter_words.txt','r') 
        #read file, assign to list
        file = infile.read().rstrip()
        threeletterwords = file.split()
    #if file does not open
    except:
        print("Error opening file!")
        threeletterwords = []
    #for each word in list
    for i in threeletterwords:
        #change word into set of letters
        word = set(i)

        #if the letters are found in random letters
        if (word.issubset(randomletters)):
            #add to all possible words list
            allpossiblewords.append(i)
            #add to computer score by 1
            computer_score += 1
    #close three_letter_words file
    infile.close()
    
    #for four letter words
    #open four letter word file in read mode
    infile = open('four_letter_words.txt','r')
    #try read file, assign to list
    try:
        file = infile.read().rstrip()
        fourletterwords = file.split(',')
    #if file does not open
    except:
        print("Error opening file!")
        fourletterwords = []
    #for each word in list
    for i in fourletterwords:
        #delete all spaces, make each word into set
        word =i.replace(' ','')
        #if the letters are found in random letters
        if (set(word).issubset(randomletters)):
            #add to all possible words list
            allpossiblewords.append(word)
            #add to computer score by 1
            computer_score += 1
    #close file
    infile.close()

    #for five letter words
    #open five letter word file in read mode
    infile = open('five_letter_words.txt','r')
    #try read file, assign to list
    try:
        file = infile.read().rstrip()
        fiveletterwords = file.split(',')
    #if file does not open
    except:
        print("Error opening file!")
        fiveletterwords = []
    #for each word in list
    for i in fiveletterwords:
        #delete all spaces, make each word into set
        word =i.replace(' ','')
        #if the letters are found in random letters
        if (set(word).issubset(randomletters)):
            #add to all possible words list
            allpossiblewords.append(word)
            #add to computer score by 1
            computer_score += 1
    #close file
    infile.close()
    
    #return all possible words and computer score
    return(allpossiblewords, computer_score)

#define determine_player_score function that takes in users words and random letters, determines how many words player correctly identified, and returns player score, (Max)
def determine_player_score(userwords, allpossiblewords):
    #begin player score accumulator
    player_score = 0
    #for all words that userinputs
    for word in userwords:
        #not case sensitive
        word = word.lower()
        #if word is in the list of possible words add to score
        if word in allpossiblewords:
            player_score += 1
    #return player score
    return(player_score)

#define round_results function that takes in users words and allpossiblewords, displays words players correctly identified and words players missed to screeen (not value returning) Max
def round_results(userwords, allpossiblewords):
    correctwords = []
    for word in userwords:
        word = word.lower()
        if word in allpossiblewords:
            correctwords.append(word)
    print("The words that you got correct were:")
    for word in correctwords:
        print(word)
    print("The words you missed were:")
    for word in allpossiblewords:
        if word not in userwords:
            print(word)
          
#define final_results function that takes in computer score, player score, and round count, and prints results to outfile (Shea)
def final_results(totalcomputer, totalplayer, round_count):
    #open file
    outfile = open('final_results.txt','w')
    #write total computer score
    outfile.write("Total computer score: ")
    totalcomputer = str(totalcomputer)
    outfile.write(totalcomputer+'\n')
    #write total player score
    outfile.write("Total player score: ")
    totalplayer = str(totalplayer)
    outfile.write(totalplayer+'\n')
    #write total round count
    outfile.write("Total round count ")
    round_count = str(round_count)
    outfile.write(round_count+'\n')
    #close file
    outfile.close()

#call main function
main()



    
