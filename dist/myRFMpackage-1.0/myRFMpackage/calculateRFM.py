#!/usr/bin/env python3
"""
#########################################################################################
Copyright (c) 2016. All rights reserved.  See the file LICENSE for
license terms.
#########################################################################################

File: LE_Packages.py
Proj: Python Workshop
Desc: A non-technical introduction to Python, 
Auth: Sylvia Schumacher
Date: 2017/12/01
"""
#%%
"""
####################################################################
Exercise 1: Create your first package
####################################################################
"""
#%%
import pandas as pd
import numpy as np
#%%
def calculateRFM(data, weight_recency=1, weight_frequency=1, weight_monetary=1):

    """
    Calculate a weighted RFM score: recency, frequency, and 
    monetary for every customer.

    @param data: A pandas DataFrame containing the transaction 
        record details for every customer.
    @param weight_recency: Weight of recency
    @param weight_frequency: Weight of frequency
    @param weight_monetary: Weight of monetary
    
    @return: a pandas DataFrame containing receny, frequency and monetary
    score as well as the weighted final score and the group membership
    
    @raise keyError: raises an exception
    """
    # Ensure that the weights add up to one
    weight_recency2 = weight_recency/sum([weight_recency, weight_frequency, 
                                          weight_monetary])
    weight_frequency2 = weight_frequency/sum([weight_recency, weight_frequency, 
                                              weight_monetary])
    weight_monetary2 = weight_monetary/sum([weight_recency, weight_frequency, weight_monetary])
    
    # RFM measures
    max_Date=max(data["TransDate"])
    rfm=data.groupby("Customer", as_index=False).agg({"TransDate":"max",#recency = difference between latest transaction and "today"
                    "Quantity": "count", #frequency = number of transactions
                    "PurchAmount":"mean"}) #monetary = average amount spent per transaction
    #rename the colums
    rfm.rename(columns = {"TransDate":"Recency", "Quantity":"Frequency", "PurchAmount": "Monetary"}, inplace=True)
    #recency is defined as max.date - last purchase
    rfm["Recency"]=max_Date-rfm["Recency"]
    #make sure recency is numeric
    rfm["Recency"]=rfm["Recency"].dt.days

    # RFM scores
    #recency
    bins_freq = [-0.1, 1000, 2000, max(rfm["Recency"])] 
    scores_recency = ["3","2","1"] #decreasing for recency
    rfm["Recency2"] = pd.cut(rfm["Recency"], bins_freq, labels=scores_recency)
    rfm["Recency2"]=rfm["Recency2"].cat.codes+1
    #frequency
    bins_freq=[-0.1,1,3,max(rfm["Frequency"])]
    scores_others=["1","2","3"]
    rfm["Frequency2"] = pd.cut(rfm["Frequency"], bins_freq, labels=scores_others)
    rfm["Frequency2"]=rfm["Frequency2"].cat.codes+1
    #monetary
    bins_mon=[-0.1,50,100,max(rfm["Monetary"])]
    rfm["Monetary2"] = pd.cut(rfm["Monetary"], bins_mon, labels=scores_others)
    rfm["Monetary2"]=rfm["Monetary2"].cat.codes+1

    # Overall RFM score
    rfm["finalscore"]=rfm["Frequency2"]*weight_frequency2+rfm["Monetary2"]*weight_monetary2+rfm["Recency2"]*weight_recency2
    
    # RFM group
    rfm["group"]=round(rfm["finalscore"])
    
    return rfm
#%%
