class insertion_step:

	def wait(self, opening,arrival):
		return max(0, opening-arrival)

	def estimateArrival(self,l_i, l_k, times,start):
		return times[l_i][l_k]+start
	
	def maxShift(self, Locations, i, opening, closing, arrival, times,start,end):
		if i == (len(Locations)-1):
			return 0
		return 	min( closing-arrival , 
						self.wait(opening, arrival) + 
							self.maxShift(
								Locations, i+1, Locations[i+1].opening, 
								Locations[i+1].closing, self.estimateArrival(i, i+1,times,start), 
								times,start,end))


	def ratio(self,Locations,i):
		return Locations[i].score*1.0/Locations[i].shift	

	def Shift( self, Locations, j , i, times, start):
		cij = self.estimateArrival( i, j, times, start )
		wait = Locations[j].wait
		Tj = Locations[j].max_shift
		cjk = self.estimateArrival( j, len(Locations)-1 , times, start)
		cik = self.estimateArrival( i,  len(Locations)-1, times, start)

		Shift = cij + wait + Tj + cjk - cik
		Sum_Wait_MaxShift = Locations[j].wait + Locations[j].max_shift

		return Shift if (Shift <= Sum_Wait_MaxShift) else Sum_Wait_MaxShift
		
	def update_locations(self,Locations,times,start,end):
		
		for i in range(1,len(Locations)-1):
			arrival = self.estimateArrival(Locations[i].id_location,Locations[i+1].id_location,times,start)

			Locations[i].wait = self.wait(Locations[i].opening, arrival)

			Locations[i].max_shift = self.maxShift(Locations, 0, Locations[i].opening, Locations[i].closing, arrival, times,start,end)
			
			Locations[i].shift = self.Shift(Locations, i, i-1, times, start)
		
			Locations[i].ratio = self.ratio( Locations, i )
			
		return Locations
