from safe_gridworld_env import cliff_env

from plotting import plot_results

from rl_agent import agent

env = cliff_env()

rl_agent = agent()

plotter = plot_results()