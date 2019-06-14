
import csv
from datetime import date



def read_lists_from_csv_line(links_file):

   #links_file = "it_jobs.csv"
   #Job URL,Job Date,Job Title,Job Company,Job Compny Logo

   job_url_list                   = []
   job_date_list                  = []
   job_title_list                 = []
   job_company_list               = []
   job_company_logo_list          = []

   with open(links_file, newline='', encoding='utf-8') as f:
       reader = csv.reader(f)
       headers = next(reader) # to skip header line (first line)

       for row in reader:
           
           #print(row[0].strip())
           job_url                          = row[0].strip()
           job_date                         = row[1].strip()
           job_title                        = row[2].strip()
           job_company                      = row[3].strip()
           job_company_logo                 = row[4].strip()

           
           job_url_list.append(job_url)                   
           job_date_list.append(job_date)           
           job_title_list.append(job_title)         
           job_company_list.append(job_company)        
           job_company_logo_list.append(job_company_logo)   

   return job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list
   




#----------------------------

#------ main -------------------



links_file = "it_jobs.csv"

job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list = read_lists_from_csv_line(links_file)


print(job_url_list[2])



today = date.today()
today_date = today.strftime("%m.%d.%y")
today_date_header = "_at_" + today_date


print(today_date_header)

