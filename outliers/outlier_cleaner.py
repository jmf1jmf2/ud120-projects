#!/usr/bin/python



def outlierCleaner(predictions, ages, net_worths):

	def calculate_error(x, y):
		z = x-y
		return z**2
	
	from operator import itemgetter
	errors = (predictions - net_worths) ** 2
	#errors = map(calculate_error, predictions, net_worth)
	cleaned_data = zip(ages, net_worths, errors)
	cleaned_data.sort(key=itemgetter(2), reverse=True)
	to_remove = int(round(len(predictions*.1)))
	return cleaned_data[9:]
	
    ### your code goes here
	
	"""
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
	
    

