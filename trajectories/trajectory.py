from math import sqrt
from collections import defaultdict
import datetime
import colorsys
import matplotlib.pyplot as plt
import pandas as pd
from trajectories import model

__author__ = 'spgenot'


class Trajectory:
    """
    Defines a trajectory.
    @idd: the id of the trajectory
    @x_traj: the x positions of the trajectory
    @y_traj: the y positions of the trajectory
    @t_traj: the time positions of the trajectory
    @eps_traj: the value of the error for each position
    @in_movement: if it is non empty: contains movement state (True -> in movement) of each position
    @labels: if it is non empty: contains the cluster of points the position belongs to (-1 => in movement, outlier)
    """
    def __init__(self, idd, x_array, y_array, t_array, eps_array):
        """
        Initialisation method
        """
        self.id = idd
        self.x_traj = x_array
        self.y_traj = y_array
        self.t_traj = t_array
        self.process_time()
        self.eps_traj = eps_array
        self.in_movement = []
        self.labels = []

    def plot_trajectory(self):
        """
        Plots the trajectory at hand.
        If we have built the model, it will also plot the clusters of points that are not in movement.
        """
        plt.plot(self.x_traj, self.y_traj, 'x')
        unique_labels = set(self.labels)
        n = len(unique_labels)
        hsv_tuples = [(x*1.0/n, 0.5, 0.5) for x in range(n)]
        rgb_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples)

        for l in range(0,len(unique_labels)):
            stop_x = []
            stop_y = []
            for x in range(0, len(self.labels)):
                if self.labels[x] == l and self.labels[x] != -1:
                    stop_x.append(self.x_traj[x])
                    stop_y.append(self.y_traj[x])
            plt.plot(stop_x, stop_y, 'o', color=rgb_tuples[l])
        plt.title("Display of trajectory: {}".format(self.id))
        plt.show()

    def average_distance(self):
        """
        Computes and returns the average distance between two consecutive points.
        """
        avg_dist = 0
        for i in range(0, len(self.x_traj)-1):
            avg_dist += sqrt((self.x_traj[i] - self.x_traj[i+1])**2 +
                             (self.y_traj[i] - self.y_traj[i+1])**2 +
                             (self.t_traj[i] - self.t_traj[i+1])**2)
        avg_dist /= (len(self.x_traj)-1)
        return avg_dist

    def process_time(self):
        """
        Takes the time in a datetime format and transforms into an interval of elapsed seconds
        """
        start_time = self.t_traj[0]
        new_time = []
        for x in self.t_traj:
            new_time.append((x - start_time).seconds)
        self.t_traj = new_time

    def normalize(self):
        """
        Rescale the values.
        We rescale the x and y axis by taking the max and min globally over x and y.
        For t we take the max over t only.
        """
        maxi_xy = max(max(self.x_traj), max(self.y_traj))
        mini_xy = min(min(self.x_traj), min(self.y_traj))
        maxi_t = max(self.t_traj)
        mini_t = min(self.t_traj)
        for i in range(0, len(self.x_traj)):
            self.x_traj[i] = (self.x_traj[i] - mini_xy)/float(maxi_xy-mini_xy)
            self.y_traj[i] = (self.y_traj[i] - mini_xy)/float(maxi_xy-mini_xy)
            self.t_traj[i] = (self.t_traj[i] - mini_t)/float(maxi_t-mini_t)

    def featurizer(self):
        """
        Takes the trajectory and transforms it into a feature vector [(x,y,t)]
        """
        features = []
        for i in range(0, len(self.x_traj)):
            point_feature = [self.x_traj[i], self.y_traj[i], self.t_traj[i]]
            features.append(point_feature)
        return features

    def build_model(self, eps, min_points):
        """
        Builds the DBScan model, clusters the points, and sets the labels and in_movement variables.
        :param eps: Eps parameter for DBScan
        :type eps: float
        :param min_points: Minimum of points to form cluster, DBScan parameter
        :type min_points: int
        """
        features = self.featurizer()
        dbscan = model.DBScan(features, eps, min_points)
        dbscan.fit_predict()
        self.labels = dbscan.cluster_labels
        self.in_movement = [(x<0) for x in self.labels]


class Trajectories:
    """
    Defines a set of trajectories.
    @trajectories: list of Trajectory objects
    """
    def __init__(self, path):
        """
        Class initialisation method.
        :param path: path to the trajectories data (data.csv)
        :type path: str
        """
        df = pd.read_csv(path, sep='\t')
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)
        t_dict = defaultdict(list)
        eps_dict = defaultdict(list)
        for row in df.iterrows():
            x_dict[row[1][0]].append(row[1][1])
            y_dict[row[1][0]].append(row[1][2])
            t_dict[row[1][0]].append(datetime.datetime.strptime(row[1][3], "%Y-%m-%d %H:%M:%S.%f"))
            eps_dict[row[1][0]].append(row[1][4])
        trajectories = []
        for idd in x_dict.keys():
            traj = Trajectory(idd, x_dict[idd], y_dict[idd], t_dict[idd], eps_dict[idd])
            trajectories.append(traj)
        self.trajectories = trajectories

    def plot_trajectories(self, indexes):
        """
        Plots all the trajectories contained in indexes.
        :param indexes: indexes of the trajectories to plot
        :type indexes: list(str)
        """
        for x in indexes:
            plt.plot(self.trajectories[x].x_traj, self.trajectories[x].y_traj, 'x')
        plt.title("Plot of multiple trajectories.")
        plt.show()

    def get_trajectory(self, idd):
        """
        Fetch trajectory with id=idd
        :param idd: id of the trajectory to fetch
        :return: Trajectory
        """
        for x in self.trajectories:
            if x.id == idd:
                return x
