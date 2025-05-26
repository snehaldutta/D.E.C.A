import random
import math
from typing import List, Tuple, Optional

Point = Tuple[float, float]

def dist(p1: Point, p2: Point) -> float:
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def is_point_in_circle(p: Point, center: Point, radius: float) -> bool:
    return dist(p, center) <= radius + 1e-9

def get_circle_two_points(p1: Point, p2: Point) -> Tuple[Point, float]:
    center = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    radius = dist(p1, p2) / 2
    return center, radius

def get_circle_three_points(p1: Point, p2: Point, p3: Point) -> Tuple[Point, float]:
    A = p2[0] - p1[0]
    B = p2[1] - p1[1]
    C = p3[0] - p1[0]
    D = p3[1] - p1[1]
    E = A * (p1[0] + p2[0]) + B * (p1[1] + p2[1])
    F = C * (p1[0] + p3[0]) + D * (p1[1] + p3[1])
    G = 2 * (A * (p3[1] - p2[1]) - B * (p3[0] - p2[0]))

    if abs(G) < 1e-9:
        return p1, 0  # Collinear points

    cx = (D * E - B * F) / G
    cy = (A * F - C * E) / G
    center = (cx, cy)
    radius = dist(center, p1)
    return center, radius

def welzl(points: List[Point], boundary: List[Point], n: int) -> Tuple[Point, float]:
    if n == 0 or len(boundary) == 3:
        if len(boundary) == 0:
            return ((0, 0), 0)
        elif len(boundary) == 1:
            return (boundary[0], 0)
        elif len(boundary) == 2:
            return get_circle_two_points(boundary[0], boundary[1])
        else:
            return get_circle_three_points(boundary[0], boundary[1], boundary[2])

    p = points[n - 1]
    center, radius = welzl(points, boundary, n - 1)

    if is_point_in_circle(p, center, radius):
        return center, radius
    else:
        return welzl(points, boundary + [p], n - 1)

def minimum_bounding_circle(points: List[Point]) -> Tuple[Point, float]:
    shuffled = points[:]
    random.shuffle(shuffled)
    return welzl(shuffled, [], len(shuffled))