__author__ = 'spgenot'
import unittest
from datetime import datetime
from datetime import timedelta
from trajectories.trajectory import Trajectory
import math


class TestTrajectory(unittest.TestCase):

    def test_t_trajectory(self):
        start_time = datetime.strptime('2016-01-13 15:26:0.0', "%Y-%m-%d %H:%M:%S.%f")
        x_array = range(0, 10)
        y_array = range(0, 10)
        t_array = [start_time + timedelta(0, x) for x in range(0, 10)]
        eps_array = [0 for x in range(0, 10)]
        idd = 0
        traj = Trajectory(idd, x_array, y_array, t_array, eps_array)
        self.assertEqual(x_array, traj.t_traj)

    def test_average_distance(self):
        start_time = datetime.strptime('2016-01-13 15:26:0.0', "%Y-%m-%d %H:%M:%S.%f")
        x_array = range(0, 10)
        y_array = range(0, 10)
        t_array = [start_time + timedelta(0,x) for x in range(0, 10)]
        eps_array = [0 for x in range(0, 10)]
        idd = 0
        traj = Trajectory(idd, x_array, y_array, t_array, eps_array)
        self.assertAlmostEqual(traj.average_distance(), math.sqrt(3), delta=0.01)

    def test_featurizer(self):
        start_time = datetime.strptime('2016-01-13 15:26:0.0', "%Y-%m-%d %H:%M:%S.%f")
        x_array = range(0, 10)
        y_array = range(0, 10)
        t_array = [start_time + timedelta(0,x) for x in range(0, 10)]
        eps_array = [0 for x in range(0, 10)]
        idd = 0
        traj = Trajectory(idd, x_array, y_array, t_array, eps_array)
        features = traj.featurizer()
        optimal_features = [[x, x, x] for x in x_array]
        self.assertEqual(features, optimal_features)