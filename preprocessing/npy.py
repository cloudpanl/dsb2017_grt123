#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 11:13:41 2018

@author: ly
"""

import numpy as np
import os
import matplotlib.pyplot as plt

import matplotlib.animation as animation


prep_folder='/home/ly/data/dsb2017/sample_processing'






def animate(box, gifname):
    # Based on @Zombie's code
    fig = plt.figure(figsize=[16,9])
    plt.axis("off")
    anim = plt.imshow(box[0], cmap=plt.cm.gray)
    def update(i):
        anim.set_array(box[i])
        return anim,
    
    a = animation.FuncAnimation(fig, update, frames=range(len(box)), interval=100, blit=True)
    a.save(gifname, writer='imagemagick')


file_list=os.listdir(prep_folder)
file_list=filter(lambda x:x.split('_')[-1]=='clean.npy' , file_list)

for patient in  file_list:
    patient_id=patient.split('_')[0]
    dis_dir=os.path.join(prep_folder,patient_id)
    
#    if not os.path.exists(dis_dir):
#        os.makedirs(dis_dir)
    npy_path=os.path.join(prep_folder,patient)
    npy_matrix=np.load(npy_path)[0] 
    n_slices=npy_matrix.shape[0]
    #for i in range(n_slices):
    #    plt.axis('off')
    #    plt.imshow(npy_matrix[i],cmap=plt.cm.gray)
    #    plt.savefig(os.path.join(dis_dir,str(i)+'.jpg'))
    
    pat=[npy_matrix[i] for i in range(n_slices)]

    animate(pat, os.path.join(prep_folder,patient_id+'.gif'))