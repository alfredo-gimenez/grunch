"""Grunch: A program that decides where to go to lunch"""

import sys
import lunchabase


def main():
    print "==== Grunch ===="

    # Create lunchabase
    my_lunchabase = lunchabase.lunchabase("nearby")
    my_lunchabase.add_place("Mexican", "Guadalajara")
    my_lunchabase.add_place("Mexican", "Chuys")
    my_lunchabase.add_place("Chinese", "Four Seasons Gourmet")
    my_lunchabase.add_place("Burgers", "Burgers & Brew")
    my_lunchabase.add_place("Burgers", "In-N-Out")

    # Reject categories
    print "Cuisine options are:"
    my_lunchabase.display_cuisines()

    print "Are there any cuisines you do NOT want?"
    reject_input = \
        raw_input("(Type a comma-separated list, e.g. Italian, Vegan): ")
    reject_list = str.split(reject_input, ',')

    for reject in reject_list:
        my_lunchabase.reject_cuisine(reject)

    # Choose a place
    satisfied = False

    while not satisfied:
        place = my_lunchabase.choose_place()
        response = raw_input("How about " + place.name + " [Y/n]? ")
        if response.strip().lower() == "y":
            break
        my_lunchabase.reject_place(place.name)

if __name__ == '__main__':
    sys.exit(main())
