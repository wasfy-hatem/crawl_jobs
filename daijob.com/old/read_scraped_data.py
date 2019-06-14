
import jsonpickle
#import json
import simplejson as json

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys




def get_lists_of_attraction(value):#value is dummy here
   
   # value is dummy here
   value = "IT Jobs"
   # read
   with open("jobs_it.json", "r") as in_f:
       ###cate_lists_dict = jsonpickle.decode(json.load(in_f))
       x_list = jsonpickle.decode(json.load(in_f))

   #--------------------------------------------------------------
   '''
   "I feel history and culture", "Learn at the museum", "Relax in the hot spring", "Cobalt blue sea", "A distinctive park Superb view", "Scenic spots", "Outdoor sports", "Experience menu",  #activity "Shopping"
   '''
   ###values    =   ["history and culture", "museum", "hot spring", "sea", "park", "view", "sport", "activity", "shopping"]
   ###keys      =   ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

   ###attraction_dict = dict(zip(keys, values))

   #############page_num = "1"
   #--------------------------------------------------------------
   
   # receiving attraction
   #value = "history and culture" # = values[0] # = attraction_dict["keys[0]"]  # = attraction_dict["1"]

   # getting attraction lists
   print("Getting Lists of Jobs: ", value)
   ###x_list = cate_lists_dict[value]
   job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list = zip(*x_list)
   print("job_title_list size is: ", len(job_title_list))
   ###for place_name_t in place_name_t_list:
      ###print("---------------------------------------------")
      ###print(place_name_t)
      ###print("---------------------------------------------") 
   return job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list



#--------- Main program ----------------------------------------

arr = sys.argv # arr is program_name, value, .......the needed params....

#--------------------------------------------------------------

'''
"I feel history and culture", "Learn at the museum", "Relax in the hot spring", "Cobalt blue sea", "A distinctive park Superb view", "Scenic spots", "Outdoor sports", "Experience menu",  #activity "Shopping"
'''
###values    =   ["history and culture", "museum", "hot spring", "sea", "park", "view", "sport", "activity", "shopping"]
###keys      =   ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

###attraction_dict = dict(zip(keys, values))

#############page_num = "1"
#--------------------------------------------------------------

#value = "history and culture" # = values[0] # = attraction_dict["keys[0]"]  # = attraction_dict["1"] # = arr[1]

value = arr[1] # getting value from outside

job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list = get_lists_of_attraction(value)

for job_title in job_title_list:
      print("---------------------------------------------")
      print(job_title)
      print("---------------------------------------------")

