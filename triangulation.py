from geopy import distance

def triangulate(tower1, tower2, tower3, dist1, dist2, dist3):
    """
    Basic triangulation using three cell towers.
    tower1, tower2, tower3 are tuples of (latitude, longitude)
    dist1, dist2, dist3 are distances from each tower to the target
    """
    def get_third_point(p1, d1, p2, d2):
        # Calculate the two possible points
        bearing = distance.distance(kilometers=d1).destination(p1, 0)
        c1 = distance.distance(kilometers=d2).destination(p2, bearing)
        c2 = distance.distance(kilometers=d2).destination(p2, bearing + 180)
        return c1, c2

    # Get two possible points from the first two towers
    c1, c2 = get_third_point(tower1, dist1, tower2, dist2)
   
    # Check which point is closer to the third tower
    if abs(distance.distance(c1, tower3).kilometers - dist3) < abs(distance.distance(c2, tower3).kilometers - dist3):
        return c1
    else:
        return c2

# Example usage (can be commented out when used as a module)
# tower1 = (40.7128, -74.0060)  # New York
# tower2 = (34.0522, -118.2437)  # Los Angeles
# tower3 = (41.8781, -87.6298)  # Chicago
# dist1 = 100  # km
# dist2 = 200  # km
# dist3 = 150  # km
# estimated_location = triangulate(tower1, tower2, tower3, dist1, dist2, dist3)
# print(f"Estimated location: {estimated_location}")
