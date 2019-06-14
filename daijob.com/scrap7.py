import jsonpickle
#import json
import simplejson as json

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.chrome import service



def get_pages_count(cate_num):
   #claculate pages count function
   attraction   = "job_types[]=" + str(cate_num) + "&jt[]=" + str(cate_num) #IT unix --> project manager cate_num = 301
   #attraction   = "job_types[]=301&jt[]=301" #IT unix --> project manager
   base_url     = "https://www.daijob.com/en/jobs/search_result?"
   base_url_com = "https://www.daijob.com"
   page_num     = "&page=1" #predefined as first page here as we need to get number of pages only
   sort_by      = "&sort_order=3" #by updated date
   site_url     = base_url + attraction + sort_by + str(page_num)
    
   #for testing, comment it when live ### hatm Wasfy
   
   #IT (PC, Web, Unix)   IT (Mainframe)   IT (Hardware/Network)   IT (Embedded Software, Control Systems)   IT (Other)
   site_url     = "https://www.daijob.com/en/jobs/search_result?account_types[]=1&job_types[]=300&job_types[]=301&job_types[]=302&job_types[]=303&job_types[]=304&job_types[]=305&job_types[]=306&job_types[]=307&job_types[]=400&job_types[]=401&job_types[]=402&job_types[]=403&job_types[]=404&job_types[]=405&job_types[]=500&job_types[]=501&job_types[]=502&job_types[]=503&job_types[]=504&job_types[]=505&job_types[]=506&job_types[]=507&job_types[]=4000&job_types[]=4001&job_types[]=4002&job_types[]=4003&job_types[]=600&job_types[]=601&job_types[]=603&job_types[]=604&job_types[]=605&job_types[]=612&job_types[]=606&job_types[]=607&job_types[]=608&job_types[]=609&job_types[]=611&job_types[]=610&jt[]=400&jt[]=500&jt[]=4000&jt[]=600&job_search_form_hidden=1&sort_order=3" + str(page_num)


   ########################################

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

   ###############################################


   #####read = urlopen(site_url).read()
   read = driver.page_source
   #print (" Title Of the Site Is : " + title)

   #read = urlopen(site_url).read()
   #print (" Title Of the Site Is : " + title)
   soup = BeautifulSoup(read,"html.parser",from_encoding="UTF-8")

   #soup = BeautifulSoup(read, 'html.parser')
   ####print (soup.title.get_text()) ## Example For Title
   # <p class="count">12</p>
   mydivs_class_is_count       =  soup.find_all("div", class_="search_sort clearfix mb30")
   p_tags                      =  mydivs_class_is_count[0].find_all("p")
   
   #print("p_tags is: ", p_tags)
   span_tags                   =  p_tags[0].find_all("span")
   
   results_count               =  span_tags[0].text  #each page takes 15 result as fixed system


   print("Results count is: ", results_count)

   #number of pages = (results_count/15)

   #devide by 15 and check if there is reminder then pages_number = results_count//15 +1, if not then results_count//15 

   if int(results_count) % 15 == 0: #means no reminder
      pages_count = int(results_count)//15
   else: #means any reminder
      pages_count = (int(results_count)//15) + 1

   print("Pages number is:", pages_count)
   return pages_count, results_count



#page_num = 1
#while page_num <= pages_count:
#   print("Page number: ", page_num)
#   page_num +=1





def get_scrape_url(page_num, cate_num):

   #print (url)
   #return
   #attraction   = "job_types[]=301&jt[]=301" #IT unix --> project manager
   attraction   = "job_types[]=" + str(cate_num) + "&jt[]=" + str(cate_num) #IT unix --> project manager cate_num = 301
   base_url     = "https://www.daijob.com/en/jobs/search_result?"
   base_url_com = "https://www.daijob.com"
   page_number  = "&page=" + str(page_num)
   sort_by      = "&sort_order=3" #by updated date
   account_type = "&account_types[]=1" #means we  need only direct employer company not 3rd party rec company
   site_url     = base_url + attraction + sort_by + account_type + str(page_number)
    
   #for testing, comment it when live ### hatm Wasfy

   #IT (PC, Web, Unix)   IT (Mainframe)   IT (Hardware/Network)   IT (Embedded Software, Control Systems)   IT (Other)
   ########################################
   site_url     = "https://www.daijob.com/en/jobs/search_result?account_types[]=1&job_types[]=300&job_types[]=301&job_types[]=302&job_types[]=303&job_types[]=304&job_types[]=305&job_types[]=306&job_types[]=307&job_types[]=400&job_types[]=401&job_types[]=402&job_types[]=403&job_types[]=404&job_types[]=405&job_types[]=500&job_types[]=501&job_types[]=502&job_types[]=503&job_types[]=504&job_types[]=505&job_types[]=506&job_types[]=507&job_types[]=4000&job_types[]=4001&job_types[]=4002&job_types[]=4003&job_types[]=600&job_types[]=601&job_types[]=603&job_types[]=604&job_types[]=605&job_types[]=612&job_types[]=606&job_types[]=607&job_types[]=608&job_types[]=609&job_types[]=611&job_types[]=610&jt[]=400&jt[]=500&jt[]=4000&jt[]=600&job_search_form_hidden=1&sort_order=3" + str(page_number)


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

   ###############################################


   #####read = urlopen(site_url).read()
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

   mydivs0 = soup.find_all("div", class_="jobs_box_header_title mb16")
   for div in mydivs0:
       ###print (div)
       #print(div.text)
       #print(div.contents)

       #main_image = div.find('div', attrs={'class': 'main_image'})
       main_image = div

       ##-->print(main_image.get_text())
       a_tags = main_image.find_all("a")

       #for tag in a_tags:
       #print(tag)
       #img_tags  = a_tags[0].find_all("img")
       job_company = a_tags[0].text#get('href')
       #for img_tag in img_tags:
       # print(img_taga)
       #printing alternate text
       print("---------------------------------------------------------------------")

       job_company_list.append(job_company) #
       print("job company: ", job_company)
       print("---------------------------------------------------------------------")



   # for col_1 div, that has image url and name
   mydivs = soup.find_all("div", class_="jobs_box_logo_wrap")
   for div in mydivs: 
       ###print (div)
       #print(div.text)
       #print(div.contents)
    
       #main_image = div.find('div', attrs={'class': 'main_image'})
       main_image = div

       ##-->print(main_image.get_text())
       a_tags = main_image.find_all("a")
    
       #for tag in a_tags:
       #print(tag)
       #img_tags  = a_tags[0].find_all("img")
       place_image_detail_url = a_tags[0].get('href')
       #for img_tag in img_tags:
       # print(img_taga)
       #printing alternate text
       print("---------------------------------------------------------------------")
       #place_name = img_tags[0]['alt']
       #place_name_list.append(place_name)
       #print("image alt (place_name): ", place_name)
       #printing image source
       #place_image_url = base_url + img_tags[0]['src']

       job_url = base_url_com + place_image_detail_url #acting as job adv url

       job_url_list.append(job_url) #acting as job adv url full one
       print("job url: ", job_url)
       print("---------------------------------------------------------------------")


       img_tags                  = main_image.find_all("img")
       job_company               = img_tags[0].get('alt')
       job_company_logo          = img_tags[0].get('src')

       job_company_list.append(job_company)
       job_company_logo_list.append(job_company_logo)

      
   # for col_2 div, that has place describtion, place url and name
   #mydivs2 = soup.find_all("div", class_="jobs_table02 table01")
   mydivs2 = soup.find_all("div", class_="jobs_box_content")

   #jobs_box_content
   print("+++++++++++++++++++")
   #print(soup)
   for div in mydivs2:
       #print (div)
       ##print(div.text)
       #print(div.contents)

       #main_image = div.find('div', attrs={'class': 'title'})
       ##-->print(main_image.get_text())
       p_tags             = div.find_all("p", class_="ta_right fc_gray02")
       #print(a_tags)
       span_tags          = p_tags[0].find_all("span")
       job_date           = span_tags[0].text   



       print("+---------------------------------------------------------------------+")
       ###job_title = p_tags[0].text 
       ###job_title_list.append(job_title)
       #print("job title: ", job_title)

       ####### ---> get updated date  job_date
       #span_tags                   =  p_tags[1].find_all("span")

       #job_date                    =  span_tags[0].text  # job date

   
       #place_url = base_url + a_tags[0]['href']
       #place_url_list.append(place_url)
       print("job date: ", job_date)
       #print("+---------------------------------------------------------------------+")
       
       #p_tags = div.find_all("p")

       #place_short_desc = p_tags[0].text #short

       #div.find_all("p", class_=("jobs_table02 table01")
       job_date_list.append(job_date)

       #place_long_desc  = p_tags[1].text #long
       #place_long_desc_list.append(place_long_desc)

       #print("short description: ", place_short_desc)
       #print("long description: ", place_long_desc)
       #print("++++++++++++++++++++++++++++++++++++++++++++")
       print("+---------------------------------------------------------------------+")

   mydivs3 = soup.find_all("div", class_="jobs_box_header_position mb16")

   #jobs_box_content
   print("+++++++++++++++++++")
   #print(soup)
   for div in mydivs3:
       #print (div)
       ##print(div.text)
       #print(div.contents)

       #main_image = div.find('div', attrs={'class': 'title'})
       ##-->print(main_image.get_text())
       a_tags             = div.find_all("a")
       #print(a_tags)
       #span_tags          = p_tags[0].find_all("span")
       job_title           = a_tags[0].text.rsplit(' ', 1)[0] 
       job_title_list.append(job_title)



       print("+---------------------------------------------------------------------+")
       ###job_title = p_tags[0].text 
       ###job_title_list.append(job_title)
       print("job title: ", job_title)

       ####### ---> get updated date  job_date
       #span_tags                   =  p_tags[1].find_all("span")

       #job_date                    =  span_tags[0].text  # job date


       #place_url = base_url + a_tags[0]['href']
       #place_url_list.append(place_url)
       #print("job date: ", job_date)



   return  job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list

   #place_name_t_list, place_image_url_list, place_url_list, place_short_desc_list, place_long_desc_list



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


#-----------------------------------------------------------
# Main code

'''
"I feel history and culture", "Learn at the museum", "Relax in the hot spring", "Cobalt blue sea", "A distinctive park Superb view", "Scenic spots", "Outdoor sports", "Experience menu",  #activity "Shopping"
'''
#values    =   ["history and culture", "museum", "hot spring", "sea", "park", "view", "sport", "activity", "shopping"]
#keys      =   ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


'''
values     =   ["Fresh seafood and tavern", "Excellent Yakiniku  Yakitori", "Champon  Ramen", "Sweets & Cafe", "Western food", "Island lunch", "Bar snack"]
keys       =   ["16", "17", "18", "19", "20", "21", "22"]
attraction_dict = dict(zip(keys, values))

#############page_num = "1"
cate_num = "1"

#db_list = []
cate_lists_dict = {}
for cate_num, value in sorted(attraction_dict.items()):
   
   print("%%%%%%% Working on Cate: ", value)
   print("%%%%%%% Working on Cate: ", cate_num)
   #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   # get_pages_count(cate_num)
   # get_scrape_url(page_num, cate_num)
   pages_count, results_count  = get_pages_count(cate_num)
   #---------------------------------#

   place_name_t_list, place_image_url_list, place_url_list, place_short_desc_list, place_long_desc_list = get_scrape_cate(pages_count, cate_num)
   
   #zipofalllists1=zip(a,b,c,d,e)
   x_list = zip(place_name_t_list, place_image_url_list, place_url_list, place_short_desc_list, place_long_desc_list)
   cate_lists_dict[value] = x_list

   #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   print("*^^^^^^^^^^^length of place_name_t_list is: ", str(len(place_name_t_list)))

   for i in place_name_t_list:

      print("*************************************")
      print("place name is:  --> ", i)
      print("*************************************")


# write
with open("goto_food_db.json", "w") as out_f:
    #json.dump(list(zipofalllists), out_f)
     json.dump(jsonpickle.encode(cate_lists_dict), out_f)
'''

# read
##with open("out.json", "r") as in_f:
    ##alllists = json.load(in_f)

#for i, j, k, l, m, n, o, p, q in alllists:
    ##d[i] = [j, k]
    #print("i: ", i)
    ##print("j: ", j)
    ##print("k: ", c)





#get_scrape_url(page_num, cate_num)

#working June 2019
###get_scrape_url(3, 301)
#get_pages_count(301) #IT unix --> project manager cate_num = 301




cate_num = "301" #dummy will not be used in case of forcing full url from outside
# get_pages_count(cate_num)
# get_scrape_url(page_num, cate_num)
pages_count, results_count  = get_pages_count(cate_num)
#---------------------------------#

job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list = get_scrape_cate(pages_count, cate_num)

   
#zipofalllists1=zip(a,b,c,d,e)
x_list = zip(job_url_list, job_date_list, job_title_list, job_company_list, job_company_logo_list)
###cate_lists_dict[value] = x_list

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print("*^^^^^^^^^^^length of job_title_list is: ", str(len(job_title_list)))

for i in job_title_list:
   print("*************************************")
   print("Job title is:  --> ", i)
   print("*************************************")


# write
with open("jobs_it.json", "w") as out_f:
    #json.dump(list(zipofalllists), out_f)
    ###json.dump(jsonpickle.encode(cate_lists_dict), out_f)
    json.dump(jsonpickle.encode(x_list), out_f)

