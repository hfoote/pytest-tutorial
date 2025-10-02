## Application code
import matplotlib.pyplot as plt
import numpy as np

class sinFunction:
	
	def __init__(self, amplitude, frequency, phase):
		
		self.amplitude = amplitude 
		self.frequency = frequency
		self.phase = phase

	def __call__(self, x):
		return self.amplitude * np.sin(self.frequency * x - self.phase)
	
	def get_period(self):
		return 2*np.pi / np.abs(self.frequency)

	def plot(self, domain=[1, 2*np.pi]):
		x = np.linspace(domain[0], domain[1], 500)
		lines = plt.plot(x, self(x))
		return lines