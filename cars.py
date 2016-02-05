import math

def shortestDetour(points):
    """Calculate the detour distance between two different rides. 

    Given four latitude / longitude pairs, where driver one is traveling 
    from point A to point B and driver two is traveling from point C to point D, 
    write a function (in your language of choice) to calculate the shorter of the 
    detour distances the drivers would need to take to pick-up and drop-off the other driver.
    """

    a_start, a_stop, b_start, b_stop = points

    a_trip = [a_start, a_stop]
    a_drops = [a_start, b_start, b_stop, a_stop]
    a_detour = totalDistance(a_drops) - totalDistance(a_trip)

    b_trip = [b_start, b_stop]
    b_drops = [b_start, a_start, a_stop, b_stop]
    b_detour = totalDistance(b_drops) - totalDistance(b_trip)

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
