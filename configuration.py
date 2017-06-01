import numpy as np

class Config(object):
    '''
    configuration used in deep net experiment 
    '''
    def __init__(self, batch_size, learning_rate, experiment_name, saver_dir, num_epoch, loss_type, log_dir, log_file, recon_dir, max_model_to_keep=200):
        self.batch_size = batch_size
        self.learning_rate = learning_rate 
        self.experiment_name = experiment_name
        self.saver_dir = saver_dir # 'Directory to save the trained model
        self.num_epoch = num_epoch # 'Number of epochs to run trainer
        self.loss_type = loss_type 
        self.log_dir = log_dir
        self.log_file = log_file
        self.recon_dir = recon_dir
        self.max_model_to_keep = max_model_to_keep #'max saved models'
