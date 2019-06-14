import jsonpickle
#import json
import simplejson as json

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.chrome import service

import wget
##############################
import csv
from datetime import date
import time


#site_url is:  https://www.daijob.com/en/jobs/detail/683754
#Page Title is : www.daijob.com

#page 130
#https://www.daijob.com/en/jobs/detail/771947


def scrap_job_ok_and_expired(job_url):
   site_url = job_url
   print("site_url is: ", site_url)
   driver = webdriver.Opera(executable_path='/home/wasfy/python_progs/crawl_jobs/operadriver_linux64/operadriver')
   driver.get(site_url)
   print("Page Title is : %s" %driver.title)
   if "Daijob.com :: 'Jobs for international business professionals."  in driver.title: #---> job expired
      print("\n**** job is expired ***\n")
      job_company_name = job_type = job_industry = job_location = job_description = job_company_info = job_working_hours = job_requirnments = job_japanese_level = job_salary = job_other_salary_description = job_holidays = job_contract = job_nearest_station = "expired"
      driver.close() #->closing
      driver.quit()

      return job_company_name, job_type, job_industry, job_location, job_description, job_company_info, job_working_hours, job_requirnments, job_japanese_level, job_salary, job_other_salary_description, job_holidays, job_contract, job_nearest_station 
   
   else:  #job is not expired
      print("\n**** job is not expired ---> we call our parser ***\n")
      job_company_name, job_type, job_industry, job_location, job_description, job_company_info, job_working_hours, job_requirnments, job_japanese_level, job_salary, job_other_salary_description, job_holidays, job_contract, job_nearest_station = get_scrape_job_full_details_from_url(job_url)
      return job_company_name, job_type, job_industry, job_location, job_description, job_company_info, job_working_hours, job_requirnments, job_japanese_level, job_salary, job_other_salary_description, job_holidays, job_contract, job_nearest_station

### --> not good

   



def get_scrape_job_full_details_from_url(job_url):

   #print (url)
   #return
   #attraction   = "job_types[]=301&jt[]=301" #IT unix --> project manager
   #initialization
   job_company_name = job_type = job_industry = job_location = job_description = job_company_info = job_working_hours = job_requirnments = job_japanese_level = job_salary = job_other_salary_description = job_holidays = job_contract = job_nearest_station = ""

   '''
   attraction   = "job_types[]=" + str(cate_num) + "&jt[]=" + str(cate_num) #IT unix --> project manager cate_num = 301
   base_url     = "https://www.daijob.com/en/jobs/search_result?"
   base_url_com = "https://www.daijob.com"
   page_number  = "&page=" + str(page_num)
   sort_by      = "&sort_order=3" #by updated date
   account_type = "&account_types[]=1" #means we  need only direct employer company not 3rd party rec company
   site_url     = base_url + attraction + sort_by + account_type + str(page_number)a
   '''

    
   #for testing, comment it when live ### hatm Wasfy

   #IT (PC, Web, Unix)   IT (Mainframe)   IT (Hardware/Network)   IT (Embedded Software, Control Systems)   IT (Other)
   ########################################
   ###site_url     = "https://www.daijob.com/en/jobs/search_result?account_types[]=1&job_types[]=300&job_types[]=301&job_types[]=302&job_types[]=303&job_types[]=304&job_types[]=305&job_types[]=306&job_types[]=307&job_types[]=400&job_types[]=401&job_types[]=402&job_types[]=403&job_types[]=404&job_types[]=405&job_types[]=500&job_types[]=501&job_types[]=502&job_types[]=503&job_types[]=504&job_types[]=505&job_types[]=506&job_types[]=507&job_types[]=4000&job_types[]=4001&job_types[]=4002&job_types[]=4003&job_types[]=600&job_types[]=601&job_types[]=603&job_types[]=604&job_types[]=605&job_types[]=612&job_types[]=606&job_types[]=607&job_types[]=608&job_types[]=609&job_types[]=611&job_types[]=610&jt[]=400&jt[]=500&jt[]=4000&jt[]=600&job_search_form_hidden=1&sort_order=3" + str(page_number)

   site_url = job_url #"https://www.daijob.com/en/jobs/detail/797796" #forced for single job page


   #with page number: https://www.daijob.com/en/jobs/search_result?page=2&job_types[]=301&jt[]=301
   #site_url = "http://goto.nagasaki-tabinet.com/spot/?page=1&list_type=row&sort_type=access&cate_m=2"
   #         = "https://www.daijob.com/en/jobs/search_result?job_types[]=301&jt[]=301&page=2"
   print("site_url is: ", site_url)
   #site_url = "http://goto.nagasaki-tabinet.com/spot/?page=1&?latitude=&longitude=&list_type=row&sort_type=access&keyword=&cate_m=1"
   #########
   # selenium
   ###############################################
   driver = webdriver.Opera(executable_path='/home/wasfy/python_progs/crawl_jobs/operadriver_linux64/operadriver')
   driver.get(site_url)
   print("Page Title is : %s" %driver.title)
   #if driver.title = "Daijob.com :: 'Jobs for international business professionals."  #---> job expired
   ###############################################
   #if "Daijob.com :: 'Jobs for international business professionals."  in driver.title: #---> job expired
      #print("\n**** job is expired ***\n")
      #job_company_name = job_type = job_industry = job_location = job_description = job_company_info = job_working_hours = job_requirnments = job_japanese_level = job_salary = job_other_salary_description = job_holidays = job_contract = job_nearest_station = "expired"
      #driver.close()
      #driver.quit()

   #return job_company_name, job_type, job_industry, job_location, job_description, job_company_info, job_working_hours, job_requirnments, job_japanese_level, job_salary, job_other_salary_description, job_holidays, job_contract, job_nearest_station


   #--------------------------->
   #else: # it is not expired
   #####read = urlopen(site_url).read()
   #else:  #job is not expired
      #print("\n**** job is not expired ---> we call our parser ***\n")
   ##--> 3 steps
   read = driver.page_source
   #print (" Title Of the Site Is : " + title)

   #soup = BeautifulSoup(open(html_path, 'r'),"html.parser",from_encoding="iso-8859-1")
   #soup = BeautifulSoup(read, 'html.parser')
   soup = BeautifulSoup(read,"html.parser",from_encoding="UTF-8")
   #print (soup.title.get_text()) ## Example For Title
   ###->### print("all is: \n", soup)

   #scrape_url("hello")
   
   '''
   place_name_list           = []
   place_image_url_list      = []
   place_name_t_list         = []
   place_url_list            = []
   place_short_desc_list     = []
   place_long_desc_list      = []
   '''

   #for jobs
   job_url_list              = []
   job_date_list             = []
   job_title_list            = []
   job_company_list          = []
   job_company_logo_list     = []

   mydivs0 = soup.find_all("div", class_="jobs_box_content") #big parent
   for div in mydivs0:
       ###print (div)
       #print(div.text)
       #print(div.contents)

       #main_image = div.find('div', attrs={'class': 'main_image'})
       main_div = div
       
       # start sections here:
       # another cover for expired
       try:

         div_tags_jobs_table03_table01 = main_div.find_all("div", class_="jobs_table03 table01")
         tr_tags_jobs_table03_table01  = div_tags_jobs_table03_table01[0].find_all("tr") #results in 14 <tr> tag, tr_tags_jobs_table03_table01[0] to tr_tags_jobs_table03_table01[13]
       except:
         print("Expired job is detected by the second filter")
         print("\n**** job is expired ***\n")
         job_company_name = job_type = job_industry = job_location = job_description = job_company_info = job_working_hours = job_requirnments = job_japanese_level = job_salary = job_other_salary_description = job_holidays = job_contract = job_nearest_station = "expired"
         driver.close() #->closing
         driver.quit()
         
         return job_company_name, job_type, job_industry, job_location, job_description, job_company_info, job_working_hours, job_requirnments, job_japanese_level, job_salary, job_other_salary_description, job_holidays, job_contract, job_nearest_station


       #print("tr_tags_jobs_table03_table01[0]:  ", tr_tags_jobs_table03_table01[0])
       #print("tr_tags_jobs_table03_table01[13]:  ", tr_tags_jobs_table03_table01[13])


       #'''
       #'''

       #--> # tr_tags_jobs_table03_table01[0] job_company_name
       #-----------------------------------------------------------#
       try:

         h4_tags = tr_tags_jobs_table03_table01[0].find_all("h4")
         job_company_name = h4_tags[0].text
       except:
         job_company_name = "not shown"

       print("job_company_name: ", job_company_name)
       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[1] job_type
       #-----------------------------------------------------------#
       try:

         a_tags = tr_tags_jobs_table03_table01[1].find_all("a")
         job_type = ""
         for a in a_tags:
            job_type = job_type + "\n" + a.text
       except:
         job_type = "not shown"

       print("job_type: ", job_type)

         
       #-----------------------------------------------------------#


       #--> # tr_tags_jobs_table03_table01[2] job_industry
       #-----------------------------------------------------------#

       try:

         a_tags = tr_tags_jobs_table03_table01[2].find_all("a")
         job_industry = a_tags[0].text
       except:
         job_industry = "not shown"
       print("job_industry: ", job_industry)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[3] job_location
       #-----------------------------------------------------------#
       try:

         a_tags = tr_tags_jobs_table03_table01[3].find_all("a")
         job_location = ""
         for a in a_tags:
            job_location = job_location + "\n" + a.text
       except:
         job_location = "not shown"
       print("job_location: ", job_location)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[4] job_description
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[4].find_all("td")
         job_description = td_tags[0].text
       except:
         job_description = "not shown"
       print("job_description: ", job_description)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[5] job_company_info
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[5].find_all("td")
         job_company_info = td_tags[0].text
       except:
         job_company_info = "not shown"
       print("job_company_info: ", job_company_info)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[6] job_working_hours
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[6].find_all("td")
         job_working_hours = td_tags[0].text
       except:
         job_working_hours = "not shown"
       print("job_woking_hours: ", job_working_hours)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[7] job_requirnments
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[7].find_all("td")
         job_requirnments = td_tags[0].text
       except:
         job_requirnments = "not shown"
       print("job_requirnments: ", job_requirnments)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[8] job_japanese_level
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[8].find_all("td")
         job_japanese_level = td_tags[0].text
       except:
         job_japanese_level = "not shown"
       print("job_japanese_level: ", job_japanese_level)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[9] job_salary
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[9].find_all("td")
         job_salary = td_tags[0].text
       except:
         job_salary = "not shown"
       print("job_salary: ", job_salary)

       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[10] job_other_salary_description
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[10].find_all("td")
         job_other_salary_description = td_tags[0].text
       except:
         job_other_salary_description = "not shown"
       print("job_other_salary_description: ", job_other_salary_description)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[11] job_holidays
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[11].find_all("td")
         job_holidays = td_tags[0].text
       except:
         job_holidays = "not shown"
       print("job_holidays: ", job_holidays)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[12] job_contract
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[12].find_all("td")
         job_contract = td_tags[0].text
       except:
         job_contract = "not shown"
       print("job_contract: ", job_contract)


       #-----------------------------------------------------------#



       #--> # tr_tags_jobs_table03_table01[13] job_nearest_station
       #-----------------------------------------------------------#
       try:

         td_tags = tr_tags_jobs_table03_table01[13].find_all("td")
         job_nearest_station = td_tags[0].text
       except:
         job_nearest_station = "not shown"
       print("job_nearest_station: ", job_nearest_station)
       


       #-----------------------------------------------------------#
       driver.close() #closing
       driver.quit()






   return  job_company_name, job_type, job_industry, job_location, job_description, job_company_info, job_working_hours, job_requirnments, job_japanese_level, job_salary, job_other_salary_description, job_holidays, job_contract, job_nearest_station


def get_scrape_cate(pages_count, cate_num):
   #get_scrape_url(page_num, cate_num)
   '''
   place_name_t_list           = []
   place_image_url_list        = []
   place_url_list              = []
   place_short_desc_list       = []
   place_long_desc_list        = []
   '''

   job_url_list              = []
   job_date_list             = []
   job_title_list            = []
   job_company_list          = []
   job_company_logo_list     = []
   

   if pages_count > 1:
       page_num = 1
       while page_num <= pages_count:
        print("@@@@@@@@@@@@@@@@@@@@@@@@")
        print("@Dealing with Page #", str(page_num))
        print("@@@@@@@@@@@@@@@@@@@@@@@@")
        job_url_listi, job_date_listi, job_title_listi, job_company_listi, job_company_logo_listi = get_scrape_url(str(page_num), str(cate_num))

        job_url_list.extend(job_url_listi)
        job_date_list.extend(job_date_listi)
        job_title_list.extend(job_title_listi)
        job_company_list.extend(job_company_listi)
        job_company_logo_list.extend(job_company_logo_listi)

        '''
        place_name_t_list.extend(place_name_t_listi)
        place_image_url_list.extend(place_image_url_listi)
        place_url_list.extend(place_url_listi)
        place_short_desc_list.extend(place_short_desc_listi)
        place_long_desc_list.extend(place_long_desc_listi)
        '''

        page_num +=1

   elif pages_count == 1:
        job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list  = get_scrape_url("1", str(cate_num))

   return  job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list





def read_lists_from_csv_line(links_file):

   #links_file = "it_jobs.csv"
   #Job URL,Job Date,Job Title,Job Company,Job Compny Logo

   #import csv
   #in main
   '''
   links_file = "it_jobs.csv"
   job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list = read_lists_from_csv_line(links_file)
   print(job_url_list[2])

   '''

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
#-----------------------------------------------------------
# Main code

#------------------------>
'''   
links_file = "it_jobs.csv"
job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list = read_lists_from_csv_line(links_file)
#print(job_url_list[2])

'''

links_file = "it_jobs.csv"
job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list = read_lists_from_csv_line(links_file)


#get_scrape_url(page_num, cate_num)

#working June 2019

job_company_name_list                                = []
job_type_list                                        = []
job_industry_list                                    = []
job_location_list                                    = []
job_description_list                                 = []
job_company_info_list                                = []
job_working_hours_list                               = []
job_requirnments_list                                = []
job_japanese_level_list                              = []
job_salary_list                                      = []
job_other_salary_description_list                    = []
job_holidays_list                                    = []
job_contract_list                                    = []
job_nearest_station_list                             = []


#for job_url in job_url_list:
total_number_of_jobs = str(len(job_url_list))
current_job_number = 1


today = date.today()
today_date = today.strftime("%m.%d.%y")
today_date_header = "_at_" + today_date

file_name_base = "it_jobs_full_rbr"
#file_name_json = file_name_base + today_date_header + ".json"
file_name_csv_rbr  = file_name_base + today_date_header + ".csv"


RESULT =  ['job_date', 'job_company_name', 'job_type', 'job_industry', 'job_location', 'job_description', 'job_company_info', 'job_working_hours', 'job_requirnments', 'job_japanese_level', 'job_salary', 'job_other_salary_description', 'job_holidays', 'job_contract', 'job_nearest_station']

with open(file_name_csv_rbr,'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    #wr = csv.writer(sys.stderr, dialect='excel') #csv.writer(f)

    wr.writerow(RESULT)
#

RESULT = []




for job_url, job_date in zip(job_url_list, job_date_list):
  print("----------------------------------------")
  print("Total number of found jobs is : ", total_number_of_jobs)
  print("----------------------------------------")
  current_job_number_of_max = str(current_job_number) + "/" + str(total_number_of_jobs)
  print("Working now on job: ", current_job_number_of_max)
  print("----------------------------------------")
  print("|")
  print("|")
  current_job_number +=1
  time.sleep(1) #sleep 1 seconds
  print("----------------------------------------")
  print("|||--> Sleeping for 1 seconds ... -->|||")
  print("----------------------------------------")

  job_company_name, job_type, job_industry, job_location, job_description, job_company_info, job_working_hours, job_requirnments, job_japanese_level, job_salary, job_other_salary_description, job_holidays, job_contract, job_nearest_station = scrap_job_ok_and_expired(job_url) #get_scrape_job_full_details_from_url(job_url)
  #job_date


#get_pages_count(301) #IT unix --> project manager cate_num = 301
  print("\n--> job_date: ", job_date)
  print("\n---------------------------------------------------------\n")

  print("job_industry: ", job_industry)

  print("\n---------------------------------------------------------\n")

##############################################################
#for i in range(0,len(job_company_name_list)):
  # write row by row

  RESULT.append(job_date)
  #print("job_date", job_date)

  RESULT.append(job_company_name)
  #print("job_company_name_list[i]", job_company_name_list[i])
  RESULT.append(job_type)

  #print("job_industry_list[i]", job_industry_list[i])

  RESULT.append(job_industry)
  RESULT.append(job_location)
  RESULT.append(job_description)
  RESULT.append(job_company_info)
  RESULT.append(job_working_hours)
  RESULT.append(job_requirnments)
  RESULT.append(job_japanese_level)
  RESULT.append(job_salary)
  RESULT.append(job_other_salary_description)
  RESULT.append(job_holidays)
  RESULT.append(job_contract)
  RESULT.append(job_nearest_station)



  with open(file_name_csv_rbr,'a') as resultFile:
      wr = csv.writer(resultFile, dialect='excel')
      #wr = csv.writer(sys.stderr, dialect='excel') #csv.writer(f)

      wr.writerow(RESULT)

  RESULT = []



###############################################################
  #-----
  #list filling
  
  #-----
  '''
  job_company_name_list.append(job_company_name)
  job_type_list.append(job_type)
  job_industry_list.append(job_industry)
  job_location_list.append(job_location)
  job_description_list.append(job_description)
  job_company_info_list.append(job_company_info)
  job_working_hours_list.append(job_working_hours)
  job_requirnments_list.append(job_requirnments)
  job_japanese_level_list.append(job_japanese_level)
  job_salary_list.append(job_salary)
  job_other_salary_description_list.append(job_other_salary_description) 
  job_holidays_list.append(job_holidays)
  job_contract_list.append(job_contract)
  job_nearest_station_list.append(job_nearest_station)
  '''
# now we have full lists , so we write them to 2 ypes of files as a variety json & csv
'''
today = date.today()
today_date = today.strftime("%m.%d.%y")
today_date_header = "_at_" + today_date

file_name_base = "it_jobs_full"
file_name_json = file_name_base + today_date_header + ".json"
file_name_csv  = file_name_base + today_date_header + ".csv"


x_list = zip(job_date_list, job_company_name_list, job_type_list, job_industry_list, job_location_list, job_description_list, job_company_info_list, job_working_hours_list, job_requirnments_list, job_japanese_level_list, job_salary_list, job_other_salary_description_list, job_holidays_list, job_contract_list, job_nearest_station_list)

# write json
with open(file_name_json, "w") as out_f:
    #json.dump(list(zipofalllists), out_f)
    ###json.dump(jsonpickle.encode(cate_lists_dict), out_f)
    json.dump(jsonpickle.encode(x_list), out_f)



# ------>


#titles
RESULT =  ['job_date', 'job_company_name', 'job_type', 'job_industry', 'job_location', 'job_description', 'job_company_info', 'job_working_hours', 'job_requirnments', 'job_japanese_level', 'job_salary', 'job_other_salary_description', 'job_holidays', 'job_contract', 'job_nearest_station']

with open(file_name_csv,'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    #wr = csv.writer(sys.stderr, dialect='excel') #csv.writer(f)

    wr.writerow(RESULT)
#

RESULT = []

#import csv
#RESULT = ['apple','cherry','orange','pineapple','strawberry']
#RESULT = place_name_list, place_geo_loc_list, place_id_list, place_url_list, plat_plng_list, place_photo_url_list

#['job_company_name', 'job_type', 'job_industry', 'job_location', 'job_description', 'job_company_info', 'job_working_hours', 'job_requirnments', 'job_japanese_level', 'job_salary', 'job_other_salary_description', 'job_holidays', 'job_contract', 'job_nearest_station']

print("len(job_company_name_list) - 1 = ", len(job_company_name_list) - 1)
#for i in range(0,len(job_company_name_list) - 1):
for i in range(0,len(job_company_name_list)):
   

   RESULT.append(job_date_list[i])
   print("job_date_list[i]", job_date_list[i])

   RESULT.append(job_company_name_list[i])
   print("job_company_name_list[i]", job_company_name_list[i])
   RESULT.append(job_type_list[i])

   print("job_industry_list[i]", job_industry_list[i])

   RESULT.append(job_industry_list[i])
   RESULT.append(job_location_list[i])
   RESULT.append(job_description_list[i])
   RESULT.append(job_company_info_list[i])
   RESULT.append(job_working_hours_list[i])
   RESULT.append(job_requirnments_list[i])
   RESULT.append(job_japanese_level_list[i])
   RESULT.append(job_salary_list[i])
   RESULT.append(job_other_salary_description_list[i])
   RESULT.append(job_holidays_list[i])
   RESULT.append(job_contract_list[i])
   RESULT.append(job_nearest_station_list[i])



   with open(file_name_csv,'a') as resultFile:
       wr = csv.writer(resultFile, dialect='excel')
       #wr = csv.writer(sys.stderr, dialect='excel') #csv.writer(f)

       wr.writerow(RESULT)

   RESULT = []

'''


###### ----- > 
'''
'''
###### --------->
