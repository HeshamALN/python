print("Mad libs where libs get mad.\nStart below:\n")

time = input('Enter a number from 1 to 12: ')
item = input('Enter a noun (plural): ')
name = input('Enter a name: ')
sentence = input('Enter any sentence: ')
action = input('Enter a verb: ')


name = name.title()
sentence = sentence.upper()



print("It was {} o'clock when I heard a knock at the door." .format(time))
print("I opened the door and there was a box full of {} with a note saying From Mr.{}" .format(item, name))
print("Just as I closed the door I heard a scream {}" .format(sentence))
print("I froze in place and all I could do was {}" .format(action))