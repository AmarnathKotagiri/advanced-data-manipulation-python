[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8612751&assignment_repo_type=AssignmentRepo)
# Advanced Data Manipulation THA
In this assignment, you will use advanced functions in `Pandas` to query and filter your data. These functions reduce the workload by simplifying and reducing your code.

To submit, please perform the following:
1. Save a script file for Python with the following name: `tha_lastname_firstname.py` where lastname is your last name and firstname is your first name.
1. Save your screenshots of your output to the directory `assets`. This directory exists at the same leve as `data`.
1. Link your screenshots in `submission.md` where appropriate. That is, if you have screenshots supporting your answers, link those screenshots next to your answer.
1. Answer questions in `submission.md`, linking any screenshots as necessary.
1. Push your assignment to GitHub.

## COVID-19 Pandemic in the United States
In the previous assignment you scraped data from Wikipedia. This data came from a [statistical summary](https://en.wikipedia.org/wiki/Economic_impact_of_the_COVID-19_pandemic_in_the_United_States#Statistical_summary) with various data including job levels, umemployment rate, inflation rate. You will not scrape data for this assignment. Instead, import the data you exported in the ICE. So yes, this means you will copy the file from the other assignment over to this assignment. You will need to create a `data` directory.

## Rename Columns (1 pt.)
Import your `scraped_data.txt`. Once imported, rename columns like so: (1 pt.)
* `jobs_lvl` change to `jobs_lvl_1000`
* `jobs_mth` change to `jobs_month`
* `unemp_rate` change to `unemploy_rate`
* `unemp_mil` change to `unemploy_mil`
* `emp_pop` change to `employ_pop`
* `infl_rate` change to `infl_rate_perc`
* `snp500_mean` change to `snp500_mean_lvl`
* `public_debt` change to `public_debt_tril`
* `month` leave it as is

## Data Wrangling and Manipulation (9 pts.)
It is time to practice your data wrangling skills with Python. Please perform the following tasks. Take a screen capture of your output and link it in `submission.md`. 

Note, some of the tasks ask you to use regular expressions. Since we have not covered it yet in class, I have provided the regex syntax. If parentheses are included as part of the regex, include it. For example, I provide `(^j)` below. Thus, your code would be `.filter(regex='(^j)')`.

Ready? Let's go!
1. Calculate the mean of `jobs_lvl_1000`. (1 pt.)
1. Calculate the median of `jobs_lvl_1000`. (1 pt.)
1. Select all columns that start with a *j* (i.e., `(^j)`) **or** contain an *a* (i.e., `(a)`). Save it as a new data frame named `jobs_data_alt`.  (1 pt.)
1. Using your newly created data frame `jobs_data_alt`, select months in which `jobs_lvl_1000` was greater than 135,000. (1 pt.)
1. Using Pandas piping notation, perform the previous two operations together and save it as a new data frame `jobs_data_alt2`. This means you should select columns that start with a *j* or contain an *a* and select months in which `jobs_lvl_1000` was greater than 135,000. (2 pts.)

Please perform the following tasks. *Do not use* `jobs_data_alt` or `jobs_data_alt2`, but use the original data frame you initially created from the text file.
1. Using Pandas piping notation, select all columns that end with the letter *l* (i.e., `l$`) or contain the letter *o* (i.e., `o`). Additionally, select rows in which `snp500_mean_lvl` is greater than or equal to 3000. (2 pts.)
1. Using the query you just performed, calculate the mean and median of `jobs_lvl_1000`. How does it compare to the answers above? Please provide your answer in `submission.md`. (1 pt.)