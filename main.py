import trajectories.trajectory
import os

__author__ = 'spgenot'


print("Loading trajectories...")
#os.chdir('..')
dir_path = os.getcwd()
if 'trajectories' in dir_path:
    os.chdir('..')
    dir_path = os.getcwd()

path = dir_path + '/sujet/data.csv'
dataset = trajectories.trajectory.Trajectories(path)
eps = 0.004
min_points = 30


print("Plotting a trajectory:")
dataset.trajectories[0].plot_trajectory()

print("Plotting multiple trajectories:")
dataset.plot_trajectories([0, 1, 2])


print("Displaying the result of the movement detection model:")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


for traj in dataset.trajectories:
    traj.normalize()
    traj.build_model(eps, min_points)
    print("Trajectory id: {}".format(traj.id))
    print("Number of pauses in the trajectory: {}".format(len(set(traj.labels))))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    traj.plot_trajectory()
