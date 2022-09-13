# Cliff environment class for safe deep reinforcement learning tests

# Import gym library
from gym import Env
from gym.spaces import Discrete, Box, Dict, MultiBinary, MultiDiscrete

# Import general purpose and numerical libraries
from scipy.stats import norm 
import numpy as np

def get_initial_map(initial_position, goal_position, shape):
    # Define cliff positions
    cliff_position = ((3, 2), (3, 3), (3, 4))

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
    def __init__(self, p_action_down = 0.01, initial_risk = 0.001, initial_position = (3, 0), goal_position = (3, 6)):
        # Define Action space:
        # 0: left
        # 1: up
        # 2: right
        # 3: down
        self.action_space = Discrete(4,)

        # Setup initial and goal position
        self.initial_position = initial_position
        self.goal_position = goal_position

        # Define observation space: 
        # position x in the map
        # position y in the map
        self.map_shape = (4, 7)
        self.observation_space = Dict({'position_x': Discrete(self.map_shape[0]), 
                                       'position_y': Discrete(self.map_shape[1])})

        # risk with respect to fatal state
        self.risk = Box(low = 0, high = 1, shape = (1,))
        
        # Define Probability of action going down
        self.p_action_down = p_action_down

        # Define initial risk
        self.risk = initial_risk

        # Define initial state
        self.state = (self.initial_position[0], self.initial_position[1])

        # Define initial map
        # Agent's position: 1
        # Goal: 2
        # Fatal state: 3
        self.map = get_initial_map(self.initial_position, self.goal_position, self.map_shape)

    ###############################################

    def move(self, new_action):

        action = self. action_roulette(self, action)

        # Left
        if action == 0:
            state_transition = np.array([0, -1])

        # Up
        elif action == 1:
            state_transition = np.array([1, 0])

        # Right
        elif action == 2:
            state_transition = np.array([0, 1])

        # Down
        elif action == 3:
            state_transition = np.array([-1, 0])

        return state_transition
    
    ###############################################

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

    def valid_move(self, last_state, state_transition):

        new_state_x = last_state['position_x']
        new_state_y = last_state['position_y']

        state_transition_x = state_transition[0]
        state_transition_y = state_transition[1]

        if (new_state_x + state_transition_x) < self.map_shape[0] and (new_state_x + state_transition_x) > self.map_shape[0]:
            pass
        

        return new_state

    ###############################################

    def step(self, action):
        # Apply action
        self.action = self.action_roulette(self, action)
        
        # Get new state
        state_transition = self.move(action)

        last_position = self.state



        # Compute reward

        # Episode termination signal
        
        # Info
        info = {}
        pass

    ###############################################

    def render(self):
        pass

    ###############################################

    def reset(self):
        # Initial state
        self.state = get_initial_map(self.initial_position, self.goal_position, self.observation_shape)