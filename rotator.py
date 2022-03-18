import numpy as np

class Rotator:

    def __init__(self, rotation_angle, x_reference_point, y_reference_point, delta=0):
        self.rotation_angle = rotation_angle
        self.x_reference_point = x_reference_point
        self.y_reference_point = y_reference_point
        self.delta = delta

    def rotate_point(self, x, y, z):
        y_pn = self.y_reference_point - y
        x_pn = self.x_reference_point - x

        b = x_pn/y_pn
        a = np.rad2deg(np.arctan(x_pn/y_pn))
        l_p = np.sqrt(np.square(y_pn) + np.square(x_pn))

        a1 = self.rotation_angle - a

        y_np = l_p * np.cos(np.deg2rad(a1))
        x_np = l_p * np.sin(np.deg2rad(a1))

        return x_np, y_np, z + self.delta
