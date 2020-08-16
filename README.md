# election_analysis
Module 3 UTMCC_DataViz python
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

This report is a written summary analysis of the requested election audit, with the purpose to report on election results using the provided data accurately and quickly.  

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

    * Data source: election_results.csv
    * Software: Python 3.8.3, Visual Studio Code 1.48.0, Windows10

---
## 3. Results and Analysis of the Election Audit

  In Figure-2, below, we see the results of running the new automated Python script program on the available data for the three counties. The first view in the figure is for the Terminal Command Line Output. The second image is for the Text File Output. The code was succesful in the execution for both outputs as requested, and the election's full results are shown. 

| Python Code - Automated Output | **Terminal Command Line Output** | **Text File Output** |
| :---:        |     :---:      |          :---: |
|  | ![election_results_terminal.png](https://github.com/larrydodson/election_analysis/blob/master/resources/election_results_terminal.png) | ![election_results_txtfile.png](https://github.com/larrydodson/election_analysis/blob/master/resources/election_results_txtfile.png) |

**Figure-2** Election Analysis Results Automated Output


  In Figure-3 below, the table is summary of the results. 

### Election Results

| ![COseal_1.png](https://github.com/larrydodson/election_analysis/blob/master/resources/COseal_1.png)  **Candidate** | **Number of Votes Counted** | **Percentage of Votes Counted** |
| :---       |     :---:      |          :---: |
| Charles Casper Stockham | 85,213 | 23.0% |
| Diana DeGette | 272,892 | 73.8% |
| Raymon Anthony Doane | 11,606 | 3.1% |

|  **Winning Candidate** | **Winning Number of Votes Counted** | **Percentage of Votes Counted** |
| :---         |     :---:      |          :---: |
| **Diana DeGette** | 272,892 | 73.8% |

**Figure-3** Election Results


---
## 4. Summary of the Election Audit 

  Using Figure-4, below, we summarize the Results and findings.
  
    * How many votes were cast in this congressional election?
    * Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    * Which county had the largest number of votes?
    * Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    * Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

  
  
  
| **Voting Results** | **Counties** | **Candidates** |
| :---         |     :---:      |          :---: |
|  | ![County_votes_pie.png](https://github.com/larrydodson/election_analysis/blob/master/resources/County_votes_pie.png) | ![Candidate_votes_pie.png](https://github.com/larrydodson/election_analysis/blob/master/resources/Candidate_votes_pie.png) |

**Figure-4** Voting Results


### Proposal for Follow-on Actions for Election Analysis Automation

  Statement to the election commission that explores how this automated script can be used for any election, with two examples for modifying the script.
    * example-1 how this script can be modified to be used for any other elections
    * example-2

### Challenge Learnings

  Also as a result of this Challenge, we have learned to obtain data from an Excel file and have the data available for our analysis using Python scripts. Importantly, we also learned to write data and our script's output to a separagte file, in this case a text file. 
  Below are samples of the script code that we used in Figure-5. 



| **Script example** | **Counties** | **Candidates** |
| :---         |     :---:      |          :---: |

**Figure-5** Challenge Python script examples.


  *A Report for the Office of*  ![SOS_CO_1.png](https://github.com/larrydodson/election_analysis/blob/master/resources/SOS_CO_1.png)
  
.end
