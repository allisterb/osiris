# osiris
<p align="center">
<img src="https://dm2301files.storage.live.com/y4mmRC1xelS6Y6MEqUnZ-k2vjpADHpo6UMZAaZWROunr9-Ml5FYDlZ6WMxCGedy7NDhwDpusZdF5E1oLR5Qn6momydHe7tYUOMwNeFeGW7pUWkBjGPSnZp2sacYWs9IKkose6xjhSySL_v2tbfItRI7T_Pw_Tayhaa2F_vrwW6ucyr6WPa6s9DWH_if9Y5Y3yAU?width=375&height=250&cropmode=none"/>
</p>

Information below is for my entry into the [TigerGraph Graph for All hackathon](https://graphforall.devpost.com/).

## Predict Global Crises

Forecasting crises in general and conflict and violence in particular is essential for policy-making and public- and private-sector disaster response and civil and police and military resource allocation. Very few phenomena have the same impact on the economic and financial states of a country than wars, invasions, insurgencies, civil unrest, global and domestic terrorism, and so on. But current qualitative and quantitative methods for analyzing and predicting human-initiated conflict and crises are not adequate e.g. [Philip Tetlock](https://www.stat.berkeley.edu/~aldous/Blog/tetlock2020.pdf):
>International politics poses a challenge for these methods because the laws governing the system are elusive or highly
debatable, relevant data points are often unavailable or unprecedented, and thousands of variables interact in countless ways.
History functions as a series of unfolding events, with highly contingent branching paths sometimes separated by mere
happenstance.Tectonic shifts can hinge on seemingly mundane occurrences.at makes it hard to deduce future events from
theoretical principles or to induce them from past experience...seasoned political experts had trouble outperforming “dart-tossing chimpanzees”—random guesses...when it came to predicting global events experts fared even worse against amateur news junkies.

Forecasting is an essential activity in many key areas like climate studies and economics and finance. Our inability to forecast political conflict and societal violence makes the world a more dangerous place.

![pol](https://dm2301files.storage.live.com/y4mOpcp6TX-t4AoBoXYnCDUIhHJcuGJm8JpJBf1TU8XrwnvFi2Ds-CfJvBmo_O1kPwVptYc9IQBiBM_VRDxkZTFSqRMz1fP5C0NGCocyc3H_qnC_LTiwhxyuAQejoG3lphg6tlYZ0l2lmNqVQicXA7fg8kVXnBvat2tQP7zUhl4NH6B7KPI9EK6Ctq7-sfVyXcG?width=2000&height=1600&cropmode=none)
*Can events like these be predicted?*

The rationalist approach to predicting crises assumes there are theoretical models and casual structures we can discover using our reason that reveal the hidden order in global events. The empiricist approach does not make this assumption and seeks to make sense of the world and make predictions by finding patterns in observations and data. 

Computational methods for data-driven forecasting using *algorithms* can be better than traditional statistical models with static parameters e.g. [Phil Schrodt](https://www.benjaminbagozzi.com/uploads/1/2/5/7/12579534/data-based-computational-approahes-to-forecasting-political-violence.pdf)
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

* "As opposed to some statistical models,
many machine learning algorithms were specifically designed to generate accurate
predictions, and do this exceedingly well." 


* "A number of the algorithmic approaches approximate the widely used qualitative method “case-based reasoning” which match patterns of events from past cases to the events observed
in a current situation, and then use the best historical fit to predict the likely outcome
of the current situation...This similarity to the methods of human analysts accounted for
these methods originally being labeled “artificial intelligence” in some of the early
studies."

* "Major trends in the empirical study of political violence, such as the
‘big data’ revolution and an increasing interest in predictive models, mean that
algorithmic approaches will likely become increasingly popular in the coming
years."

* "As with many of the algorithmic applications, network models have only become feasible in the last decade of so, as they require very substantial amounts of data and computational capacity. Consequently the number of applications at present is relatively small, though these
are very active research areas."

There are very few (possibly none) freely-available solutions for effectively using graph-based models and algorithmic approaches to conflict forecasting like graph deep learning on the massive amount of [automatically coded spatio-temporal political event data](http://data.gdeltproject.org/documentation/ISA.2013.GDELT.pdf)  from projects like [GDELT](https://www.gdeltproject.org/). There are many methods for [political event forecasting using deep-learning](https://arxiv.org/abs/2112.06345) and many open-source libraries available for doing deep learing including [graph deep learning](https://www.dgl.ai/), and the more data ML models are fed they better they perform. But ressearchers are not database experts and working with the large [tabular denormalized datasets](https://www.gdeltproject.org/data.html#rawdatafiles) GDELT provides  is a daunting task. Even using the massive resources of [Google BigQuery](https://blog.gdeltproject.org/a-compilation-of-gdelt-bigquery-demos/), SQL queries for getting normalized GDELT data in a node-edge format suitable for graph analysis are complex, requiring multiple joins and subqueries and very costly and slow to run. Just getting data into a CSV file for network analysis and visualization can be very difficult as the raw GDELT is split among thousands of files updated very 15mins and Google caps how much data an ordinary user can export to CSV out of BigQuery.

## Description

**osiris is a Python data processing and analysis environment for data-based computational conflict forecasting using very large datasets and graph-based methods and models and visualization.**

Conflict in societies can be naturally modelled as graphs and networks e.g consider the graph diagram below 
![g](https://dm2301files.storage.live.com/y4m02Z0glxGHexjaEhMCGi825lIRrO_7YaKKWf9smTq6AoR_wCGOJjcfxUcP4h-HjEuVL3WjqOZCPFEQsKa-IUKjZlQDc1L-ysQI_LcmWQZrwtjEsEvHGEHA9C-m3Kqs0aaz_UJdBnJ0UuI2vTMpEIofQOCwT1KeZALS8CVj_nE6W-uG2u08V2l0QhUxHVOn9zx?width=1986&height=901&cropmode=none)

The diagram captures a tiny part of the conflict that erupted in the U.S. in the summer of 2020 during the presidency of Donald J. Trump. Organizations and movements like BLM and Antifa staged violent protests over the police killing of George Floyd  in response to which President Trump criticized these organizations and ordered further mobilization of police and other security forces.

The larger vertices outlined in orange represent *events* while the smaller vertices represent *actors*. Each event has spatio-temporal attributes and is [coded](https://en.wikipedia.org/wiki/Conflict_and_Mediation_Event_Observations) using a standard classification like `1823 KILL BY PHYSICAL ASSAULT` or `1453 ENGAGE IN VIOLENT PROTESTS TO DEMAND RIGHTS`,
Directed edges connect actors with events with each event being connected to a dyad or pair of actors where one actor is the *source* of the event action and the other the *target*. Using this model we observe:

* Actors initiate and receive event actions and events connect to other events only through actor vertices.
* If an event A is possible cause of B then A must happen before B and a path must exist from B to A passing only through event vertices that also precede B.
* A sequence or chain of events leading to a violent event may show increasing levels of intensity e.g `1453 ENGAGE IN VIOLENT PROTESTS TO DEMAND RIGHTS` -> `153 MOBILIZE OR INCREASE POLICE POWER` -> `1823 KILL BY PHYSICAL ASSAULT`. The event coding reflects this increase numerically.
* A typical news day globally would comprise a network of tens of thousands of event vertices and edges like these.

This global event data may be harvested from the massive amount of news stories published and available online each day where a *story* will *mention* a particular event on a particular date together with the actors involved. A schema in TigerGraph for this model of events and news would look like
![gdelt_event_schema](https://dm2301files.storage.live.com/y4mEJMfRYpOgh_8PPTHp-k45OLbUuXThve4zBdAg-FZ7cR8JjtxaahKI-l0n8dSXoPKQA1QOvaIOW5YOpkA2mMuE1VCkQlIDyCjmoEaJHgy3Uxfpq_ZLOB5SBw88JfjT8zq2K-IwXbkfmIl7fHPMpVahvTG1ASLOPf3UGKo4gDH6HS6O7RlaYptEPu3gMhp2Jjw?width=1535&height=705&cropmode=none)

osiris is designed to allow researchers and workers in technical conflict forecasting to easily and effectively use statistical and algorithmic methods like graph deep learning on the massive amounts of automatically extracted and coded spatio-temporal political event data from the  [GDELT](https://www.gdeltproject.org/) large-scale event dataset. osiris tries to solve all the common problems of working with the enormous amounts of  GDELT data, from extracting the existing denormalized tabular data from Google BigQuery or the GDELT file server, transforming it into a node-vertex schema and loading it into the graph database, to executing queries against graph data, and visualizing large graph datasets using Graphistry GPU-accelerated graph visualization.

![oo](https://github.com/allisterb/Mina/blob/master/docs/screencap_nb2.webp?raw=true)


## Dependencies

* Python 3.8+

## Installation
### CLI and Jupyter
1. Clone the repo and its submodules: `git clone https://github.com/allisterb/osiris --recurse-submodules`.
2. Run the install scripts: `install` on Windows or `install.sh` on Linux/macOS. This will install all the Python dependencies.
3. Run `osi --help` or `osi.sh --help` to see the list of osiris CLI commands.
4. Run `set_gsql_auth_env[.sh] mytguser mytgpass` with the GSQL user and pass to your TigerGraph server instance.
5. If you need to create a secret for the REST++ API of your server you can say `osi[.sh] graph mytgserverurl mytgdb create-secret mysecret` e.g. `osi graph https://osiris0.i.tgcloud.io GDELT_Events create-secret s2` assuming your GSQL user has the right permissions.
6. If you need to get a token for the REST++ API of your server you can say `osi[.sh] graph mytgserverurl mytgdb get-token` e.g. `osi graph https://osiris0.i.tgcloud.io GDELT_Events get-token` This command looks for the API secret needed in the  `OSIRIS_GRAPH_SERVER_SECRET` env var.
7. Run `set_restpp_auth_env[.sh] mytgtoken` with the REST++ API token for your TigerGraph server instance.
8. If your GSQL and REST++ auth env variables are set you can do `osi[.sh] graph mytgserver mytgdb ping` to check connectivity to your graph server e.g. `osi graph https://osiris0.i.tgcloud.io GDELT_Events ping`. 

10. To start Jupyter server run `start_jupyter[.sh] path_to_my_notebooks` e.g. `start_jupyter notebooks`.
 
