from typing import Tuple

import math


__version__ = "1.0.0"


Coordinate = Tuple[float, float]


def coordinate_to_radians(value: Coordinate) -> Coordinate:
    """
    Converts the given coordinate pair from degrees to radians.

    Arguments:
        value: The degree coordinate pair to convert.
    """
    return (math.radians(value[0]), math.radians(value[1]))


class PlanetRadius:
    """
    Solar System planet radii in kilometers and miles.
    """

    mercury_km = 2439.7
    mercury_mi = 1515.97

    venus_km = 6051.8
    venus_mi = 3760.44

    earth_km = 6371.0088
    earth_mi = 3958.8

    mars_km = 3389.5
    mars_mi = 2106.1

    jupiter_km = 69911
    jupiter_mi = 43441

    saturn_km = 58232
    saturn_mi = 36184

    uranus_km = 25362
    uranus_mi = 15759

    neptune_km = 24622
    neptune_mi = 15300


def great_circle_distance(first: Coordinate, second: Coordinate, *, radius: float = PlanetRadius.earth_km) -> float:
    """
    Calculates the great circle distance between the given (latitude, longitude) coordinate pairs.

    Latitude and longitude values are expected to be in *degrees*.

    Arguments:
        first: The first (latitude, longitude) pair.
        second: The second (latitude, longitude) pair.
        radius: Sphere radius (or mean spheroid radius), default is `PlanetRadius.earth_km`.

    Returns:
        The calculated distance.
    """
    return great_circle_distance_rad(
        coordinate_to_radians(first),
        coordinate_to_radians(second),
        radius=radius,
    )


def great_circle_distance_rad(
    first: Coordinate, second: Coordinate, *, radius: float = PlanetRadius.earth_km
) -> float:
    """
    Calculates the great circle distance between the given (latitude, longitude) coordinate pairs.

    Latitude and longitude values are expected to be in *radians*.

    Arguments:
        first: The first (latitude, longitude) pair.
        second: The second (latitude, longitude) pair.
        radius: Sphere radius (or mean spheroid radius), default is `PlanetRadius.earth_km`.

    Returns:
        The calculated distance.
    """
    return radius * math.acos(
        math.sin(first[0]) * math.sin(second[0])
        + math.cos(first[0]) * math.cos(second[0]) * math.cos(first[1] - second[1])
    )
