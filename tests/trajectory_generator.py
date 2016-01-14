from datetime import datetime
from datetime import timedelta
from trajectories.trajectory import Trajectory
import numpy as np

__author__ = 'spgenot'

"""
Contains all classes of synthetically generated test trajectories.
"""


def time_spacing(n, t_spacing):
    """
    Helper method to create a even spaced datetime array
    """
    start_time = datetime.now()
    t_traj = [start_time]
    for x in range(0, n-1):
        new_time = start_time + timedelta(0, t_spacing*(x+1))
        t_traj.append(new_time)
    return t_traj


class StraightLine:
    """
    Defines a trajectory with equal x-spacing and t-spacing.
    Corresponds to a straight line with no pause.
    """
    def __init__(self, n, x_spacing, t_spacing):
        x_traj = [i*x_spacing for i in range(0, n)]
        y_traj = [1 for i in range(0, n)]
        eps_traj = [0 for i in range(0, n)]
        t_traj = time_spacing(n, t_spacing)
        self.trajectory = Trajectory(1, x_traj, y_traj, t_traj, eps_traj)


class StraightLineWithPause:
    """
    Defines a trajectory with equal x-spacing and y-spacing except one fix point at the middle.
    Corresponds to a straight line with a single (perfect) pause.
    """
    def __init__(self, number_samples, number_samples_in_pause, x_spacing, t_spacing):
        t_traj = time_spacing(number_samples, t_spacing)
        y_traj = [1 for i in range(0, number_samples)]
        eps_traj = [0 for i in range(0, number_samples)]
        pause_position = number_samples - number_samples_in_pause
        if pause_position % 2 == 0:
            pause_position /= 2
            end_position = 2*pause_position+1
        else:
            pause_position = (pause_position - 1)/2
            end_position = 2*pause_position+2

        before = [x*x_spacing for x in range(0, pause_position)]
        pause = [pause_position*x_spacing for x in range(0, number_samples_in_pause - 1)]
        after = [x*x_spacing for x in range(pause_position, end_position)]
        x_traj = before + pause + after
        self.trajectory = Trajectory(2, x_traj, y_traj, t_traj, eps_traj)


class StraightLineWithNoisyPause:
    """
    Defines a straight line with pause.
    The pause is noisy, i.e. is spread out around a fix point along a N(0,var) noise.
    """
    def __init__(self, number_samples, number_samples_in_pause, x_spacing, t_spacing):
        t_traj = time_spacing(number_samples, t_spacing)
        y_traj = [1 for i in range(0, number_samples)]
        eps_traj = [0 for i in range(0, number_samples)]
        pause_position = number_samples - number_samples_in_pause
        if pause_position % 2 == 0:
            pause_position /= 2
            end_position = 2*pause_position+1
        else:
            pause_position = (pause_position - 1)/2
            end_position = 2*pause_position+2

        noise = np.random.normal(0, x_spacing/2.0, number_samples_in_pause)

        before = [x*x_spacing for x in range(0, pause_position)]
        pause = [pause_position*x_spacing for x in range(0, number_samples_in_pause - 1)]
        pause = [x + y for x, y in zip(pause, noise)]
        after = [x*x_spacing for x in range(pause_position, end_position)]
        x_traj = before + pause + after
        self.trajectory = Trajectory(2, x_traj, y_traj, t_traj, eps_traj)




