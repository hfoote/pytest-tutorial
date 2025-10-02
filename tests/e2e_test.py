import matplotlib
import numpy as np
from sine import sinFunction

# constants to specify the sine curve
AMP = 2.
FREQ = 2.
PHASE = -np.pi
TOL = 1e-10 # some small error tolerance to deal with floating-point math

def test_sin_class_functionality(mocker):
	# here, we know the user will want to plot the sine function, 
	# so we mock out the dependency on matplotlib again.
	mock_plot = mocker.patch("matplotlib.pyplot.plot")
	mock_plot.return_value = [matplotlib.lines.Line2D(xdata=[], ydata=[])] # we can assume plt.plot() returns a list of Line2D objects

	# A user wants to explore the behavior of a sine function. They define a sin curve, 
	sine = sinFunction(AMP, FREQ, PHASE)

	# and check that the value at x=0 is what they expect.
	assert np.abs(sine(0)) < TOL

	# Next, they extract the period of the sin curve,
	per = sine.get_period()

	# and check that the function has the same value after one period
	assert np.abs(sine(per)) < TOL 
	# and one half period
	assert np.abs(sine(per/2.)) < TOL 

	# finally, they plot the curve over two periods,  
	sin_plot = sine.plot(domain=[0, 2.*sine.get_period()])
	
	# and notice that they have been given the matplotlib Line2D object to modify if they choose. 
	assert isinstance(sin_plot[0], matplotlib.lines.Line2D)
