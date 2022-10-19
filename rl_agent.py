import torch
import torch.nn as nn
import torch.optim as optim
import torch.functional as F

import numpy as np
import random

from collections import deque

from shortest_path import tree

class DQN(nn.Module):
    def __init__(self, n_features, n_actions):
        # Initialize nn Module
        super(DQN, self).__init__()
        
        # Store feature and actions
        self.n_features = n_features
        self.n_actions = n_actions

        # Define structure for NN
        #TODO Define an adequate architecture - Maybe LSTM or GRU?
        self.architecture = nn.Sequential(
            nn.Linear(self.n_features, 32),
            nn.Dropout(p=0.2),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.Dropout(p=0.2),
            nn.ReLU(),
            nn.Linear(16, self.n_actions),
        )
        pass

    def forward(self, input):
        #TODO Need softmax?
        logits = self.architecture(input) 
        return logits

class replay_memory:
# Store the tuples (state, action, next state, reward) that the agent observes.
    def __init__(self, capacity):
        # Initialize the memory
        self.capacity = capacity
        self.memory = deque([], maxlen=self.capacity)
        pass
    
    def store(self, state, action, next_state, reward, risk):
        transition = (state, action, next_state, reward, risk)
        self.memory.append(transition)
        pass

    def sample(self, batch_size):
        # Sample transition from memory
        return random.sample(self.memory, batch_size)

    def __len__(self):
        # length of memory
        return len(self.memory)

class agent(DQN):

    # Initialize RL agent
    def __init__(self, n_features, n_actions, lr = 0.9999, gamma = 0.9999, beta = 0.5):
        # Initialize NN module
        super(agent, self).__init__
        
        # Store number of features and actions
        self.n_features = n_features
        self.n_actions = n_actions

        # Initialize state, action, reward, and risk variables
        self.state = []
        self.action = []
        self.reward = []
        self.risk = []

        # Store learning parametres
        self.lr = lr        # Learning rate
        self.gamma = gamma  # Discounted factor
        self.beta = beta    # Regularization parameter
        pass

    # Compute risk from current state to fatal state
    def get_risk(self):
        # Compute shortest path
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
    
    # Optimize NN - Backpropagation
    def optimize_model():
        pass    