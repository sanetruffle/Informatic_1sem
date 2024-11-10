from random import randint
from math import sqrt

gravitational_constant = 6.67408E-11

class Star():
    type = "star"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "red"
    image = None


class Planet():
    type = "planet"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "green"
    image = None
    angular_velocity = 0
    previous_position = (0, 0)


def calculate_force(body, space_objects):
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        dx = obj.x - body.x
        dy = obj.y - body.y
        distance = sqrt(dx**2 + dy**2)
        if distance == 0:
            continue

        force = gravitational_constant * body.m * obj.m / distance**2
        Fx = force * dx / distance
        Fy = force * dy / distance
        body.Fx += Fx
        body.Fy += Fy


def move_space_object(body, dt):
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def calculate_angular_velocity(planet, star):
    dx = planet.x - star.x
    dy = planet.y - star.y
    distance = sqrt(dx**2 + dy**2)
    velocity_magnitude = sqrt(planet.Vx**2 + planet.Vy**2)
    planet.angular_velocity = velocity_magnitude / distance


def check_kepler_second_law(planet, star, dt):
    dx1 = planet.previous_position[0] - star.x
    dy1 = planet.previous_position[1] - star.y
    dx2 = planet.x - star.x
    dy2 = planet.y - star.y

    area = abs(dx1 * dy2 - dy1 * dx2) / 2
    planet.previous_position = (planet.x, planet.y)
    return area


def recalculate_space_objects_positions(space_objects, dt):
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)
        if isinstance(body, Planet):
            calculate_angular_velocity(body, space_objects[0])  