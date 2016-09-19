# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 01:00:43 2016

@author: Leo

L1 error: (average difference between orig file and new file)
MSE error: 
"""

import numpy as np
from scipy.io import wavfile

try:
    import matplotlib.pyplot as plt
except:
    print 'matplotlib could not be loaded, plots are not available'

def compare_wavs(sound_1, sound_2, print_additional_comment='', plot=False):

    # Check files have same sample rate and length
    assert sound_1[0] == sound_2[0]
    assert sound_1[1].shape == sound_2[1].shape
    
    # L1 norm error'
    l1_err = np.abs(sound_1[1] - sound_2[1]).mean()
    
    # MSE (Mean Square Error)
    ms_err = np.square(sound_1[1] - sound_2[1]).mean()
    
    # Prints
    if print_additional_comment:
        print print_additional_comment
    print 'L1 error is {val}'.format(val=l1_err)
    print 'MSE is {val}'.format(val=ms_err)
    
    # Plot
    if plot:
        plot_files(sound_1, sound_2, print_additional_comment)

def plot_files(sound_1, sound_2, print_additional_comment='', side='left'):    
    
    sides = {'left':0, 'right':1}    
    
    plt.figure()
    plt.title(print_additional_comment)
    ax = plt.subplot(211)
    ax.step(range(sound_1[1].shape[0]), sound_1[1][:, sides[side]])
    ax.step(range(sound_2[1].shape[0]), sound_2[1][:, sides[side]])
    ax.set_title('Full wavs')
    
    ax = plt.subplot(212)
    ax.step(range(sound_1[1].shape[0]), sound_2[1][:, sides[side]] \
                        - sound_1[1][:, sides[side]]) 
    ax.set_title('Difference')

def normalise_by_std(sound_1, sound_2):
    return (sound_2[0], sound_2[1]*np.std(sound_1[1])/np.std(sound_2[1]))

if __name__ == '__main__':
    ## PARAMETERS

    # Files to load
    file_1_path = 'sound_card_test_new.wav'
    file_2_path = 'sound_card_test_real.wav'
    
    # Show plots (only if you have matplotlib):
    do_plot = False
    
    # RUN 
    # Open wave files and put in numpy array
    sound_1 = wavfile.read(file_1_path)
    sound_2 = wavfile.read(file_2_path)
    
    # Normalised by standard deviation
    sound_2_norm = normalise_by_std(sound_1, sound_2)
    
    # Compare new file and normalised new file with the original
    compare_wavs(sound_1, sound_2, '\n*** Orig file ***', plot=do_plot)
    compare_wavs(sound_1, sound_2_norm, '\n*** Normalised file ***', plot=do_plot)
