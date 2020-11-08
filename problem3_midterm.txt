#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:11:25 2020

@author: NorinaSun
"""

def find_unique(full_list):
    unique = [] 
    for i in full_list: 
        if i not in unique: 
            unique.append(i) 
    return unique

def get_diffs(value_list):
    diff_list = []
    for j in range(0,len(value_list)):
        for i in range(j+1,len(value_list)):
            diff = abs(value_list[j] - value_list[i])
            diff_list.append(diff)
    return diff_list
        
#question two
def new_channel_check(new_channel,existing_channels):
    combined_channels = existing_channels + [new_channel]
    combined_diffs = get_diffs(combined_channels)
    
    if len(find_unique(combined_diffs)) != len(combined_diffs):
        valid = False
        print("new valid is invalid")
    else:
        valid = True
        print("new value is valid")
        
    return valid
         
# =============================================================================
# channels = [3,5,8]
# new_channel = 11
# 
# new_channel_check(new_channel, channels)
# 
# =============================================================================

#question three

def max_channels(values):
    
    selected_channels = []
    val = values[0]
    selected_channels.append(values[0])
    diff = 1
    diff_list = list(range(1,max(values)))
    
    while val + diff < max(values):
        val = val + diff
        if new_channel_check(val, selected_channels) == True:
            pass
        else: 
            while new_channel_check(val, selected_channels) == False:
                val = val + 1
            
        selected_channels.append(val)
        print("selected_channels",selected_channels)
        
        updated_diffs = get_diffs(selected_channels)
        
        for i in updated_diffs:
            try:
                diff_list.remove(i)
            except:
                pass
            
        diff = min(diff_list)
            
    return selected_channels

#validating
def validating(results):
    #print(find_unique(results))
    #print(results)
    if len(find_unique(get_diffs(results))) != len(get_diffs(results)):
        print("this selection is not valid")
    else:
        print("this selection is valid")

# =============================================================================
# test = range(1,200)
# validating(max_channels(test))
#          
# =============================================================================
