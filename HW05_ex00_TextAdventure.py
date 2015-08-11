#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys

# Body

def infinite_stairway_room(user, count=0):
    # print user + " walks through the door to see a dimly lit hallway."
    print "At the end of the hallway is a", count * 'long', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print user + ' takes the stairs'
        if (count > 0):
            print "but she's not happy about it"
        infinite_stairway_room(user, count + 1)
    if next == "teleport":
        gold_room(user)


def gold_room(user):
    print "This room is full of gold.  How much does " + user + " take?"
    next = raw_input("> ")
    if "0" in next or "1" in next or "1" in next or "2" in next or "3" in next or "4" in next or "5" in next or "6" in next or "7" in next or "8" in next or "9" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, " + user + " is not greedy, you win!"
        exit(0)
    else:
        dead(user + "," + "you greedy bastard!")


def bear_room(user):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is " + user + " going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or "honey":
            dead("The bear looks at " + user + " then slaps their face off.")
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. " + user + " can go through it now."
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews " + user + "'s" " leg off.")
        elif next == ("open" or "door") and bear_moved:
            gold_room(user)
        else:
            print "I got no idea what that means."


def cthulhu_room(user):
    print "Here" + user + " sees the great evil Cthulhu."
    print "He, it, whatever stares at" + user + "and " + user + " goes insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    user = sys.argv[1]
    # START the TextAdventure game
    print user + " is in a dark room."
    print "There is a door to your right and left, and a set of stairs in front of you."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room(user)
    elif next == "right":
        cthulhu_room(user)
    elif next == "stairs":
        infinite_stairway_room(user, count=0)
    else:
        dead(user + " stumbles around the room until they starve.")

if __name__ == '__main__':
    main()
