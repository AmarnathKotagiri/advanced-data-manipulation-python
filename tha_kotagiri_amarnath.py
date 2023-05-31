import os
import pandas as pd

dir = r"F:\MIS-PDS\advanced-data-manipulation-tha-AmarnathKotagiri\data"
os.chdir(dir)

ScrapedData = pd.read_table(dir+r'\scraped_data.txt', sep='\t')

ScrapedData=ScrapedData.rename(columns={
    "jobs_lvl":"jobs_lvl_1000",
    "jobs_mth":"jobs_month",
    "unemp_rate":"unemploy_rate",
    "unemp_mil":"unemploy_mil",
    "emp_pop":"employ_pop",
    "infl_rate":"infl_rate_perc",
    "snp500_mean":"snp500_mean_lvl",
    "public_debt":"public_debt_tril"
})

print(ScrapedData.agg({"jobs_lvl_1000":["mean"]}))
print(ScrapedData.agg({"jobs_lvl_1000":["median"]}))

job_data_alt=ScrapedData.filter(regex='(^j)|a')
print(job_data_alt)

print(job_data_alt.query("jobs_lvl_1000>135000"))

job_data_alt2 = ScrapedData.filter(regex='(^j)|a|month').query("jobs_lvl_1000>135000")
print(job_data_alt2)

print(ScrapedData.filter(regex="l$|o").query("snp500_mean_lvl>3000"))

print(ScrapedData.filter(regex="l$|o").query("snp500_mean_lvl>3000").agg({"jobs_lvl_1000":["mean","median"]}))