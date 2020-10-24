import random 
import numpy as np 
import scipy.stats as stats 
import matplotlib.pyplot as plt 
import statistics 
import math 
p = 0 #probability of arrival, to be varied over time 
r1 = 0.75 #probability that the a packet is switched to 1st port 
r2 = 0.25 #probability that the a packet is switched to 1st port 
T_Total = 100 #number of times repeating the simulation 
outlist1 = [] 
outlist2 = [] 
avg_list = [] 
packet_process_list = [] 
efficiency_list = [] 
packet_process_list_mean = [] 
prob_arrival = [] 
index1 = 0 
index2 = 0 
out_1_to_2 = [] 
out_1_to_1 = [] 
out_2_to_2 = [] 
out_2_to_1 = [] 
for j in range(T_Total): 
    p = np.random.rand() 
    prob_arrival.append(p) 
bufferlist1 = [] #input buffer for 1st input 
bufferlist2 = [] #input buffer for 2nd input 
index1 = 0 
index2 = 0 
packet_process = 0 
prob1 = np.random.rand(T_Total) 
prob2 = np.random.rand(T_Total) 
for i in range(T_Total): 
    # ------- ANALYSING PACKET ARRIVAL AT INPUT 1------------------ 
    #checking if in the previous iteration the packet was not transferred from input 1 
    #print('aya_01') 
    if(prob1[i] > p): #checking if the packet has arrived at input 1 
        bufferlist1.insert(i,1) #updating the bufferlist if arrived 
        transfer1 = np.random.rand() 
        if(transfer1 < r1): #checking where the packet wants to go 
            out_1_to_2.insert(i,1) #packet from 1 wants to go to 2 
            out_1_to_1.insert(i,0) 
        else: 
            out_1_to_1.insert(i,1) #packet from 1 wants to go to 1 
            out_1_to_2.insert(i,0) 
        else: 
            bufferlist1.insert(i,0) #updatinig the bufferlist if not arrived
            out_1_to_1.insert(i,0) 
            out_1_to_2.insert(i,0)
#----------- DOING THE SAME FOR INPUT 2 ---------------------
#  # #checking if in the previous iteration the packet was not transferred from input 2 
    if(prob2[i] > p): #checking if the packet has arrived at input 1 
        bufferlist2.insert(i,1) #updating the bufferlist if arrived 
        transfer2 = np.random.rand() 
        if(transfer2 < r2): #checking where the packet wants to go 
            out_2_to_1.insert(i,1) #packet from 1 wants to go to 2 
            out_2_to_2.insert(i,0) 
        else: 
            out_2_to_2.insert(i,1) #packet from 1 wants to go to 1 
            out_2_to_1.insert(i,0) 
        else: 
            bufferlist2.insert(i,0) #updatinig the bufferlist if not arrived 
            out_2_to_1.insert(i,0) 
            out_2_to_2.insert(i,0)
while(index1 != T_Total and index2 != T_Total): 
    #condition where both at 1 and 2 wishes to go to 2 
    if bufferlist1[index1] == 0 and bufferlist2[index2] == 0: 
        index1+=1 
        index2+=1 
    elif bufferlist1[index1] == 0 and bufferlist2[index2] == 1: 
        if (out_2_to_1[index2] == 1): 
            packet_process +=1 outlist1.append(1) 
    elif (out_2_to_1[index2] == 1): 
        packet_process +=1 
        outlist2.append(1) 
        index2 +=1 
        index1 +=1