class insertion_step:

	def wait(self, opening,arrival):
		wait = max(0, opening-arrival)
		
		return wait

	def estimateArrival(self,l_i, l_k, times,start):
		return times[l_i][l_k]+start
	
	def maxShift(self, Locations, i, opening, closing, arrival, times,start,end):
		if i == (len(Locations)-1):
			return 0
		max_shift = min( closing-arrival , self.wait(opening, arrival) + self.maxShift(Locations, i+1, Locations[i+1].opening, Locations[i+1].closing, self.estimateArrival(i, i+1,times,start), times,start,end))

		return max_shift	

	def Shift( j , i):
		cij = EstimateArrivalFrom( IncludedLocations[i], Locations[j] )
		wait = Locations[j].Wait
		Tj = max_shift
		cjk = EstimateArrivalFrom( Locations[j], IncludedLocations[i+1] )
		cik = EstimateArrivalFrom( IncludedLocations[i],  IncludedLocations[i+1])

		Shift = cij + wait + Tj + cjk - cik
		Sum_Wait_MaxShift = IncludedLocations[i+1].Wait + IncludedLocations[i+1].MaxShift

		return Shift if (Shift <= Sum_Wait_MaxShift) else Sum_Wait_MaxShift
		
	def update_locations(self,Locations,times,start,end):
		len_loc = len(Locations)-1
		for i in range(len_loc):
			arrival = self.estimateArrival(Locations[i].id_location,Locations[i+1].id_location,times,start)
			Locations[i].wait = self.wait(Locations[i].opening, arrival)
			
			print "o: ",Locations[i].opening," a: ",arrival," wait: ",Locations[i].wait

			Locations[i].max_shift = self.maxShift(Locations, 0, Locations[i].opening, Locations[i].closing, arrival, times,start,end)
			"""
			Locations[i].Shift = Shift( i, Locations.LastIndex-1 )
			Locations[i].Ratio = Ratio( i )
			"""
		return Locations
