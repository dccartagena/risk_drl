import torch
import torch.nn as nn
import torch.optim as optim
import torch.functional as F

import numpy as np

class DQN:
    def __init__(self, n_features, n_actions):
        self.n_features = n_features
        self.n_actions = n_actions

        # Define structure for NN
        pass

    def forward(self):
        pass

class replay_memory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory
        pass

class agent():

    # Initialize RL agent
    def __init__(self, n_features, n_actions, lr = 0.9999, gamma = 0.9999, param_reg = 0.5):

        self.n_features = n_features
        self.n_actions = n_actions

        self.state = []
        self.action = []
        self.reward = []
        self.risk = []

        self.lr = lr
        self.gamma = gamma
        self.param_reg = param_reg # Regularization parameter

        pass

    # Replay memory
    def replay_memory(self):
        pass

    # Compute risk from current state to fatal state
    def get_risk(self):
        # Compute shortest path
        pass
    
    # Computer shortest path to fatal state
    def get_shortest_path(self):
        pass

    # Compute reward + risk regularization
    def get_reward(self):
        # Get new reward

        # Get risk from current state

        # Compute regularized reward: reward + risk
        pass

    # Compute action
    def get_action(self):
        pass

    # Train agent
    def train(self, env):
        pass
    

    