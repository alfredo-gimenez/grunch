import random


class lunchplace:
    """ A single lunch option """
    available = True

    def __init__(self, name):
        self.name = name


class lunchcuisine:
    """ A collection of lunch options from one type of cuisine """
    places = {}
    available = True

    def __init__(self, name):
        self.name = name

    def add_place(self, place):
        self.places[place] = lunchplace(place)


class lunchabase:
    """ A collection of available lunch cuisines """
    cuisines = {}

    def __init__(self, name):
        self.name = name

    def add_place(self, cuisine, place):
        if cuisine not in self.cuisines:
            self.cuisines[cuisine] = lunchcuisine(cuisine)
        if place not in self.cuisines[cuisine].places:
            self.cuisines[cuisine].places[place] = lunchplace(place)

    def reject_cuisine(self, cuisine):
        if cuisine in self.cuisines:
            self.cuisines[cuisine].available = False

    def reject_place(self, cuisine, place):
        if cuisine in self.cuisines and place in self.cuisines[cuisine].places:
            self.cuisines[cuisine].places[place].available = False

    def choose_cuisine(self):
        valid = False
        while not valid:
            choice = random.choice(self.cuisines.keys())
            valid = self.cuisines[choice].available
        return self.cuisines[choice]

    def choose_place(self):
        valid = False
        while not valid:
            cuisine = self.choose_cuisine()
            choice = random.choice(cuisine.places.keys())
            valid = cuisine.places[choice].available
        return cuisine.places[choice]

    def display_cuisines(self):
        print self.cuisines.keys()
