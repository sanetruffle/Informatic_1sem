from random import randint

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


def calculate_force(body, space_objects):
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        dx = obj.x - body.x
        dy = obj.y - body.y
        distance = (dx**2 + dy**2)**0.5
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


def recalculate_space_objects_positions(space_objects, dt):

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
