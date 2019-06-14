
Steps:

(1) scrap7.py  ---> 
"makes search on daijob and saves all jobs URLs and other informations as arrays of strings in json file"  generates  "jobs_it.json"

(2) read_scraped_data_write_to_csv.py --> 
reads info from json file "jobs_it.json" and put it in neat way in csv file "it_jobs.csv"

(3) scrap_job_single_page_v2__row_by_row_refined.py -->
gets url and job date for each job row in "it_jobs.csv" and opens its url and scrapes all data then writes it down to the final csv file "it_jobs_full_rbr_at_06.13.19.csv"
