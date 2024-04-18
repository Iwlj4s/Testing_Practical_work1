import pytest
import math


# Вариант 1
def triangle_area_base_height(base, height):
    return 0.5 * base * height


# Вариант 2
def triangle_area_sides_angle(side1, side2, angle):
    return 0.5 * side1 * side2 * math.sin(math.radians(angle))


# Вариант 3
def resistance_parallel(r1, r2):
    return (r1 * r2) / (r1 + r2)


# Вариант 4
def resistance_series(r1, r2):
    return r1 + r2


# Вариант 5
def current_voltage_resistance(voltage, resistance):
    return voltage / resistance


# Вариант 6
def pounds_to_kg(pounds):
    return pounds * 0.4059


# Вариант 7
def trip_cost(gas_consumption, distance, gas_price_per_liter):
    return 2 * (gas_consumption / 100) * distance * gas_price_per_liter


# Вариант 8
def trapezoid_area(base1, base2, height):
    return ((base1 + base2) / 2) * height


# Вариант 9
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height


# Вариант 10
def cylinder_surface_area(radius, height):
    base_area = 2 * math.pi * radius * height
    side_area = 2 * math.pi * radius ** 2
    return base_area + side_area


# Вариант 11
def parallelepiped_volume(a, b, c):
    return a * b * c


# Вариант 12
def verst_to_km(verst):
    return verst * 1.0668
