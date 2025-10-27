## Unit tests
import matplotlib
import numpy as np
import pytest
from sine import sinFunction, cosFunction
from tests.e2e_test import AMP, FREQ, PHASE, TOL

@pytest.fixture
def sine_object():
	return sinFunction(AMP, FREQ, PHASE)

@pytest.fixture
def cos_object():
	return cosFunction(AMP, FREQ, PHASE)

def test_sineFunction_attributes_are_assigned(sine_object):
	assert sine_object.amplitude == AMP
	assert sine_object.frequency == FREQ
	assert sine_object.phase == PHASE

def test_sineFunction_returns_evaluation_when_called(sine_object):
	assert sine_object(-PHASE) < TOL
	assert (sine_object(np.pi - PHASE) - 1.) < TOL
	assert type(sine_object(0)) == np.float64

def test_cosFunction_returns_evaluation_when_called(cos_object):
	assert np.abs(cos_object(-PHASE) + AMP) < TOL
	assert np.abs(cos_object(np.pi - PHASE) + AMP) < TOL
	assert type(cos_object(0)) == np.float64

def test_sineFunction_calculates_period_correctly(sine_object):
	period = sine_object.period
	assert (period - np.pi) < TOL # pi is the expected answer for a frequency of 2
	assert type(period) == np.float64

def test_sineFunction_plot_returns_matplotlib_line_list(mocker, sine_object):
	mock_plot = mocker.patch("matplotlib.pyplot.plot")
	mock_plot.return_value = [matplotlib.lines.Line2D(xdata=[], ydata=[])]

	lines = sine_object.plot()
	assert type(lines) == list
	assert isinstance(lines[0], matplotlib.lines.Line2D)

def test_sineFunction_plot_calls_plot_correctly(mocker, sine_object):
	mock_plot = mocker.patch("matplotlib.pyplot.plot")

	low_bound = 0
	high_bound = 1
	sine_object.plot(domain=[low_bound, high_bound])
	
	x, y = mock_plot.call_args[0]
	assert np.allclose(x, np.linspace(low_bound, high_bound, 500))
	assert np.allclose(y, sine_object(x))
