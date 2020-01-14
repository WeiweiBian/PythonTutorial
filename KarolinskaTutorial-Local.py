# # Python 
# 
# Python is an interpreted, high-level, general-purpose programming language.    
# Can be used for almost anything.   
# We are using it for data analysis.    
# Main library used in data analysis is pandas.   
# There used to be 2 version python2 (or python) and python 3. Since January 1st Python 2 has been depricated so we are only using python 3.
# 
# ## Main Resource
# - [python](https://www.python.org/)
# - [stackoverflow](https://stackoverflow.com/)
# - [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/)
# - [toward data science](https://towardsdatascience.com/)
# 
# ## Editors
# 
# Editors can be IDEs, text editors or notbooks.
# - [Anaconda](https://www.anaconda.com/): deployment environment
#   - [Jupyter](https://jupyter.org/): notebook
# - [VS Code](https://code.visualstudio.com/): text editor
# - [PyCharm](https://www.jetbrains.com/pycharm/): IDE
# - [Google Colab](https://colab.research.google.com/): notebook
# 
# 
# 
# # Libraries
# Libraries can contain datasets, tools, graphics, processes, functions and so on.
# They are basically what makes a language powerfull.
# 
# 
# **Note**: it is possible but not common that libraries have (slightly) different names for anaconda, only exist for anaconda or don't exist for it. 
# 
# **Other languages in python notebooks**   
# It is possible to run command lines from a notebook.
# Some notebooks also allow other languages to be mixed in as long as they are in separate cells and you specify the language (and of course it is suported).   
# For example Jupyter notebooks support Python, Java, R, Julia, Matlab, Octave, Scheme, Processing, Scala.   
# 
# ---
# 
# *Good Practice*   
# Different languages should be in their own cells.   
# It is common for kernels/runtime environments to not allow the mixing of languages in a cell.

# A lot of the libraries come pre-installed in the environments so we can just load them. 

#Import libraries
import numpy as np #basic scientific computation 
import pandas as pd #for data science
from gapminder import gapminder #dataset
import matplotlib.pyplot as plt #ploting 
import seaborn as sns; sns.set_style("darkgrid") #ploting
my_dpi=96 #dots per inch. Used in the size of the plots

import csv #library for handling csv files 

import statsmodels.api as sm #library for statistical modeling

import unicodecsv

# # Datasets
# Datasets are mostly used in the form of a dataframe in python.
# Datasets can be also found in the form of lists or dictionaries but in this workshop we will look into dataframes and specifically Pandas dataframes.   
# Dataframes are sets of data in a "table" format. 
# They come with a multitude of operations and functions they can be performed on them.
# 
# ## Loading datasets
# Dataframes can be loaded and created in many ways. Some of them are the following:
# - Library
# - Sample dataset
# - File
# - Online
# - Generated in scrip by typing in data
# 
# ### Loading from a library
# #### Overview and quick statistics
# 
# It is important to overview dataframes to
# - make sure we are looking at the correct data
# - identify potential errors and point of correction
# - know the datatypes and column names
# - know the ranges and basic statistics 

print(type(gapminder))


print(gapminder)


print("the first 5 lines of the dataframe are \n" , gapminder.head(), "\n") # print the first 5 lines of the df
print("the basic statistics of the dataframe are \n" , gapminder.describe(), "\n") # print basic info/statistics about the dataframe
print("the data types of the dataframe are \n" , gapminder.dtypes, "\n") # print the data types of the columns
print("the data types of the dataframe are (plus sparsity) \n" , gapminder.ftypes, "\n") # print more detailed info about the data types of the columns

# # Python and errors
# Python is very expressive.   
# This means you get loads of text when there is an error or a warning.  
# Only exceptions (that I have encountered so far) are out of bounds errors that are shown as keyError, That usually means that the position that is trying to be accesed doesn't exist or has a different index. 

# # Data Wrangling
# A big part of data wrangling is fixing the data types of columns.

gapminder['continent'] = pd.Categorical(gapminder['continent']) #change continent to categorical

# # Calling and casting
# 
# As we will see mostly bellow there is not need to define a variable before calling it for the first time.   
# 
# For casting types of data the data needs to be processed but the variable does not. 
# # Data Visualization
# Most of Python's good graphing libraries are libraries that have been migrated from other languages (R, Matlab).   
# The most common ones are matplotlib used in combination with seaborn, that allow the user to make plots ina similar way as ggplot does in R.

# graph data
for i in gapminder.year.unique(): #for every year in the data make the following graph
  fig = plt.figure(figsize=(680/my_dpi, 480/my_dpi), dpi=my_dpi) #create a figure
  tmp=gapminder[ gapminder.year == i ] #seperate the data to be graphed
  plt.scatter(tmp['lifeExp'], tmp['gdpPercap'] , s=tmp['pop']/200000 , 
              c=tmp['continent'].cat.codes, cmap="Accent", alpha=0.6, edgecolors="white", linewidth=2) #plot and colors
  plt.yscale('log') #set the scale of the y axis to logarythmic
  plt.xlabel("Life Expectancy") #set the label of the x axis
  plt.ylabel("GDP per Capita") #set the label of the y axis
  plt.title("Year: "+str(i) ) #set the title
  plt.ylim(0,100000) #set the scale of the y axis
  plt.xlim(30, 90) #set the scale of the x axis

# # Uploading data from file
# 
# Here we will try 
# - From local system
# - From google sheet
# 

with open('life_expectancy_years.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    lifeExpectancy = list(reader)
    
lifeExpectancy = pd.DataFrame(lifeExpectancy)

# # Data Wrangling (2)
# 
# Data are rarely in the correct format or type when loaded. 
# Common corrections that usually need to be done are:
# - Assigning a row as headers
# - Correcting the index
# - Correcting data types
# - Dealing with NAs or empty cells
# - ...
# 
# **Note**: A good practice would be to pass the original dataset first to a new one (with more appropriate name) so if something goes wrong the original data are unchanged. 

print(lifeExpectancy)

# **Note:** It is good practice to try your operations and when finalized make sure they work together.   
# For example, have one cell with all the finalized operations, one with testing and as soon as an operation is finalized move it with the rest of them.   
# Afterwards, reset your dataframe, run all the changes together and then see how they have affected the dataframe.

# ## Missing values 
# The dataset we are dealing with has a lot of NAs. There are many ways to deal with missing vallues, such as: 
# - Removing the columns with a certain threshold of NAs
# - Removing the rows with a certain threshold of NAs
# - Assigning the mean of the column to the missing value
# - Assigning the mean of the group to the missing value   
# 
# All of the above can be performed with the function ```pandas.DataFrame.dropna```.   

lifeExpectancy['country'] = pd.Categorical(lifeExpectancy['country']) #change country to categorical
lifeExpectancy = lifeExpectancy.set_index('country') #set country as index
lifeExpectancy = lifeExpectancy.unstack() #unstack the categories created by the new index
lifeExpectancy = lifeExpectancy.to_frame().stack(level=0) #stack the dataframe using the first level as columns
lifeExpectancy = lifeExpectancy.to_frame().swaplevel() #turn the rows to columns
lifeExpectancy.index.names = ['year', 'drop', 'country']
lifeExpectancy = lifeExpectancy.droplevel('drop')
lifeExpectancy.rename(columns={ lifeExpectancy.columns[0]: "expectancy" }, inplace = True)

print(lifeExpectancy)

immunization = pd.read_csv('dtp3_immunized_percent_of_one_year_olds.csv') #read the uploaded file to a df


print(immunization)

immunization['country'] = pd.Categorical(immunization['country']) #change country to categorical
immunization = immunization.set_index('country') #set country as index
immunization = immunization.unstack() #unstack the categories created by the new index
immunization = immunization.to_frame().stack(level=0) #stack the dataframe using the first level as columns
immunization = immunization.to_frame().swaplevel() #turn the rows to columns
immunization.index.names = ['year', 'drop', 'country'] #rename the index columns
immunization = immunization.droplevel('drop') #delete the 2nd level of teh index
immunization.rename(columns={ immunization.columns[0]: "dtp3" }, inplace = True) #rename the column without douplicating


print(immunization)


immunization = immunization.reset_index(drop=False) #reset the index

print(immunization)

demographics = gapminder[['continent', 'country']] #copy the columns continent and country from the gapminder data to a new df


expAndImmune = lifeExpectancy.merge(immunization, how='inner', on=['year', 'country']) #merge the life expectancy and immunization data based on the year and country columns
expAndImmune = expAndImmune.merge(demographics, how='outer', on='country').dropna() #merge the previous df with the demographics column 


print(expAndImmune)

# ## Handling douplicates
# A lot of merging operations generate douplicate entries, especially if they are outer joins. It is important to make sure that these are eliminated.   
# In this case we can just eliminate all but one of the douplicate entries, but in other cases you might ened to keep the second, or maybe last entry, or eliminate douplicates based on a specific column(s).   

expAndImmune = expAndImmune.drop_duplicates().reset_index(drop=True) 


# %%
print(expAndImmune.dtypes)

expAndImmune.dtp3 = pd.to_numeric(expAndImmune.dtp3)
expAndImmune.expectancy = pd.to_numeric(expAndImmune.expectancy)

# # Statistics
# 
# Grouping data is a very usefull function as it can provide an easier way of handling data and geting statistcs out of the groups.*italicized text*

# %%
print(expAndImmune.groupby(['continent']).max()) #find the max of each column for each continent
print(expAndImmune.groupby(['continent']).expectancy.max()) #find the max of the life expectancy for each continent
print(expAndImmune.groupby(['continent']).dtp3.min()) #find the min of the immunization data for each continent 


# %%
for continent, temp in expAndImmune.groupby(['continent']): #for each continent group the data and put it in a temp df
  print(continent, ':') 
  print(temp.groupby(['country'])['dtp3'].max().rename('max').sort_values(ascending = False).head(2).reset_index(drop=False)) #find the max of dtp3 immunization and print the first 2 rows in descending order
  print(temp.groupby(['country'])['expectancy'].max().rename('max').sort_values(ascending = True).head(3).reset_index(drop=False)) #find the max of life expectancy and print the first 3 rows in ascending order
  print("max values:\n", temp.max(), "\n")
  print("correlation of life expectancy and immunization to dtp3 is:\n", temp['expectancy'].corr(temp['dtp3']), "\n") # find the correlation of the life expectancy and immunization columns

# # Functions
# 
# in Python there is no need to define the variable type of an argument when creating a function.   
# A function starts after the ```:```and includes everythin that is indented. If the indentation stops the function ends.
# 
# 

# %%
def baseStats(data):
  for continent, temp in data.groupby(['continent']): #for each continent group the data and put it in a temp df
    print(continent, ':') 
    print(temp.groupby(['country'])['dtp3'].max().rename('max').sort_values(ascending = False).head(2).reset_index(drop=False)) #find the max of dtp3 immunization and print the first 2 rows in descending order
    print(temp.groupby(['country'])['expectancy'].max().rename('max').sort_values(ascending = True).head(3).reset_index(drop=False)) #find the max of life expectancy and print the first 3 rows in ascending order
    print("max values:\n", temp.max(), "\n")
    print("correlation of life expectancy and immunization to dtp3 is:\n", temp['expectancy'].corr(temp['dtp3']), "\n") # find the correlation of the life expectancy and immunization columns
    
    for country in temp.country.unique():
      # print(continent, country)
      tmp=temp[temp.country == country]
      fig = plt.figure(figsize=(680/my_dpi, 480/my_dpi), dpi=my_dpi) #create a figure
      plt.plot(tmp['year'], tmp['expectancy'], label="Life Expectancy") #plot and colors
      plt.plot(tmp['year'], tmp['dtp3'], label="Dtp3 immunization")
      plt.xticks(rotation=45)
      plt.legend(loc="upper left")
      plt.title(continent + " " + country) #set the title


baseStats(expAndImmune)

# # Saving to file
# 
# A easy as it is to load data from different sources it is as easy to save them back to a file. 
# 

expAndImmune.to_csv('expAndImmune.csv')

# # Predicting data
# 
# Like with other data science language we can performe predictive algorithms in python as well.
# We will use *predictive modelling* to find out the vallues for the next year in the data.   
# One of the most common methods of predictive modelling is *regression modeling*.   
# One of the most common mothods of regression modelling is *linear regression*.  
# First we want to graph our data in a scatter plot of the two variables we want to investigate, as well as checking their correlation.

fig = plt.figure(figsize=(680/my_dpi, 480/my_dpi), dpi=my_dpi) #create a figure
plt.plot(expAndImmune['dtp3'], expAndImmune['expectancy'], '.') #plot and colors

print(expAndImmune['expectancy'].corr(expAndImmune['dtp3'])) # print the correlation of the 2 variables
print(expAndImmune['dtp3'].corr(expAndImmune['expectancy'])) # print the correlation of the 2 variables

# Then we need to split our set to a predictor and a target set.   
# In this case this means that we will split one of our variables to use as a target value. For this example we will use the *life expectancy*.
# 
# 

target = expAndImmune[['expectancy']] #ceperate the expectancy column to a variable (df)

predictor = expAndImmune[['year', 'country', 'continent', 'dtp3']] #ceperate the other columns in a variable (df)

# The next step is to separate the two variables we will compare even more, and fit our model with them.

X = predictor.dtp3 # separate only the dtp3 variable as the predicting variable
y = target.expectancy # rename the target variable

model = sm.OLS(y, X).fit() # fit the model
predictions = model.predict(X) # make the predictions by the model

model.summary() # Print out the statistics

# # References
# - [Gapminder Data - Expectancy](http://gapm.io/ilex)
# - [Gapminder Data - Immunization](https://data.unicef.org/child-health/immunization.html)
# - [Gapminder data animation tutorial](https://python-graph-gallery.com/341-python-gapminder-animation/)
# - [Simple and multiple linear regression in python](https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9)
# 
