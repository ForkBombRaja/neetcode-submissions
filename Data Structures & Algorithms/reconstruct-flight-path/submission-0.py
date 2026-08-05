from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # set up a dictionary where we will put the tickets
        ticketDictionary = defaultdict(list)
        # empty itinerary which we fill
        itinerary = []
        for fro, to in sorted(tickets, reverse=True):
            ''' 
            for each ticket push to dict in format from : to
            '''
            ticketDictionary[fro].append(to)
        def constructItinerary(airport):
            """
            recursively construct itinerary from a base airport
            """
            while ticketDictionary[airport]:
                ''' 
                keep recursing while the source airport is still in the dictionary
                recurse on the nect airport return if all dests from there are exhausted
                this will cause the 
                '''
                constructItinerary(ticketDictionary[airport].pop())
            #append current airport to itinerary
            itinerary.append(airport)
        # construct itinerary from JFK
        constructItinerary("JFK")
        return itinerary[::-1]         