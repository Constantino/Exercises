import random

class insertion_step:

	def wait(self, opening,arrival):
		#Wait: in case of arriving before the location opens, 
		#if we arrive later then we wait 0 minutes
		return max(0, opening-arrival)

	def estimateArrival(self,l_i, l_k, times,start):
		#estimate time from location_i to location_k + start time
		return times[l_i][l_k]+start
	
	def maxShift(self, Locations, i, opening, closing, arrival, times,start,end):
		if i == (len(Locations)-1):
			#If we reach the last location, means it's the end of the tour
			return 0

		#We chose the maximum time allowed to stay in one place in order to not make 
		#infeasible the staying time for the rest of locations.
		return 	min( closing-arrival , 
						self.wait(opening, arrival) + 
							self.maxShift(
								Locations, i+1, Locations[i+1].opening, 
								Locations[i+1].closing, self.estimateArrival(i, i+1,times,start), 
								times,start,end))


	def ratio(self,Locations,i):
		#Gain of choosing it taking score vs cost of time
		return Locations[i].score*1.0/Locations[i].shift	

	def Shift( self, Locations, j , i, times, start):
		#Get the total cost of time of including a location between location_i and location_k
		cij = self.estimateArrival( i, j, times, start )
		wait = Locations[j].wait
		Tj = Locations[j].max_shift
		cjk = self.estimateArrival( j, len(Locations)-1 , times, start)
		cik = self.estimateArrival( i,  len(Locations)-1, times, start)

		Shift = cij + wait + Tj + cjk - cik
		Sum_Wait_MaxShift = Locations[j].wait + Locations[j].max_shift

		return Shift if (Shift <= Sum_Wait_MaxShift) else Sum_Wait_MaxShift
		
	def update_locations(self,Locations,times,start,end):
		#Since location 0 is the origin and the last one the end of the tour:
		#Iterate from the second location until the penultimate location
		for i in range(1,len(Locations)-1):
			Locations[i].arrival = self.estimateArrival(Locations[i].id_location,Locations[i+1].id_location,times,start)

			Locations[i].wait = self.wait(Locations[i].opening, Locations[i].arrival)

			Locations[i].max_shift = self.maxShift(Locations, 0, Locations[i].opening, Locations[i].closing, Locations[i].arrival, times,start,end)
			
			Locations[i].shift = self.Shift(Locations, i, i-1, times, start)
		
			Locations[i].ratio = self.ratio( Locations, i )
			
		return Locations

	def select_to_insert(self,Locations):
		percentage = 30 #percent
		ratios = [e.ratio for e in Locations]
		#Get radio value to select potential locations to choose
		selection_point = sum(ratios)*percentage/100
		potential_locations = [e for e in Locations if e.ratio >= selection_point]
		
		len_pot = len(potential_locations)
		index = random.randrange(0,len_pot)
		location_selected = potential_locations[index]
		"""
		print "random_number: ",index
		print "ratios: ",ratios
		print "select_point: ",selection_point
		print "potencial_locations: ",potential_locations
		"""
		#print "location_selected: ",location_selected
		#print "l sel: ",Locations[location_selected].id_location
		return location_selected

	def update_after_insertion(self,j,Locations,times,start,end):
		k = j+1
		Locations[j].shift = self.Shift(Locations, j, j-1, times, start)
		Locations[k].wait = max( 0, Locations[k].wait - Locations[j].shift )
		Locations[k].arrival = Locations[k].arrival + Locations[j].shift
		Locations[k].shift = max(0,Locations[j].shift - Locations[k].wait)
		print "k: ",k," shift: ",Locations[k].shift
		#Locations[k].start = Locations[k].start + Locations[k].shift
		Locations[k].max_shift = max(0,Locations[k].max_shift - Locations[k].shift)

		return Locations
