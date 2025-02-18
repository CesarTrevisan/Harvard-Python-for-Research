# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:16:50 2017

@author: trevi
"""

import numpy as np
import random
import scipy.stats as ss

def distance(p1, p2):
    """
    Find the distance between points p1 and p2.
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))
    

p1 = np.array([1,1])
p2 = np.array([4,4])


def majory_vote(votes):
    """
    XXX        
    
    """
    vote_counts = {}
    
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_count = max(vote_counts.values())
    
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)

    return random.choice(winners)

votes = [1,2,3,1,2,3,3,3,3,3,2,2,2,2]
majory_vote(votes)

def majory_vote_short(votes):
    """
    Return the most common element in votes.        
    
    """
    mode, count = ss.mstats.mode(votes)

    return mode

#######################################
    
points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
    
p = np.array([2.5, 2])

import matplotlib.pyplot as plt

plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])

distances = np.zeros(points.shape[0])

def find_nearest_neighbors(p, points, k=5):
    """
    Find the k-nearest neighbors of point p and return their indices.
    """

    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind =np.argsort(distances)
    
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    """
    Return predicted class for point p.
    """
    ind = find_nearest_neighbors(p, points, k)
    return majory_vote_short(outcomes[ind])
    
outcomes = np.array([0,0,0,0,1,1,1,1,1])



### Generating Synthetic Data

def generate_synth_data(n=50):
    """
    Create two sets of points from bivariate normal distributions.
    """
    points = np.concatenate( (ss.norm(0, 1).rvs((n,2)), ss.norm(1, 1).rvs((n,2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    
    return points, outcomes

n = 200
(points, outcomes) = generate_synth_data(n)
plt.figure()
plt.plot(points[:n, 0], points[:n, 1], "ro")
plt.plot(points[n:, 0], points[n:, 1], "bo")
plt.savefig("bivardata.pdf")

########################

def make_prediction_grid(predictors, outcomes, limits, h, k):
    """ Classify each point on the prediction grid. """
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    
    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    
    return (xx, yy, prediction_grid)
    
def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)
    
    
#### Testing Algoritm

(predictors, outcomes) = generate_synth_data()
    
k=5; filename="knn_synth_5.pdf"; limits = (-3, 4, -3, 4); h= 0.1

(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)    
plot_prediction_grid(xx, yy, prediction_grid, filename)
    
k=50; filename="knn_synth_50.pdf"; limits = (-3, 4, -3, 4); h= 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)    
plot_prediction_grid(xx, yy, prediction_grid, filename)
    
    
    



















    