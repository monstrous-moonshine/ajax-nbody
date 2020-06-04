from flask import request
import numpy as np

class Body:
    def __init__(self, params):
        self.r = np.array(params[0:2])
        self.v = np.array(params[2:4])
        self.m = params[4]
    
    def force_from(self, other):
        G = 6.67e-11
        delta = other.r - self.r
        dist2 = np.sum(delta ** 2)
        magnitute = G * self.m * other.m / dist2 ** 1.5
        return delta * magnitute

    def move(self, f, dt):
        a = f / self.m
        self.v = self.v + a * dt
        self.r = self.r + self.v * dt

    def get_params(self):
        return list(self.r) + list(self.v) + [self.m]

def update_nbody(form):
    dt = 2.5e4
    bodies = [Body([float(item) for item in form.getlist(key)]) \
        for key in form.keys()]
    
    # compute the forces
    forces = [np.array([0, 0]) for _ in bodies]
    for i, b1 in enumerate(bodies):
        for j, b2 in enumerate(bodies):
            if i != j:
                forces[i] = forces[i] + b1.force_from(b2)
    
    for f, b in zip(forces, bodies):
        b.move(f, dt)
    
    return [b.get_params() for b in bodies]
