# PythonTutorial
Python tutorial for Karolinska Lab (Jan 2020)

# Installation 

Clone this repository with    
``` git clone git@github.com:mnikolop/PythonTutorial.git ```
# Usage

This project includes the same code in 3 different versions of the same code.   
The different versions are written for the different platforms the project can be run and changes have been made to account for the different technologies.

## For Colaboratory users

The relevant file is 
```KarolinskaTutorial-Colab.ipynb```.   
The file contains a link to opening it in your own colab account. 

For this to run the following are needed:
- A google account.
- The ```dtp3_immunized_percent_of_one_year_olds.csv``` file to be uploaded in the directory Colab creates in the user's drive account.

## For Anaconda users

The relevant file is 
```KarolinskaTutorial-Conda.ipynb```.   

For this to run the following are needed:
- Python3 [installation](https://www.python.org/downloads/)
- Anaconda [installation](https://www.anaconda.com/distribution/)
- A python3 kernel with some libraries installed. Can be found in the repository. This environment is provided in the repository.

## For local runtime

The relevant file is 
```KarolinskaTutorial-Local.ipynb```.   

For this to run the following are needed:
- Python3 [installation](https://www.python.org/downloads/)
- Python compatible code editor
- Install the following libraries with pip:
    ```pip install seaborn```
    ```pip install matplotlib```
    ```pip install gapminder```
    ```pip install pandas```
    ```pip install unicodecsv```