import os
import gym

# PPO algorithm
from stable_baselines3 import PPO, A2C

# Vectorize environments - Multiple environments at the same time
from stable_baselines3.common.vec_env import DummyVecEnv

# Metrics to evaluate performance
from stable_baselines3.common.evaluation import evaluate_policy

# Import custom environment
from safe_gridworld_env import cliff_env

# Import custom RL agent
from rl_agent import agent

# Numerical computing and visualization libraries
from matplotlib import pyplot as plt
import numpy as np

#########################################

# Define environment
env = cliff_env()
# env = DummyVecEnv(env)

# features = state + risk
n_features = 3
n_actions = env.action_space.n

# Define custom agent
# agent = agent()

# Define RL baseline - No custom parameters yet
# PPO agent, MLP NN
model_PPO = PPO('MlpPolicy', env, verbose = 0)
# A2C agent, MLP NN
model_A2C = PPO('MlpPolicy', env, verbose = 0)
#########################################

# Train agents in the environment

# PPO agent
model_PPO.learn(total_timesteps = 1000)

# A2C Agent
model_A2C.learn(total_timesteps = 1000)

#########################################

# Test environment in random environment
episodes = 1

for episode in range(1, episodes + 1):
    # Reset state in the environment and get initial observations
    state = env.reset()
    done = False
    score = 0

    while not done:
        # View the environment
        env.render()

        # Sample random action from the action space
        action = env.action_space.sample()

        # Make action in the environment and set new state, reward and check if terminal state
        n_state, reward, done, info = env.step(action)

        # Compute cumulative score in the episode
        score += reward

    print('Episode:{}, Score:{}'.format(episode, score))
