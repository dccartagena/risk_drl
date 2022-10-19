# Import environment
from safe_gridworld_env import cliff_env

# Import RL agent
from rl_agent import agent

# Import plotting tools
from plotting import plot_results

# Make environment
env = cliff_env()

# Make RL agent
rl_agent = agent()

# Make plotting tools
plotter = plot_results()