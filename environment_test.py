import gym
import numpy as np
import matplotlib.pyplot as plt 
import torch

# Make environment
env = gym.make("FrozenLake-v0") 

# Random seed
env.seed(0)

# Reset and render environment
env.reset()
env.render()

#----------- Functions ---------------------------------
# Epsilon-greedy method
def eps_greedy(env, curr_state, q_matrix, epsilon):
    # random number to compare
    random_roulette = np.random.uniform(0, 1)

    # epsilon roulette
    if (epsilon < random_roulette):

        # Take greedy action
        action = np.argmax(q_matrix[curr_state, :])
        
    else:

        # Take random action
        action = env.action_space.sample
    return action 

# Epsilon update method
def epsilon_update(epsilon, EPSILON_MIN, EPSILON_DECAY):
    epsilon = max(EPSILON_MIN, epsilon * EPSILON_DECAY)
    return epsilon

# Q-value matrix update
def update_q(q_matrix, curr_state, new_state, curr_action, reward, learning_rate, gamma):

    # Compute value function
    value_function = np.max(q_matrix[new_state, :])

    # Update Q-values
    q_matrix[curr_state, curr_action] = q_matrix[curr_state, curr_action] + learning_rate * (reward + gamma * value_function - q_matrix[curr_state, curr_action])
    # print(reward)

    return q_matrix

# Q-learning method
def qlearning_exploration(env, q_matrix, EPISODES, MAX_ITERATIONS, epsilon, EPSILON_MIN, EPSILON_DECAY, learning_rate, gamma):
    
    for i in range(EPISODES):
        curr_state = env.reset()

        for t in range(MAX_ITERATIONS):
            # Get epsilon-greedy action
            curr_action = eps_greedy(env, curr_state, q_matrix, epsilon)
            # print(curr_action)

            # Make action in the environment
            new_state, reward, done, info = env.step(curr_action)
            env.render()

            # Update Q-matrix
            q_matrix = update_q(q_matrix, curr_state, new_state, curr_action, reward, learning_rate, gamma)
            curr_state = new_state
            # print(q_matrix)

            # Update 
            epsilon = epsilon_update(epsilon, EPSILON_MIN, EPSILON_DECAY)

            # If done, break the loop
            if done:
                break

#-----------------------------------------------------------
# Define maximum number of iterations and number of episodes
MAX_ITERATIONS = 100
EPISODES = 100

# epsilon-greedy parameter
EPSILON_MIN = 0.0001
EPSILON_DECAY = 0.9999
epsilon = 0.2

# learning rate parameter
learning_rate = 0.1

# Discount factor
gamma = 0.9999

# Size of observation/action space
state_size = env.observation_space.n
action_size = env.action_space.n

# Create Q-matrix
q_matrix = np.zeros((state_size, action_size))

# Call the learning routine
qlearning_exploration(env, q_matrix, EPISODES, MAX_ITERATIONS, epsilon, EPSILON_MIN, EPSILON_DECAY, learning_rate, gamma)
