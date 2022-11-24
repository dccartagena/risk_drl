import os
import numpy as np
import time, datetime
import matplotlib
import matplotlib.pyplot as plt

# Class for log, print, plot results from the RL algorithm
# Future version - Make dashboard? Or call tensorboard?

class data_logger:
    
    # Initialise data logger - Create or modify log-file
    # CSV file preferred 
    def __init__(self, save_dir = [], name_file = [], initial_transition = []):
        # Check if logging folder exist - Otherwise, create one
        if save_dir == 0:
            # Check if there are other folders with default name
            n_folder = 0
            
            # Name the new log folder
            save_dir = './new_experiment_{}'.format(n_folder)
        
        # Check if logging file exist - Otherwise, create one
        if name_file == 0:
            # Check if there are other folders with default name
            n_file = 0
            
            # Name the new log folder
            name_file = 'experiment_log_{}.csv'.format(n_file)
        
        # File path for logger
        file_path = os.path.join(save_dir, name_file)
        
        # Define parameters to log
        self.episode = 0
        self.step = 0
        
        if initial_transition == 0:
            self.state = 0
            self.action = 0
            self.next_state = 0
            self.reward = 0
        else:
            pass
        
        # Save initial parameters
        pass
    
    def log_step(self):
        pass
    
    def log_episode(self):
        pass
    
    def print_log(self):
        m_episode = 'episode: {}'.format(self.episode)
        pass
    
    def plot_results():
        pass