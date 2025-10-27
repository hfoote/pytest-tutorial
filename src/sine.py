## Application code
import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod

class trigFunction(ABC):
	
	def __init__(self, amplitude, frequency, phase):
		
		self.amplitude = amplitude 
		self.frequency = frequency
		self.phase = phase

	@abstractmethod
	def __call__(self, x):
		pass
	
	@property
	def period(self):
		return 2*np.pi / np.abs(self.frequency)

	def plot(self, domain=[1, 2*np.pi]):
		x = np.linspace(domain[0], domain[1], 500)
		lines = plt.plot(x, self(x))
		return lines
	
class sinFunction(trigFunction):
	
	def __call__(self, x):
		return self.amplitude * np.sin(self.frequency * x - self.phase)

class cosFunction(trigFunction):
	
	def __call__(self, x):
		return self.amplitude * np.cos(self.frequency * x - self.phase)
	