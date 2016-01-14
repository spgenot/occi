__author__ = 'spgenot'
import unittest

import tests.trajectory_generator


class TestModel(unittest.TestCase):

    def test_straight_line(self):
        sl_traj = tests.trajectory_generator.StraightLine(10,1,1).trajectory
        eps = 0.2
        min_points = 2
        sl_traj.build_model(eps, min_points)
        expected_labels = [-1 for x in range(0, 10)]
        expected_in_mouvement = [True for x in range(0, 10)]
        self.assertEqual(list(sl_traj.labels), expected_labels)
        self.assertEqual(sl_traj.in_movement, expected_in_mouvement)


    def test_straight_line_with_pause(self):
        slwp_traj = tests.trajectory_generator.StraightLineWithPause(10, 3, 1, 1).trajectory
        eps = 1  #Min distance between two points in same x position at time t+1
        min_points = 2
        expected_labels = [-1, -1, -1, 0, 0, 0, -1, -1, -1, -1]
        expected_in_mouvement = [True, True, True, False, False, False, True, True, True, True]
        slwp_traj.build_model(eps, min_points)
        self.assertEqual(list(slwp_traj.labels), expected_labels)
        self.assertEqual(slwp_traj.in_movement, expected_in_mouvement)


