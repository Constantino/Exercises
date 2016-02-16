class insertion_step:

	def wait(self, opening,arrival):
		return max(0, opening-arrival)

	def estimateArrival(self,l_i, l_k, times):
		return times[l_i][l_k]
	
	def maxShift(self, Locations, i, opening, closing, arrival, times):
		if i == (len(Locations)-1):
			return min( closing-arrival , self.wait(opening, arrival))
		max_shift = min( closing-arrival , self.wait(opening, arrival)) + self.maxShift(Locations, i+1, Locations[i+1].opening, Locations[i+1].closing, self.estimateArrival(i, i+1,times), times)

		return max_shift	
	
	def update_locations(self,Locations,times):
		len_loc = len(Locations)-1
		for i in range(len_loc):
			arrival = self.estimateArrival(Locations[i].id_location,Locations[i+1].id_location,times)
			Locations[i].wait = self.wait(Locations[i].opening, arrival)
			
			Locations[i].max_shift = self.maxShift(Locations, i, Locations[i].opening, Locations[i].closing, arrival, times)
			"""
			Locations[i].Shift = Shift( i, Locations.LastIndex-1 )
			Locations[i].Ratio = Ratio( i )
			"""
		return Locations
