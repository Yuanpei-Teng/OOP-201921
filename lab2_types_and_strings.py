#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence
        print(message[0] + ' ' + message[-1])


        # use slice notation
        print(message[0:len(message)])
        print(message[0::len(message)-1])



        # escaping a character
        print(message[0:3] + message[4:len(message)])


        # find all a's in the input word and count how many there are
        print(message.count('a',0,len(message)))


        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        print(message.replace('a','-'))


        # printing only characters at even index positions
        even_char = message[::2]
        print(even_char)


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        message_li = list(message)
        print(list(message_li))


        # append a new element to the list and print
        message_li.append('z')
        print(message_li)

        # remove from the list in 3 ways

        #way 1
        del message_li[2]
        print(message_li)

        #way 2
        my_del = message_li.pop(3)
        print(message_li)

        #way 3
        message_li.remove('a')
        print(message_li)



        # check if the word cake is in your input list
        seperator = '-'
        message_li2 = seperator.join(message_li)
        print('c-a-k-e'in message_li2)

        # reverse the items in the list and print
        print(list(reversed(message_li)))

        # reverse the list with the slicing trick
        print(message_li[::-1])

        # print the list 3 times by using multiplication
        print(message_li*3)


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()
haha