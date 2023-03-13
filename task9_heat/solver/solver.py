from typing import NamedTuple
import numpy as np

class Interval(NamedTuple):
    start: float
    end: float
class Space(NamedTuple):
    x: Interval
    t: Interval

class ISolver():
    def __init__(self, space: Space, dh: float, dt: float, rtol: float) -> None:
        self.space: Space = space
        self.dh: float = dh
        self.dt: float = dt
        self.rtol: float = rtol
        self.axis_x, self.axis_t = np.mgrid[
            	slice(space.x.start, space.x.end, dh),
                slice(space.t.start, space.t.end, dt)
            ]
        self.map = np.zeros((len(self.axis_x), len(self.axis_t)))

    def set_bounds(self, bound_map: np.ndarray, bound_values: np.ndarray) -> None:
        self.bound_map = bound_map
        self.bound_values = bound_values
        self.map = bound_values.copy()

    def run(self):
        raise NotImplementedError
