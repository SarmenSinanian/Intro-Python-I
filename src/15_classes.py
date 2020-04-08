# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# # constructor. It should inherit from LatLon. Look up the `super` method.

class ReprWaypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __repr__(self): # String Return magic method which refers to self.attributes
        return f"Repr {self.name}, {self.lat}, {self.lon}"


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self): # String Return magic method which refers to self.attributes
        return f"{self.name}, {self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return f"name: {self.name}, difficulty: {self.difficulty}, size: {self.size}, lat: {self.lat}, lon: {self.lon }"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

repr_waypoint = ReprWaypoint('Mt Everest', 1, 2)

waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)




# class LatLon: # Name of class(a "shell"/"vessel" at this point)
#     def __init__(self, lat, lon): # First method of the class which initializes the
#                                   #  self/parameter relationship where parameters
#                                   #  that get passed while calling the classname
#                                   #  LatLon(parameter0, parameter1) will result in
#                                   #  those parameters being associated to the self
#                                   #  via self.parameter_name
#         self.lat = lat
#         self.lon = lon
#
#
# # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# # constructor. It should inherit from LatLon. Look up the `super` method.
#
# class Waypoint(LatLon): # What happens if you do not super().__init__ after using
#                         #  another class name like class Something(SomethingElse)?
#                         # In any case, class Something(SomethingElse) is a class
#                         #  Something which has inheritance from class
#                         #  SomethingElse. Below, after initializing
#                         #  the self method (aka the 'constructor'), we create the relationship
#                         #  between self/parameters where parameters that get
#                         #  passed while calling the classname Waypoint will
#     def __init__(self, name, lat, lon):
#         super().__init__(lat, lon) # This is where we use the direct inheritance
#                                    #  from the 'SomethingElse' class (LatLon)
#                                    #  which then supplies the "self.parameter"
#                                    #  relationships (NOT THE VALUES OF LAT/LON) from the inherited class
#         self.name = name           # Here, we do normal parameter to self (attribute?)
#                                    #  assignment

