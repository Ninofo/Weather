# Weather Project 

> This project aims to compare the precipitation of Seattle, WA and Detroit, MI from 01/01/2018 - 12/31/2022 to determine which city rains more.

---

## Project Overview

This project aims to determine if it rains more in Seattle, WA or Detroit, MI. This is accomplished by comparing the precipitation measured at weather stations in each city. The results of this project concluded that it rains more in Seattle than in Detroit. While both cities had similar average overall rainfall, the key finding that supported the conclusion was that Seattle experiences a statistically significant greater number of days of precipitation than Detroit for six months out of the year. 

- **Objective:** To determine if it rains more in Seattle, WA or Detroit MI based on the precipitation values
- **Domain:** Weather
- **Key Techniques:** data processing, cleaning, analyzing using python. 

---

## Project Structure

```
├── data/                 # Raw and processed data 
├── code/                 # Jupyter notebooks and Python scripts
├── reports/              # Generated reports and visualizations
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Data

- **Data Preparation:** A data frame (named 'df') was created with data subsets from the Seattle Weather station and Detroit Weather station. This new data frame includes precipitation values, the dates they were measured, and which city they were measured in. Values were imputed to fill the missing precipitation values from the Seattle weather station. df was converted to a tidy dataFrame.  Seen in .csv file "clean_Seattle_Detroit_weather" in the GitHub Repository.
- **Source:** Data was used from the NOAA (National Oceanic & Atmospheric Administrator) governmental website under National Centers for Environmental Information. Stations used was the Detroit Metro Airport, MI, US (ID:GHCND:USW00094847) and Seattle 2.1 ESE (ID:US1WAKG0225) https://www.ncei.noaa.gov/cdo-web/search?datasetid=GHCND
- **Description:** (Sattle_rain.csv , 91KB), (detroit_rain.csv, 138 KB), (clean_seattle_detroit_weather, 88 KB)
- **License:**

---

## Analysis

Analysis done in python using JupyterLabs and can be seen in "SEA_DTW_weather_Data_Processing_and_Analysis.ipynb" in repository. Read top to bottom to reproduce results. The Analysis is done using the "clean_Seattle_Detroit_weather.cvs" dataframe created in the same notebook previously listed. 
Start with importing pandas, numpy, matplotlib.pyplot and seaborn libraries for data analysis and visualization tools. Import stats from scipy for tools to perform statistical tests. I Imported the calendar to put month names in the data visualizations (graphs). I officially began my analysis using the describe() method to get basic statistical measures for the overall precipitation data, making sure to group by each city. From my initial impression I moved on to creating columns in data for precipitation averages by month and the number of days that experienced any precipitation in each city. The following analysis used seaborns barplot(), lineplot(), and boxplot() methods to create visualizations(graphs). These lead me to use 'stats' from scipy to perform a t-test for the precipitation averages by month. Then I used 'proportions_ztest' from statsmodels.stats.proportion to performed a z-test for the number of days each city experienced precipitation. The results of the above statistical tests were put in bar graphs using seaborns barplot() method and had statistically significant differences between the two cities in a given month notated with an asterisk over that month. 

---

## Results

The overall statistical measures taken for the overall precipitation values by city showed similar mean values for Seattle and Detroit.They also experienced similar precipitation maxes. Implying that they get similar amounts of precipitation overall. 
The average amount of precipitation each city experienced each month also supported the earlier finding of having similar precipitation averages overall. The key difference was in season. Detroit experienced statistically greater precipitation averages in late spring and summer for 4 months, while Seatlle experienced statistically greater precipitation averages in winter for 4 months. 
The key finding was that the proportion of days each city experienced with precipitation. Looking at the proportions by month, Seattle experienced a more statistically significant number of months with days of precipitation. Seattle experienced more days of precipitation than Detroit for 6 months.  
Be advised that the initial graph depicting all the precipitation values for each city over the entire 5 years they were measured provided limited insights but did show less precipitation in Detroit over 2022. This could imply an unprecedented weather phenomenon that resulted in less precipitation in that year for Detroit. 

---

## Authors

- Nina Fossen - [ninofo](https://github.com/ninofo)

---

## License

Not applicable/not found

---

## Acknowledgements

- Tools/libraries used include pandas, numpy, matplotlib.pyplot, seaborn, stats from scipy, and proportions_ztest from statsmodels.stats.proportion 
- Inspiration from the DATA 5100-02 Foundations of Data Science from Seattle University 
