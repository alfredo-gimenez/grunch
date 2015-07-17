"""PyLunch: A program to decide where to go to lunch, written in Python"""

import sys
import lunchabase


def main():
    print "==== PyLunch ===="

    # Create lunchabase
    my_lunchabase = lunchabase.lunchabase("nearby")
    my_lunchabase.add_place("Mexican", "Guadalajara")
    my_lunchabase.add_place("Mexican", "Chuys")
    my_lunchabase.add_place("Chinese", "Four Seasons Gourmet")
    my_lunchabase.add_place("Burgers", "Burgers & Brew")
    my_lunchabase.add_place("Burgers", "In-N-Out")

    # Reject categories
    my_lunchabase.display_cuisines()

    # Choose a place
    place = my_lunchabase.choose_place()

    print "You should go to " + place.name + "!"

if __name__ == '__main__':
    sys.exit(main())
