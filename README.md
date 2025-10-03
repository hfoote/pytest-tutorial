# pytest-tutorial
My tutorial materials on Python testing with pytest for the TIMESTEP Astronomical Software Engineering Internship, fall 2025. 

To follow along, clone this repo with 

`$ git clone https://github.com/hfoote/pytest-tutorial.git`

And install the example `sine` package with `pip install -e .` from the `pytest-tutorial` directory. Make sure to use the `-e` option to ensure you don't need to reinstall the package after making changes. 

## Tutorial notebook
A notebook containing a surface-level intro to `pytest` is located in `Tutorial/python_testing.ipynb`. I suggest starting here. You can run this locally, or go to it in your browser on github and replace "github.com" in the url with "githubtocolab.com" to run it on google colab.

## TDD exercise
The `main` branch of this repo is a small package called `sine`. Its tests are located in the `tests` directory. In the tutorial notebook, there is a prompt to stop and try writing some tests yourself according to a test-driven-development workflow. 

To do this, switch to the `exercise` branch of the repo with 

`$ git switch exercise`

This will remove the source code and unit tests for the `sine` package to let you try writing them yourself. At the end, you should end up with something like the `main` branch. 



