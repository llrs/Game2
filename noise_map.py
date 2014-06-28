# This module will provide the functions needed to generate a good map
# It is used in Place.Maping()

# Problems
# I need that some set of options to be more common than other
# I need to set some rules that two rivers together canno't be (in parallel)
# I need a 2D map not a 1D map

# class rules
# Set which are the rules between different titles
# example: a lake and a sea can't be together
class rule(object):
    """Defines how the rule is"""
    def absolute(self):
        """The elements can be or cannot be together"""
        pass
    def priority(self):
        """The elements of this class can have priority or not against others"""
        pass
    
class rules(object):
    """Defines the rules between different elements,
they must be provided in a list"""
    def __init__(self, name):
        """Defines the name of the rules"""
        self.name = name
        self.rules = []
    def __str__(self):
        """return the name of the object, and its class"""
        return "Object of class rules, named {}.".format(self.name)
    def __repr__(self):
        """Change the criptic name for the type of the object"""
        return "Object of class rules"
    def _check_input(self, input_):
        """Check if it is a list or not, if it is a tuple it change to list"""
        if isinstance(input_, tuple):
            return list(input_)
        elif isinstance(group_1, list):
            pass
        else:
            print("Please introduce a list")
    def absolute_rule(self, group_1, group_2, absolute):
        """group_1, and group_2 are two list of objects.
If absolute = True they cannot be together, else they might be together"""
        from itertools import product
        group_1 = _check_input(group_1)
        group_2 = _check_input(group_2)        
        self.rules.append((product(group_1, group_2), absolute))

    def priority_rule(self, group_1, group_2, priority):
        """If group_1 need to be more representate than grup_2, priority is >1.
If group_2 need to be more representate than grup_1, priority is <1."""
        group_1 = _check_input(group_1)
        group_2 = _check_input(group_2)
        if isinstance(priority, int):
            pass
        else:
            print("Please introduce an integer for priority rules")
        self.rules.append((product(group_1, group_2), priority))
    def remove_rule(self, rule):
        """Remove a rule of self. rules given the index of it"""
        if rule >= len(self.rules):
            print("Please introduce a valid index of the rule to delete")
        self.rules.pop(rule)
        
class noise(object):
    """Defines the noise for a map"""
    def __init__(self, frequency, amplitud, objects):
        """Create the numbers needed for """
        pass
    """Defines the rules of the noise that will be used"""
    def maping(self, width, rules, objects):#Other options needed to make the "noise" function
        """Create a map of width witdth according to the rules.
It use the noise defined to place the objects"""
        pass
    def change_rules(rules):
        """Using this method will modify the map to fit with the new rules"""
        pass

# class check
# Given a random map check if follows the rules, and correct it
