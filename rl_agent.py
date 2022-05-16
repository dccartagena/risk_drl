import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class rl_agent(nn.Module):
    def __init__(self):
        # define NN architecture
        pass

    def reset_trajectory(self):
        # Reset trajectories if on-policy
        pass

    def make_action(self):
        # Compute forward of NN
        # Convert NN value to PDF
        # Sample action from PDF
        # Compute log-probability
        pass

    def q_values(self):
        # Compute Q values
        pass

    def get_rewards(self):
        # Get rewards
        pass

    def get_safety(self):
        #Get safety values
        pass




