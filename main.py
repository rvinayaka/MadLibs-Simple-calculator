from tkinter import *       #? import tkinter module


#% Creating a display window
root = Tk()                                 #? initializing window 
root.geometry('300x300')                    #? set the width and height
root.title('FourPaws- MadLibs Generator')   #? title 
Label(root, text='Mad Libs Generator \n Have Fun!!', font = 'arial 20 bold').pack()     #? organized widget in block
Label(root, text = 'Click Any One: ', font = 'arial 15 bold').place(x = 40, y = 80)         #? place widget in specific postion


#% Define function
def madlib1():
    animals = input('Enter an animal name: ')
    profession = input('Enter profession: ')
    cloth = input('Enter type of piece of cloth: ')
    things = input('Enter things: ')
    name = input('Enter any name: ')
    place = input('Enter a place name: ')
    verb = input('Enter verb in ing form: ')
    food = input('Enter food name: ')
    print('Say!!' + food + ', the photographer said as the camera flashed! ' 
          + name + ' and I had gone to ' + place 
          +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' 
          + animals + ' pretending to be a ' + profession 
          + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' 
          + things + ' wearing ' + cloth + ' and ' + verb + ' -- exactly what I had in mind')
    

def madlib2():
    adjective = input('Enter an adjective: ')
    color = input('Enter a color name: ')
    thing = input('Enter a thing you wanted: ')
    place = input('Enter a place name you wanted to go: ')
    person = input('Enter a person\'s name: ')
    adjective2 = input('Enter an adjective: ')
    insect = input('Enter an insect name: ')
    food = input('Enter a food name: ')
    verb = input('Enter a verb: ')

    print('Last night I dreamed I was a ' + adjective + ' butterfly with ' 
          + color + ' splocthes that looked like '+ thing + ' .I flew to ' + place 
          + ' with my bestfriend and '+person+ ' who was a '+ adjective2 + ' ' + insect 
          +' .We ate some ' + food + ' when we got there and then decided to '+ verb 
          + ' and the dream ended when I said-- lets ' + verb + '.')
    

def madlib3():
    person = input('Enter a person\'s name: ')
    color = input('Enter a color name: ')
    foods = input('Enter many foods name: ')
    adjective = input('Enter an adjective: ')
    thing = input('Enter a thing you wanted: ')
    place = input('Enter a place name you wanted to go: ')
    verb = input('Enter a verb: ')
    adverb = input('Enter a adverb: ')
    food = input('Enter a food name: ')
    things = input('Enter more things you wanted: ')

    print('Today we picked apple from '+ person 
          + "'s Orchard. I had no idea there were so many different varieties of apples. I ate " 
          + color + ' apples straight off the tree that tested like ' + foods 
          + '. Then there was a '+ adjective + ' apple that looked like a ' + thing 
          + '.When our bag were full, we went on a free hay ride to '+ place 
          + ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb 
          + '. I can hardly wait to get home and cook with the apples. We are going to make appple '
          + food + ' and '+ things +' pies!.') 
    

#% Define buttons
#? Button() widget used to display buttons on tkinter window
Button(root, text = 'The Photographer', font = 'arial 15', command = madlib1, bg = 'ghost white').place(x = 60, y = 120)
Button(root, text = 'Apple and Apple', font = 'arial 15', command = madlib3, bg = 'ghost white').place(x = 70, y = 180)
Button(root, text = 'The Butterfly', font = 'arial 15', command = madlib2, bg = 'ghost white').place(x = 80, y = 240)

root.mainloop()         #? used when we want to run our program

