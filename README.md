# osiris
<p align="center">
<img src="https://dm2301files.storage.live.com/y4mmRC1xelS6Y6MEqUnZ-k2vjpADHpo6UMZAaZWROunr9-Ml5FYDlZ6WMxCGedy7NDhwDpusZdF5E1oLR5Qn6momydHe7tYUOMwNeFeGW7pUWkBjGPSnZp2sacYWs9IKkose6xjhSySL_v2tbfItRI7T_Pw_Tayhaa2F_vrwW6ucyr6WPa6s9DWH_if9Y5Y3yAU?width=375&height=250&cropmode=none"/>
</p>

[![img](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/allisterb/osiris/blob/master/notebooks/Overview.ipynb)

osiris is a Python data processing and analysis environment for data-based computational conflict forecasting using very large datasets and graph-based queries and  methods and models and visualization powered by scalable graph databases. To get started see the [notebooks](https://github.com/allisterb/osiris/notebooks), and also the [wiki](https://github.com/allisterb/osiris/wiki) for more in-depth technical info.


Information below is for my entry into the [TigerGraph Graph for All hackathon](https://graphforall.devpost.com/).


## Problem Statement: Predict Global Crises

Forecasting global crises in general and conflict and violence in particular is essential for economic policy-making and public- and private-sector disaster response and civil and police and military resource allocation. Very few phenomena have the impact on the economic stability and fortunes of countries like invasions, civil wars, insurgencies, global and domestic terrorism, civil unrest, strikes and blockades and other disruptive actions by essential workers, and so on. These crises often result in a complex set of further economic damage due to things like international sanctions, and knock-on crises in other countries like supply-chain shortages. But current qualitative and quantitative methods for analyzing and predicting human-initiated conflict and crises are not adequate e.g. [Philip Tetlock](https://www.stat.berkeley.edu/~aldous/Blog/tetlock2020.pdf):
>International politics poses a challenge for these methods because the laws governing the system are elusive or highly
debatable, relevant data points are often unavailable or unprecedented, and thousands of variables interact in countless ways.
History functions as a series of unfolding events, with highly contingent branching paths sometimes separated by mere
happenstance.Tectonic shifts can hinge on seemingly mundane occurrences.at makes it hard to deduce future events from
theoretical principles or to induce them from past experience...seasoned political experts had trouble outperforming “dart-tossing chimpanzees”—random guesses...when it came to predicting global events experts fared even worse against amateur news junkies.

From "[The perils of policy by p-value: Predicting civil conflicts](https://journals.sagepub.com/doi/10.1177/0022343309356491)" by Ward, Greenhill, and Bakke:
>Large-n studies of conflict have produced a large number of statistically significant results but little accurate guidance in terms of anticipating the onset of conflict. The authors argue that too much attention has been paid to finding statistically significant relationships, while too little attention has been paid to finding variables that improve our ability to predict civil wars.
>...
>The results provide a clear demonstration of how potentially misleading the traditional focus on statistical significance can be. Until out-of-sample heuristics — especially including predictions — are part of the normal evaluative tools in conflict research, we are unlikely to make sufficient theoretical progress beyond broad statements that point to GDP per capita and population as the major causal factors accounting for civil war onset

The rationalist approach to predicting crises and conflicts assumes there are theoretical models and casual structures we can discover using our reason that reveal the hidden order in global events. The empiricist approach does not make this assumption and seeks to make sense of the world and make predictions by finding patterns in observations and data. 

Data-driven forecasting is an essential activity in many key scientific areas like meteorology and climate studies and models for things like famine forecasting and mortgage repayment have been shown to be accurate. But human beings and societies have different properties from natural phenomena like hurricances and planets and black holes. Humans are rational, self-actualizing, purpose-driven entities, existing in a moral environment in addition to a physical and economic environment. The assumptions of uniform natural properties and relations and laws unvarying over time that are necessary for the inductive reasoning of traditional scientific prediction may not always hold for the actions of human beings and societies and countries in conflict. 

Even if we can use inductive and frequentist reasoning to predict human conflicts and crises, the nature of societies as *open, complex systems* may make prediction of crises intractable *unless we use the right models and methods and data.* 
![afcoin](https://dm2301files.storage.live.com/y4meKdvxRDnW5o5J4cpqeU-Si5wZWtmvANpnHfa8t72aVqXNUqGhpQDcID169QbA6Wn0wuOQXipOEEY0S31w8mk0v8GqiH6DYec5dt8YdxY3Y5Eh7IGTd5bdt1HliWfPDFYAC-J1QDQ98ZvJFC2bUMd6o3hl8U7-l9SYhuHTpgw3OuIjmL2-Y-AdXAqdxDQjvQO?width=848&height=619&cropmode=none)
<sub>From <a href="https://parusanalytics.com/eventdata/presentations.dir/Schrodt.Forecasting.Lecture1.pdf">"Forecasting Conflict Lecture 1 - Technical Political Forecasting: An Overview"</a> page 22 by Phillip A. Schrodt, 2013.</sub>

New types of data like *open event data* maybe more effective and faster in predicting conflict and crises e.g. Phil Schrodt "[Open Event Data and the Prospects for Near-RealTime Forecasting Models](https://parusanalytics.com/eventdata/presentations.dir/Schrodt.PRIO15.OpenSource.slides.pdf)":

>The combination of fully automated coding and the increasing number of reports on the web means that we now have an inexpensive
“instrument” for systematically monitoring global political behavior in real time...Structural indicators such as GDP, infant mortality, regime type, past or adjacent conflict change too slowly

Our inability to use better models and methods to forecast political conflict and crises and societal violence severely hinders our ability to craft effective economic policy and makes the world a more dangerous place.

![pol](https://dm2301files.storage.live.com/y4mOpcp6TX-t4AoBoXYnCDUIhHJcuGJm8JpJBf1TU8XrwnvFi2Ds-CfJvBmo_O1kPwVptYc9IQBiBM_VRDxkZTFSqRMz1fP5C0NGCocyc3H_qnC_LTiwhxyuAQejoG3lphg6tlYZ0l2lmNqVQicXA7fg8kVXnBvat2tQP7zUhl4NH6B7KPI9EK6Ctq7-sfVyXcG?width=2000&height=1600&cropmode=none)
*How can events like these be predicted?*

The ineffectiveness of existing qualitative and quantitative methods for predicting human- and state-initiated actions and crises and conflict does not imply a lack of causality or *patterns* in human actions or the futility of trying to predict globa crises and conflicts. Humans are rational actors even if our reasons for acting are deeply buried in our psyche and undetectable to external observers and self-reflection. 

Conflict between human actors and states can be naturally modelled as graphs and networks e.g consider the graph diagram below (click on the image if its too small)
![g](https://dm2301files.storage.live.com/y4m02Z0glxGHexjaEhMCGi825lIRrO_7YaKKWf9smTq6AoR_wCGOJjcfxUcP4h-HjEuVL3WjqOZCPFEQsKa-IUKjZlQDc1L-ysQI_LcmWQZrwtjEsEvHGEHA9C-m3Kqs0aaz_UJdBnJ0UuI2vTMpEIofQOCwT1KeZALS8CVj_nE6W-uG2u08V2l0QhUxHVOn9zx?width=1986&height=901&cropmode=none)

The diagram captures a tiny part of the conflict that erupted in the U.S. in the summer of 2020 during the presidency of Donald J. Trump. Organizations and movements like BLM and Antifa staged violent protests over the police killing of George Floyd  in response to which President Trump criticized these organizations and ordered further mobilization of police and other security forces.

The larger vertices outlined in orange represent *events* while the smaller vertices represent *actors*. Each event has spatio-temporal attributes and is [coded](https://en.wikipedia.org/wiki/Conflict_and_Mediation_Event_Observations) using a standard classification like `1823 KILL BY PHYSICAL ASSAULT` or `1453 ENGAGE IN VIOLENT PROTESTS TO DEMAND RIGHTS`.
Directed edges connect actors with events with each event being connected to a dyad or pair of actors where one actor is the *source* of the event action and the other the *target*. 

Using this model we can observe the following:
* Disparate events and actors may be coded using standard codes allowing consistent connections between them 
* Actors initiate and receive event actions and events connect to other events only through actor vertices.
* If an event A is possible cause of B then A must happen before B and a path must exist from B to A passing only through event vertices that also precede B.
* A sequence or chain of events leading to a violent event may show increasing levels of intensity e.g `1453 ENGAGE IN VIOLENT PROTESTS TO DEMAND RIGHTS` -> `153 MOBILIZE OR INCREASE POLICE POWER` -> `1823 KILL BY PHYSICAL ASSAULT`. The event coding can reflect this increase numerically with codes with a higher starting triple representing escalation.

 To effectively model and predict conflict we need to use new methods, of collecting observations of political *events* at a large-scale *population level*, of modelling those events in an appropriate way, and of using heuristics and *algorithms* to continuously make granular predictions about events and incorporate feedback about the quality of these predictions that can allow these algorithms to *iteratively* learn the hidden parameters in raw event data, that can create effective prediction models.   

Computational methods for data-driven forecasting using algorithms can be better than traditional statistical models with static parameters e.g. [Phil Schrodt](https://www.benjaminbagozzi.com/uploads/1/2/5/7/12579534/data-based-computational-approahes-to-forecasting-political-violence.pdf)
>Although more traditional “statistical” models still dominate quantitative studies
of political conflict, “algorithmic” approaches have proven effective, thus gaining
momentum not just within political science [21, 139] but also in other disciplines...
In general, by algorithmic approaches, we refer to specific models (such as neural
networks or random forests) or techniques (like bagging and boosting) that attempt
to leverage computational power to specify and train models through iterative
resampling techniques and to build and assess out-of-sample predictions, rather than
obtaining a single estimate of the model coefficients. Algorithmic approaches can
provide a number of benefits over statistical models...

Schrodt makes the following 6 points about algorithmic computational approaches to forecasting political violence:
 
* "Machine learning algorithms are often better suited than many traditional
statistical models at handling ‘big data’ data sets with large numbers of independent variables that potentially exceed the number of observations." 

* "Algorithms are also less dependent on rigid assumptions about the data generating
process and underlying distributions." 

* "As opposed to some statistical models, many machine learning algorithms were specifically designed to generate accurate
predictions, and do this exceedingly well." 

* "A number of the algorithmic approaches approximate the widely used qualitative method “case-based reasoning” which match patterns of events from past cases to the events observed in a current situation, and then use the best historical fit to predict the likely outcome
of the current situation...This similarity to the methods of human analysts accounted for these methods originally being labeled “artificial intelligence” in some of the early studies."

* "Major trends in the empirical study of political violence, such as the ‘big data’ revolution and an increasing interest in predictive models, mean that
algorithmic approaches will likely become increasingly popular in the coming years."

* "As with many of the algorithmic applications, *network models* have only become feasible in the last decade of so, as they require very substantial amounts of data and computational capacity. Consequently the number of applications at present is relatively small, though these are very active research areas."

There are very few (possibly none) freely-available solutions for effectively using network models and algorithmic approaches to conflict forecasting like graph deep learning on the massive amount of [automatically coded spatio-temporal political event data](http://data.gdeltproject.org/documentation/ISA.2013.GDELT.pdf)  from projects like [GDELT](https://www.gdeltproject.org/). There are many methods for [political event forecasting using deep-learning](https://arxiv.org/abs/2112.06345) and many open-source libraries available for doing deep learing including [graph deep learning](https://www.dgl.ai/), and the more data ML models are fed they better they perform. But researchers are not database experts and working with the large [tabular denormalized datasets](https://www.gdeltproject.org/data.html#rawdatafiles) GDELT provides is a daunting task. Even using the massive resources of [Google BigQuery](https://blog.gdeltproject.org/a-compilation-of-gdelt-bigquery-demos/), SQL queries for getting normalized GDELT data in a node-edge format suitable for graph analysis are complex, requiring multiple joins and subqueries, and very costly and slow to run. Just getting data into a CSV file for network analysis and visualization can be difficult as the raw GDELT data is split among thousands of files updated very 15mins and Google caps how much data an ordinary user can export to CSV out of BigQuery.



## Description

**osiris is a Python data processing and analysis environment for data-based computational conflict forecasting using very large datasets and graph-based queries and  methods and models and visualization powered by scalable graph databases.**


osiris is designed to allow researchers and workers in technical conflict forecasting to easily and effectively use statistical and algorithmic methods like graph deep learning on the massive amounts of automatically extracted and coded spatio-temporal political event data from the  [GDELT](https://www.gdeltproject.org/) large-scale event dataset. osiris tries to solve all the common problems of working with the enormous amounts of  GDELT data, from extracting the existing denormalized tabular data from Google BigQuery or the GDELT file server, to transforming it into a node-vertex schema and loading it into the graph database, to executing queries against graph data, to visualizing large graph datasets using Graphistry GPU-accelerated graph visualization.

![oo](https://github.com/allisterb/Mina/blob/master/docs/screencap_nb2.webp?raw=true)


## Dependencies

* Python 3.8+

## Installation
### Hardware requirements
osiris requires a TigerGraph instance with at least 32GB of RAM. Data loading into TigerGraph can take a lot of disk space so it's recommended you have at least 100GB available. On a 8vCPU x 32 GB RAM TigerGraph cloud instance with 100G disk storage, about 34M event vertices and 68M edges shaped from the [GDELT Events dataset](https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/) take about 20GB RAM abnd about 40GB disk space. This represents about a quarter of the 134M event vertices in the `osiris-347701.gdelt_snapshots.events_actors_20200400_` table on Google BigQuery which contains all GDELT events extracted and shaped from 2020-04-20 to 20220-04-20.

### CLI and Jupyter
1. Create a Python venv e.g `python -m venv osiris` and activate it.
2. Clone the repo and its submodules: `git clone https://github.com/allisterb/osiris --recurse-submodules`.
3. Run the install scripts: `install` on Windows or `./install` on Linux/macOS. This will install all the Python dependencies.
4. Run `osi --help` or `./osi --help` to see the list of osiris CLI commands. 
5. Set the `OSIRIS_GRAPH_SERVER_USER` and `OSIRIS_GRAPH_SERVER_PASS` with the admin user and pass to your TigerGraph server instance.
6. Run `osi graph https://osiris-dev.i.tgcloud.io _ query --file gsql/ddl_graph_GDELT_Events.gsql` to create the *GDELT_Events* graph
````
                                                                                                                                     
(osiris) root@alexander:~/Projects/osiris# osi graph https://osiris-dev.i.tgcloud.io _ query --file gsql/ddl_graph_GDELT_Events.gsql 
               __        __                                                                                                          
.-----.-----.|__|.----.|__|.-----.                                                                                                   
|  _  |__ --||  ||   _||  ||__ --|                                                                                                   
|_____|_____||__||__|  |__||_____|                                                                                                   
                                                                                                                                     
                                                                                                                                     
0.1.0                                                                                                                                
                                                                                                                                     
                                                                                                                                     
11:58:01 AM INFO     Using user tigergraph and password xxxM3 for graph server https://osiris-dev.i.tgcloud.io...                    
            INFO     Using file gsql/ddl_graph_GDELT_Events.gsql as query source.                                                    
            INFO     Executing query on graph ...                                                                                    
11:59:44 AM INFO     Executing query on graph  completed in 103.17 s.                                                                
Dropping all, about 1 minute ...                                                                                                     
Abort all active loading jobs                                                                                                        
Resetting GPE...                                                                                                                     
Successfully reset GPE and GSE                                                                                                       
Stopping GPE GSE                                                                                                                     
Successfully stopped GPE GSE in 0.005 seconds                                                                                        
Clearing graph store...                                                                                                              
Successfully cleared graph store                                                                                                     
Starting GPE GSE RESTPP                                                                                                              
Successfully started GPE GSE RESTPP in 0.072 seconds                                                                                 
Everything is dropped.                                                                                                               
Successfully created vertex types: [Event].                                                                                          
Successfully created vertex types: [Actor].                                                                                          
Successfully created edge types: [Acted].                                                                                            
Successfully created reverse edge types: [Action_Source].                                                                            
Successfully created edge types: [Action_Target].                                                                                    
Successfully created reverse edge types: [Acted_on].                                                                                 
Successfully created vertex types: [Story].                                                                                          
Successfully created edge types: [Mention].                                                                                          
Successfully created reverse edge types: [Mentioned_By].                                                                             
Stopping GPE GSE RESTPP                                                                                                              
Successfully stopped GPE GSE RESTPP in 30.310 seconds                                                                                
Starting GPE GSE RESTPP                                                                                                              
Successfully started GPE GSE RESTPP in 0.072 seconds                                                                                 
````
7. Create a secret for the REST++ API of your graph: `osi graph mytgserverurl mytgdb create-secret mysecret` e.g. `osi graph https://osiris-dev.i.tgcloud.io GDELT_Events create-secret s1`. Set the `OSIRIS_GRAPH_SERVER_SECRET` env var to the secret value.
8. Create a token for the REST++ API of your graph: `osi graph mytgserverurl mytgdb get-token` e.g. `osi graph https://osiris-dev.i.tgcloud.io GDELT_Events create-token` This command looks for the API secret needed in the  `OSIRIS_GRAPH_SERVER_SECRET` env var. Set the `OSIRIS_GRAPH_SERVER_TOKEN` env var to the token value.
9. Once your GSQL and REST++ auth env variables are set you can do `osi graph mytgserver mytgdb ping` to check connectivity to your graph server e.g. `osi graph https://osiris-dev.i.tgcloud.io GDELT_Events ping`.
10. Create the data load jobs for your graph `osi graph https://osiris-dev.i.tgcloud.io _ query --file gsql/ddl_jobs_GDELT_Events.gsql`.
11. Do a test data load using sample data e.g. `osi graph https://osiris-dev.i.tgcloud.io GDELT_Events load file actions_data file1 sample_data\actions_sample.csv`. Small osiris datasets as CSV files will be available on the osiris GitHub [releases](https://github.com/allisterb/osiris/releases) page.
12. To load data from the osiris datasets on Google BigQuery you'll need to have a [Google Cloud](https://cloud.google.com/) project and a service account and credentials to access BigQuery data. See the [Google docs](https://cloud.google.com/bigquery/docs/bigquery-storage-python-pandas) on how to create credentials to access BigQuery datasets and tables. You should set the `GOOGLE_APPLICATION_CREDENTIALS` env var to the location of your Google Cloud project credentials. With you credentials set you can say:
`osi graph https://osiris-dev.i.tgcloud.io GDELT_Events load bigquery actor_data file1 --table osiris-347701.gdelt_snapshots.events_actors_20200400_ --bs 100000 --maxrows 300000` To load 300000 *Actor* vertices using the `actor_data` job.
10. To start Jupyter server with the osiris notebooks you can say `jupyter notebook notebooks` in the osiris project root.
 
See the [installation](https://github.com/allisterb/osiris/wiki/Installation) and [data loading](https://github.com/allisterb/osiris/wiki/Data-Loading) pages and other pages of the [osiris wiki](https://github.com/allisterb/osiris/wiki) which contains more in-depth documentation.