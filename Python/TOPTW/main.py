from location import location
from insertion_step import insertion_step

def print_locations(Locations):
	for e in Locations:
		print e.id_location
		print "-- name: ",e.name
		print "-- wait: ",e.wait
		
		print "-- max_shift: ",e.max_shift
		"""
		print e.shift
		print e.radio
		"""

start = 9 #hours
end = 20 #hours

Locations = []

for e in range(5):
	Locations.append(location())

#Instance of 4 elements
Locations[0].id_location = 0
Locations[0].name = "Loc1"
Locations[0].opening = 8
Locations[0].closing = 19
Locations[0].score = 4
Locations[0].max_shift = 0

Locations[1].id_location = 1		
Locations[1].name = "Loc2"
Locations[1].opening = 9
Locations[1].closing = 20
Locations[1].score = 5
Locations[1].max_shift = 0

Locations[2].id_location = 2
Locations[2].name = "Loc3"
Locations[2].opening = 12
Locations[2].closing = 23
Locations[2].score = 3
Locations[2].max_shift = 0

Locations[3].id_location = 3
Locations[3].name = "Loc4"
Locations[3].opening = 10
Locations[3].closing = 19
Locations[3].score = 4
Locations[3].wait = 0
Locations[3].max_shift = 0

Locations[4].id_location = 4
Locations[4].name = "End"
Locations[4].opening = end
Locations[4].closing = end
Locations[4].score = 4
Locations[4].wait = 0
Locations[4].max_shift = 0

times = [[0,0.5,1.3,0.3,1],[0.5,0,0.7,2,1],[1.3,0.7,0,1,1],[0.3,2,1,0,1],[1,1,1,1,0]]

InsertionStep = insertion_step()

Locations = InsertionStep.update_locations(Locations,times,start,end)

print_locations(Locations)


