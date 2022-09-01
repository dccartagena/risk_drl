# Cliff environment class for safe deep reinforcement learning tests

# Import gym library
from gym import Env
from gym.spaces import Discrete, Box, Dict, MultiBinary, MultiDiscrete

# Import general purpose and numerical computation libraries
from scipy.stats import norm 
import numpy as np
import random
import os

def get_initial_map(initial_position, goal_position, shape):
    # Define cliff positions
    cliff_position = ((3, 1), (3, 2))

    # Initial map
    map = np.zeros(shape)

    # Setup initial and goal positions
    map[initial_position] = 1
    map[goal_position] = 2
    
    # Setup cliff positions
    # TODO Need to optimize
    for index in range(len(cliff_position)): map[cliff_position[index]] = 3 

    return map

# Class definition
class cliff_env(Env):
    def __init__(self, p_action_down = 0.01, initial_risk = 0.001, initial_position = [3, 0], goal_position = [3, 3]):
        # Define Action space:
        # 0: left
        # 1: up
        # 2: right
        # 3: down
        self.action_space = Discrete(4,)

        # Setup initial and goal position
        self.initial_position = initial_position
        self.goal_position = goal_position

        # Define observation space
        self.map_shape = (4, 4)
        self.observation_space = Dict({'position_x': Discrete(self.map_shape[0]), 
                                       'position_y': Discrete(self.map_shape[1]),
                                       'risk': Box(low = 0, high = 1, shape = (1,))})
        
        # Define action noise - Probability of going down
        self.p_action_down = p_action_down

        # Define initial risk
        self.risk = initial_risk

        # Define initial state
        self.state = (self.initial_position[0], self.initial_position[1], self.risk)

        # Define initial map
        self.map = get_initial_map(self.initial_position, self.goal_position, self.map_shape)

    def move(self, new_action):

        action = self. action_roulette(self, new_action)

        if action == 0:
            pass
        elif action == 1:
            pass
        elif action == 2:
            pass
        elif action == 3:
            pass
        pass
    
    def action_roulette(self, action):

        # Compute roulette value
        roulette_value = np.random.normal()

        # Compute percentile value, i.e. Probability(Z <= z) ~ self.p_action_down
        percentile = norm.ppf(self.p_action_down)

        # Change new action to down if roulette_value > percentile
        if (roulette_value > percentile):
            self.action = action
        else:
            self.action = 3

    def step(self, action):
        # Apply action
        new_position = self.move(action)
        last_position = self.state
        
        # Get new state

        # Compute reward

        # Episode termination signal
        
        # Info
        info = {}
        pass

    def render(self):
        pass

    def reset(self):
        # Initial state
        self.state = get_initial_map(self.initial_position, self.goal_position, self.observation_shape)