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
        self.initial_risk = initial_risk
        self.risk = initial_risk

        # Define initial state
        self.state = (self.initial_position[0], self.initial_position[1])

        # Define state transition
        self.state_transition = {0: np.array([0, -1]),  # Left
                                 1: np.array([-1, 0]),   # Up
                                 2: np.array([0, 1]),   # Right
                                 3: np.array([1, 0])}  # Down

        # Define initial map
        # Agent's position: 1
        # Goal: 2
        # Fatal state: 3
        self.map = get_initial_map(self.initial_position, self.goal_position, self.map_shape)
        self.map_render = self.map

    ###############################################

    def move(self, new_action):

        action = self.action_roulette(new_action)

        state_transition = self.state_transition.get(action)

        return state_transition
    
    ###############################################

    def action_roulette(self, new_action):

        # Compute roulette value
        roulette_value = np.random.normal()

        # Compute percentile value, i.e. Probability(Z <= z) ~ self.p_action_down
        percentile = norm.ppf(self.p_action_down)

        # Change new action to down if roulette_value > percentile
        if (roulette_value > percentile):
            action = new_action
        else:
            action = 3

        return action

    def valid_move(self, last_state, state_transition):

        new_state_x = last_state[0]
        new_state_y = last_state[1]

        state_transition_x = state_transition[0]
        state_transition_y = state_transition[1]

        new_state_x = new_state_x + state_transition_x
        new_state_y = new_state_y + state_transition_y

        if (((new_state_x) >= 0 and (new_state_y) >= 0) and 
           (((new_state_x) < self.map_shape[0] and (new_state_y) < self.map_shape[1]))):
            flag_valid = True
            new_state = (new_state_x, new_state_y)
        else:
            flag_valid = False
            new_state = last_state

        return new_state, flag_valid

    def get_reward(self):
        # Compare the next state with the map
        type_state = self.map[self.state]

        # Setup flags
        flag_fatal = False
        done = True
        
        # Check if the state is either fatal, goal, or not
        if type_state == 3:     # Fatal state
            reward = -100
            flag_fatal = True
        elif type_state == 2:   # Goal state
            reward = 10
        else:                   # Normal state
            reward = -1
            done = False

        return reward, flag_fatal, done

    ###############################################

    def step(self, action):
        # Apply action
        # action = self.action_roulette(action)
        
        # Get new state
        state_transition = self.move(action)

        last_state = self.state

        new_state, flag_valid = self.valid_move(last_state, state_transition)
        
        self.state = new_state

        # Compute risk from current state to fatal state?
        
        # Compute reward, flag for fatal states, and done signal
        reward, flag_fatal, done = self.get_reward()
        
        # Info
        info = {flag_valid, flag_fatal}
        
        return self.state, reward, done, info

    ###############################################

    def render(self):
        self.map_render[self.state] = 1
        print("current state: {}".format(self.state))
        print(self.map_render)
        pass

    ###############################################

    def reset(self):
        # Initial state
        self.state = (self.initial_position[0], self.initial_position[1])
        self.risk = self.initial_risk

        
        self.map_render = self.map
#------DEBUGGING--------
env = cliff_env()
action = 0
env.step(action)
env.render()