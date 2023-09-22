[![Python template with Github Actions](https://github.com/drktao/python-template/actions/workflows/main.yml/badge.svg)](https://github.com/drktao/python-template/actions/workflows/main.yml)

# IDS 706 Week 3 Mini-Project
This repo uses the python template generated in Week 1 to employ a polars script that provides descriptive statistics and data visualization. The script main.py contains two functions, one of which computes and displays descriptive statistics (mean, median, standard deviation) of a data column of interest, and the other of which generates a histogram of the data. The script test_main.py tests to ensure that the descriptive statistics are computed as expected.

The specific data set used in this project is a simple one; it contains all Robert De Niro movies and their corresponding Rotten Tomatoes scores. The data of interest are the scores themselves. 

## Instructions
Use Github codespaces, which will allow for a container to be built with the required packages, as detailed in requirements.txt. In the terminal, one can use `make install` to install all necessary packages from requirements.txt and upgrade the version of pip. After this, `make format` helps with visually-appealing formatting of the code. One can also use `make lint` to lint the code and `make test` to run the provided tests on the code. One can also directly run the scripts using `python main.py` and `python test_main.py`.

Running `python main.py` will also generate a summary report to the repo containing the summary statistics of the movie scores and the histogram visualization.
