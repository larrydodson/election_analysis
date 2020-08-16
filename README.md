# election_analysis
Module 3 UTMCC_DataViz python Election Audit
---
## Contents

### 
  1. Project Overview - Purpose and Objectives
  2. Resources
  3. Results: Analysis of the Election Audit
  4. Summary 
---

## 1. Project Overview

### **Purpose**    

The Colorado Secretary of State is responsible for its elections, and an employee of the Board of Elections, Tom, has requested our assistance with providing an election data analysis audit for a recent congressional race. 

Tom's request includes that we build analysis and audit tools that would allow his office to have an automated process utilizing Python programming. The goal for automation is to replace the current manual method of using Excel, improving the accuracy and quality of the elections results. An automated process would be used for analyzing election results for future elections within Colorado.  

This report is a written summary analysis of the election audit project, with the purpose to report on election results using the provided data accurately and quickly.  

**Figure-1** Election Subjects, Colorado Counties of Arapahoe, Denver, Jefferson  ![counties_map.png](https://github.com/larrydodson/election_analysis/blob/master/resources/counties_map.png)


### **Objectives**

This Audit Report presents the following results:
  - voting volume counts total
  - vote counts and percentage of votes per county 
  - vote counts and percentage per candidate
  - the election results for each candidate
  - determine the winning candidate. 


---
## 2. Resources
  - Data source: election_results.csv 
  - Software: Python 3.8.3, Visual Studio Code 1.48.0, Windows10

---
## 3. Results: Analysis of the Election Audit

  In Figure-2, below, we see the results of running the new automated Python script program on the available data for the three counties. The first view in the figure is for the Terminal Command Line Output. The second image is for the Text File Output. The code was succesful in the execution for both outputs, and the election's full requested results are shown. 

| Python Code - Automated Output | **Terminal Command Line Output** | **Text File Output** |
| :---:        |     :---:      |          :---: |
|  | ![election_results_terminal.png](https://github.com/larrydodson/election_analysis/blob/master/resources/election_results_terminal.png) | ![election_results_txtfile.png](https://github.com/larrydodson/election_analysis/blob/master/resources/election_results_txtfile.png) |

**Figure-2** Election Analysis Results Automated Output


.

  In Figure-3 below, the table is a view of the analysis results.

### Election Results

| ![COseal_1.png](https://github.com/larrydodson/election_analysis/blob/master/resources/COseal_1.png)  **Candidate** | **Number of Votes Counted** | **Percentage of Votes Counted** |
| :---       |     :---:      |          :---: |
| Charles Casper Stockham | 85,213 | 23.0% |
| Diana DeGette | 272,892 | 73.8% |
| Raymon Anthony Doane | 11,606 | 3.1% |
| Total Votes Cast | 369,711 | |

|  **Winning Candidate** | **Winning Number of Votes Counted** | **Percentage of Votes Counted** |
| :---         |     :---:      |          :---: |
| **Diana DeGette** | 272,892 | 73.8% |

**Figure-3** Election Results


---
## 4. Summary of the Election Audit 

  From the Figures above, and referencing Figure-4 below, we summarize the Results and findings of this audit. In this election: 
  - total votes = 369,711 votes
  - for each of the three counties: 
      - Arapahoe: 24,801 votes at 6.7% of the total votes
      - Denver:  306,055 votes at 82.8% of the total votes
      - Jefferson: 38,855 votes at 10.5% of the total votes
  - Denver County had the largest number of votes at 306,055
  - for each of the three candidates, please see Figure-3 above for number of votes and the percentage of total votes for each candidate
  - The election winner was candidate Diana DeGette with 272,892 votes at 73.8% of the total votes placed. 
  
| **Voting Results** | **Counties** | **Candidates** |
| :---         |     :---:      |          :---: |
|  | ![County_votes_pie.png](https://github.com/larrydodson/election_analysis/blob/master/resources/County_votes_pie.png) | ![Candidate_votes_pie.png](https://github.com/larrydodson/election_analysis/blob/master/resources/Candidate_votes_pie.png) |

**Figure-4** Voting Results


### Recommendation for Next-step Actions for Election Analysis Automation

  Proposal to the Board of Elections: The new Election Analysis and Audit Program, run in Python, was successful in automating the election count process and accurately determining the winner. In order to use the Program for any future elections, we propose that it be updated and improved in these two example areas.:  
  
  - Data entry: The script code can be modified with the ability to input data from any typical data source that the Board of Elections has avialable, with the example of manual data input that has been required from mail-in-ballots, whre the manual entry is included within the code as from a keyboard or touch screen.
  - To test and improve the code for increased capacity and reliability. When the expectatio of using the automated solution for all counties in the state, there will be much higher data file sizes, and this will indicate an increased need for processing power and time. The code can be modified, or scaled up, and tested for reliability and accuracy for the time it will used for the entire state elections.


### Challenge Learnings

  In this Challenge, we have learned to obtain data from a csv file and have the data available for our analysis using Python scripts. Importantly, we also learned to write from our script's output to a separate text file. 
  In Figure-5 below are samples of the script code. 


| **Code example** | **accessing csv file data using the CSV Module, and converting to a dictionary** | **writing to a text file with the write function** |
| :---         |     :---:      |          :---: |
|  | ![gettingfrom_csv.png](https://github.com/larrydodson/election_analysis/blob/master/resources/gettingfrom_csv.png) | ![writingto_txt.png](https://github.com/larrydodson/election_analysis/blob/master/resources/writingto_txt.png) |
|  |  |  |


**Figure-5** Challenge Python script examples.




.


*A Report for the Office of*  ![SOS_CO_1.png](https://github.com/larrydodson/election_analysis/blob/master/resources/SOS_CO_1.png)  

.end
