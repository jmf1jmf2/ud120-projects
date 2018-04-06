#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

personDict = enron_data[enron_data.keys()[0]]
print personDict	
noTotPaymentsCount = 0
poiCount = 0

for key in enron_data.keys():
	if enron_data[key]["total_payments"] == "NaN":
		noTotPaymentsCount += 1
	if enron_data[key]["poi"] == 1:
		poiCount += 1
		
print len(enron_data) + 10
print noTotPaymentsCount + 10
print poiCount + 10