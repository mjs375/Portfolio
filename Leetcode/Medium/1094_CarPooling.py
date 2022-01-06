class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        DEBUG = False
        if DEBUG: print("Capacity:{capacity}")
        
        stations = {} # track 'stations' and how many ppl at each one
        
        # Iterate each trip:
        for ppl,dpt,arv in trips:
            if DEBUG: print(f"Passengers:{ppl} | From:{dpt} | To:{arv}")
            
            # not `arv+1` bc ppl get off at station `i` before others get on:
            for i in range(dpt,arv):
                
                # Add new passengers:
                if i in stations.keys():
                    stations[i] += ppl
                else:
                    stations[i] = ppl
                    
                #--Did we overflow capacity at a certain station?
                if stations[i] > capacity:
                    return False
        
        return True
        
"""        
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
  You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
    Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

    Example 1:
      Input: trips = [[2,1,5],[3,3,7]], capacity = 4
      Output: false
    Example 2:
      Input: trips = [[2,1,5],[3,3,7]], capacity = 5
      Output: true
"""
