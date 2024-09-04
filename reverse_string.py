'''
Name: Jeffrey Moniz
Project: reverse words in a string
Description: This is a leetcode interview question in which the participant must
reverse the words in a string, for example 'the sky is blue' turns to 'blue is sky the'
'''

#create a class called solutions
class Solution(object):
    #create a function called reverseWords which takes a string and returns a new string
    def reverseWords(self, s):
        #create a stack from the string
        stack = s.split()
        reversed_word = []
        final = ''
        #create a while loop which takes the last word and adds it to a new list known as reversed_word
        while stack != []:
            w = stack.pop()
            reversed_word.append(w)
        #create a for loop which converts the list reversed_word into a string called final
        for i in reversed_word:
            final += str(i)
            final += ' '
        #removes any extra spaces at the end of the string
        if final[len(final)-1] == ' ':
            final = final[0:len(final)-1]
        #returns a string of the reversed word
        return final