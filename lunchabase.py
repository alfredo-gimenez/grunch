import sys
import random


class lunchplace:
    """ A single lunch option """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class lunchcuisine:
    """ A collection of lunch options from one type of cuisine """

    def __init__(self, name):
        self.name = name
        self.places = {}

    def __str__(self):
        return self.name

    def add_place(self, place_name):
        place_key = place_name.strip().lower()
        self.places[place_key] = lunchplace(place_name)

    def reject_place(self, place_name):
        place_key = place_name.strip().lower()
        if place_key in self.places:
            self.places.pop(place_key)


class lunchabase:
    """ A collection of available lunch cuisines """

    def __init__(self, name):
        self.name = name
        self.cuisines = {}

    def add_cuisine(self, cuisine_name):
        cuisine_key = cuisine_name.strip().lower()
        if cuisine_key not in self.cuisines:
            self.cuisines[cuisine_key] = lunchcuisine(cuisine_name)
        return self.cuisines[cuisine_key]

    def add_place(self, cuisine_name, place_name):
        place_key = place_name.strip().lower()
        cuisine = self.add_cuisine(cuisine_name)
        cuisine.places[place_key] = lunchplace(place_name)

    def reject_cuisine(self, cuisine_name):
        cuisine_key = cuisine_name.strip().lower()
        if cuisine_key in self.cuisines:
            self.cuisines.pop(cuisine_key)
            return

    def reject_place(self, place_name):
        for cuisine_key, cuisine in self.cuisines.iteritems():
            cuisine.reject_place(place_name)
            if len(cuisine.places) == 0:
                self.reject_cuisine(cuisine_key)
                return

    def choose_cuisine(self):
        return self.cuisines[random.choice(self.cuisines.keys())]

    def choose_place(self):
        if len(self.cuisines) == 0:
            print "There is no pleasing you, is there?"
            sys.exit(1)
        cuisine = self.choose_cuisine()
        return cuisine.places[random.choice(cuisine.places.keys())]

    def display_cuisines(self):
        option = 0
        for cuisine in self.cuisines.itervalues():
            option = option+1
            print str(option) + ". " + cuisine.name

    def display_tree(self):
        for cuisine in self.cuisines.itervalues():
            print cuisine
            for place in cuisine.places.itervalues():
                print "--- ",
                print place
