from location import location
from insertion_step import insertion_step

def print_locations(Locations):
	for e in Locations:
		print e.id_location
		print "-- name: ",e.name
		print "-- wait: ",e.wait
		"""
		print e.max_shift
		print e.shift
		print e.radio
		"""

start = 9 #hours
end = 20 #hours

Locations = []

for e in range(4):
	Locations.append(location())

#Instance of 4 elements
Locations[0].id_location = 0
Locations[0].name = "Loc1"
Locations[0].opening = 8
Locations[0].closing = 19
Locations[0].score = 4

Locations[1].id_location = 1		
Locations[1].name = "Loc2"
Locations[1].opening = 9
Locations[1].closing = 20
Locations[1].score = 5

Locations[2].id_location = 2
Locations[2].name = "Loc3"
Locations[2].opening = 12
Locations[2].closing = 23
Locations[2].score = 3

Locations[3].id_location = 3
Locations[3].name = "Loc4"
Locations[3].opening = 10
Locations[3].closing = 19
Locations[3].score = 4
Locations[3].wait = 0



times = [[0,0.5,1.3,0.3],[0.5,0,0.7,2],[1.3,0.7,0,1],[0.3,2,1,0]]

InsertionStep = insertion_step()

Locations = InsertionStep.update_locations(Locations,times)

print_locations(Locations)


