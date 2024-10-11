# asking the user for the text
submitted_text = input("input any form of text, could be anything you wish! ").lower()
#asking the user for letters that can be found within their text
letter1 = input("give the program a letter that can be found in the text you provided ").lower()
letter2 = input("give the program another letter that can be found in the text you provided ").lower()
letter3 = input("give the program another letter that can be found in the text you provided ").lower()
#counting each time the letter they gave us actually appears
count1 = submitted_text.lower().count(letter1)
count2 = submitted_text.lower().count(letter2)
count3 = submitted_text.lower().count(letter3)
#printing each time the letter appears
print("your first letter has appeared " + str(count1) + " times")
print("your second letter has appeared " + str(count2) + " times")
print("your third letter has appeared " + str(count3) + " times")
#getting the wordcount of the text by turning it into a list
text_list = submitted_text.split()
word_count = len(text_list)
print("There are " + str(word_count) + " words in the text submitted")
#getting the first and last letters of the text the user has given us
firstletter = submitted_text[0]
lastletter = submitted_text[-1]
print("the first letter of the text is " + firstletter)
print("the last letter of the text is " + lastletter)
#reversing the text (this is what gave me a hard time but i get it now)
reversed_list = text_list [::-1]
reversed_text = ' '.join(reversed_list)
print("if this were reversed it would look like: " + reversed_text)
#checking for the word "Python" in the text provided
HasPython = "python" in submitted_text.lower()
#dictionary for the result (i kinda understand these now)
PythonResponse = {
    True: "the text contains the word <<Python>>!",
    False: "the text doesn't contain the word <<python>> :("
}
