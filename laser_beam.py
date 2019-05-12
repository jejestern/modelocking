"""
We use python 2, since the used general_fit function is written in python 2. We wrote this program for an other project and we will reuse it now.

The aim of this script is to plot the meassured spectral distribution of CW and ML in the same plot with their refernce.

author: Jennifer Studer
"""

import numpy as np
import matplotlib.pyplot as plt
from my_general_fit import general_fit

# Getting the data
reference_cw = np.loadtxt(open('161202_cw'))
reference_ml = np.loadtxt(open('161202_modelocked'))
data_cw = np.loadtxt(open('CW_Messung_90'))
data_ml = np.loadtxt(open('ML_Messung_90'))

### Our goal is to create a function out of the reference points, so that we can use it as model. Like this we find out how much we have to shift and strecht our data, so that they fit with the ###reference.
#We create a function. It is connection of all points by straight lines.
def first_guess(ref_x, ref_y, x_range):
	if x_range <= ref_x[0] or x_range >= ref_x[-1]:
		return 0.0
		
	left = np.where(ref_x <= x_range)[0][-1]
	right = left + 1
	x = np.array([ref_x[left], ref_x[right]])
	y = np.array([ref_y[left], ref_y[right]])
	
	linear_coeff = np.polyfit(x, y, 1)
	
	return linear_coeff[0]*x_range + linear_coeff[1]

# We create the fit
def final(ref_x, ref_yf, data_xf, data_y, lim, kind):
	print kind, ":"
	ref_y = (ref_yf - min(ref_yf))/(max(ref_yf) -min(ref_yf) +0.0) #Normed and set min to zero
	
	provisional_function = np.vectorize(lambda x_range : first_guess(ref_x, ref_y, x_range))
	
	final_function = lambda parameters, data: provisional_function(parameters[0]*data + parameters[1])
	
	#We find the parameters of the final function to find out the shift and the stretch between reference and data points
	parameter, parameter_err, p_value = general_fit(data_xf, data_y, final_function, [1.0, 0.0])
	data_x = (data_xf - parameter[1] + 0.0)/parameter[0]
	
	#Plotting
	plt.plot(data_x, data_y, 'r.', label='Data points')
	plt.plot(ref_x, ref_y, 'k--', label='Reference')
	plt.xlabel('Wavelength [nm]')
	plt.ylabel('Relative Power')
	plt.xlim(lim[0], lim[1])
	plt.title('Fitted spectral distribution, '+ kind)
	plt.legend()
	plt.savefig(kind+'.pdf')
	plt.show()
	
	print "The p-value is ", p_value
	
	#We want to find the peak
	peak_x = data_x[np.argmax(data_y)]
	peak_y = data_y[np.argmax(data_y)]
	print "The peak is at ", peak_x, " nm"
	
	# Now we calculate the width at half high
	left_i = np.where(data_x < peak_x)[0]
	right_i = np.where(data_x > peak_x)[0]
	
	data_left = data_x[left_i]
	data_right = data_x[right_i]
	whm_left = data_left[np.where(data_y[left_i] <= peak_y/2.0)[0][-1]]
	whm_right = data_right[np.where(data_y[right_i] <= peak_y/2.0)[0][0]]
	print whm_right - whm_left




final(reference_cw[0], reference_cw[1], data_cw[0], data_cw[1], [760, 840], 'CW')
final(reference_ml[0], reference_ml[1], data_ml[0], data_ml[1], [700, 900], 'ML')










