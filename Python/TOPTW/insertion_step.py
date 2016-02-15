class insertion_step:

	def wait(self, opening,arrival):
		return max(0, opening-arrival)

	def estimateArrival(self,l_i, l_k, times):
		return times[l_i][l_k]

	def update_locations(self,Locations,times):
		len_loc = len(Locations)-1
		for i in range(len_loc):
			arrival = self.estimateArrival(Locations[i].id_location,Locations[i+1].id_location,times)
			Locations[i].wait = self.wait(Locations[i].opening, arrival)

			#print "i: ",i," wait: ",Locations[i].wait
			"""
			Locations[i].MaxShift = MaxShift(Locations, i, Locations[i].opening, Locations[i].closing, arrival )

			Locations[i].Shift = Shift( i, Locations.LastIndex-1 )
			Locations[i].Ratio = Ratio( i )
			"""
		return Locations
