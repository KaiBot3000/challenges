import math

def shortestDetour(points):
    """Calculate the detour distance between two different rides. 

    Given four latitude / longitude pairs, where driver one is traveling 
    from point A to point B and driver two is traveling from point C to point D, 
    write a function (in your language of choice) to calculate the shorter of the 
    detour distances the drivers would need to take to pick-up and drop-off the other driver.
    """

    trip_a_start, trip_a_stop, trip_b_start, trip_b_stop = points
    # print trip_a_start, trip_a_stop, trip_b_start, trip_b_stop
    a_trip = [trip_a_start, trip_a_stop]
    print "atrip", a_trip
    a_drops = [trip_a_start, trip_b_start, trip_b_stop, trip_a_stop]
    print "adrops", a_drops
    a_detour = totalDistance(a_drops) - totalDistance(a_trip)
    print "adetour", a_detour

    b_trip = [trip_b_start, trip_b_stop]
    b_drops = [trip_b_start, trip_a_start, trip_a_stop, trip_b_stop]
    b_detour = totalDistance(b_drops) - totalDistance(b_trip)
    print "btrip", b_trip
    print "bdrop", b_drops
    print "bdetour", b_detour

    
    shortest = min(a_detour, b_detour)

    return shortest



def totalDistance(route):
    """Given a list of point tuples, determine the total distance travelled"""

    distance = 0
    start = None

    for point in route:
        if start:
            distx = abs((start[0] - point[0]))
            disty = abs((start[1] - point[1]))
            distance += math.sqrt((distx**2) + (disty**2))
        start = point

    return distance

# print shortestDetour([(1,1), (1,4), (1,2), (1,3)])
print totalDistance([(0,0), (3, 4)])