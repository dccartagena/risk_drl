# Cliff environment class for safe deep reinforcement learning tests

# Import gym library
import gym
from gym import Env
from gym.spaces import Discrete, Box, Dict, MultiBinary, MultiDiscrete

# Import general purpose and numerical computation libraries
import numpy as np
import random
import os

# Class definition
class cliff_env(Env):
    def __init__(self, noise = 0.1):
        pass

    def step(self, action):
        pass

    def render(self):
        pass

    def reset(self):
        pass