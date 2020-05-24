# SRSA (Steam Recommender Systems Analysis)
> Taking <a href="https://store.steampowered.com/">Steam</a> data from <a href="https://cseweb.ucsd.edu/~jmcauley/datasets.html#steam_data">Julian Mcauley's Datasets</a> we analyzed the data using various Recommender Analysis methods to determine what method, or combination of methods, Steam most likely uses in their own recommender systems. We then wrote a paper explaining our ideas and processes to any new programmers or companies who are beginning to look into "monetizing their data."

<br>
---
> Take just 5 minutes to watch our analysis video...

[![SRSA Video](https://github.com/Chandler-Thompson/SRSA/blob/master/Report/PreziVideoPicture.png?raw=true)](https://prezi.com/v/jpnsimqigwam/untitled-video/)

---
<br>

## Recommender Systems Used
- Apriori (Association Rule Mining)
- KMeans
- Memory-Based
- Matrix Factorization
- KNN with z-score
- Slope One
- Co-clustering

<br>

## Tools Used
- <a href="https://scikit-learn.org/stable/">Scikit-Learn</a>
- <a href="https://pandas.pydata.org/">pandas</a>
- <a href="http://surpriselib.com/">Surprise</a>
- <a href="https://colab.research.google.com/notebooks/intro.ipynb#">Google's Colaboratory</a>

<br>

## Our Conclusion
> Overall we feel like the project was a success! We did not implement everything we wanted to at this point in time, but given more time we feel confident that we would have reached a better recommender system we could make with the given dataset. 

> Data mining is complicated with many aspects that can be difficult to understand for beginners. With this motivation in mind, we decided it best to compare and contrast different recommender algorithms on the same dataset in order to further clarify the strengths and weaknesses of each type of algorithm, given a specific scenario. 

> In working on this project and report we learned a lot more about recommender systems ourselves and the abstract concepts on which they worked and relied upon. High points included seeing our systems finish running and output results after minutes, to hours of reading in, and crunching, data. Or having a moment of epiphany realizing that of all the data we had, the only reliable and accurate indicator of a player’s interest in a game is their play time of that game. Low points included waiting 6.5 hours for the Apriori System to end, and then just staring at the output wondering if 6.5 hours is worth the data that we were given, another being the realization that KMeans clustering on high dimensional data is not exactly suitable. It was also great when we began to understand what makes Matrix Factorization such a great tool for recommending items.

> We implemented a few recommenders mostly from scratch, but the ones we could better test came from the Surprise library. This library is one that helps build and analyze recommender systems that work with rating data. While we couldn't properly test every algorithm we attempted, we did get results for a few that we could. And with the results we hope to better guide students or companies that are looking to adopt a recommender algorithm.

<br>

## Read More!
> Check out our paper under <a href="Report/Final Report.pdf">`/Report/`</a>

<br>

## The Team
| <a href="https://www.linkedin.com/in/richard-c-thompson/" target="_blank">**Richard C Thompson**</a> | <a href="https://www.linkedin.com/in/alfredo-nolasco/" target="_blank">**Al Nolasco**</a> |
| :---: |:---:|
| [![Richard C Thompson](https://avatars0.githubusercontent.com/u/6445925?s=200&u=edcfd7115ca072e0ab9eff05302af7b711715941&v=4)](https://www.linkedin.com/in/richard-c-thompson/)    | [![Al Nolasco](https://media-exp1.licdn.com/dms/image/C4D03AQEJP1jVN84w-w/profile-displayphoto-shrink_200_200/0?e=1596067200&v=beta&t=BANexZYHVZ5xDuuT0OL95B2SoqDtGZmvWKa2bPfgEgI)](https://www.linkedin.com/in/alfredo-nolasco/) |
| <a href="http://github.com/chandler-thompson" target="_blank">`github.com/chandler-thompson`</a> |  |
