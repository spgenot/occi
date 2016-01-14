__author__ = 'spgenot'
import unittest

import tests.trajectory_generator


class TestGeneratedTrajectories(unittest.TestCase):

    def test_straight_line(self):
        sl = tests.trajectory_generator.StraightLine(10, 1, 1)
        x_array = range(0, 10)
        t_array = range(0, 10)
        y_array = [1 for x in range(0, 10)]
        eps_array = [0 for x in range(0, 10)]
        self.assertEqual(x_array, sl.trajectory.x_traj)
        self.assertEqual(y_array, sl.trajectory.y_traj)
        self.assertEqual(t_array, sl.trajectory.t_traj)
        self.assertEqual(eps_array, sl.trajectory.eps_traj)

    def test_straight_line_with_pause(self):
        slwp = tests.trajectory_generator.StraightLineWithPause(10,3,1,1)
        x_array = [0, 1, 2, 3, 3, 3, 4, 5, 6, 7]
        t_array = range(0, 10)
        y_array = [1 for x in range(0, 10)]
        eps_array = [0 for x in range(0, 10)]
        self.assertEqual(x_array, slwp.trajectory.x_traj)
        self.assertEqual(y_array, slwp.trajectory.y_traj)
        self.assertEqual(t_array, slwp.trajectory.t_traj)
        self.assertEqual(eps_array, slwp.trajectory.eps_traj)

