from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from multiprocessing import cpu_count

from colors import bcolors as bc
import threading
from time import perf_counter
import time

start_scrapping = perf_counter()
home_url = "https://www.immoweb.be/en"
# Query_list
query_list = ["Flandre orientale", "Flandre occidentale", "Hainaut", "Bruxelles", "Namur", "Anvers", "Brabant wallon", "Brabant flamand", "Liège", "Luxembourg"]
# Empty list to be populated with results
list_links = list()

def print_to_textfile( _input_list: list[str], _output_file_path: str):
    # Save the result list in a text file
    filename = _output_file_path
    with open(filename, 'w') as output_file:
        for el in _input_list:
            output_file.write(f"{el}\n")
    print(f"Output text file written")

def try_cookie( _driver: webdriver.Chrome):
    # Click the cookie on opening page
    try:
        cookie_button = _driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]')
        cookie_button.click()
    except:
        pass

def fill_home_input_form(_driver: webdriver.Chrome, _input: str, _delay = 5):
    # fill the form on opening page, with the request ( name of the province )
    search_field = _driver.find_element(By.CLASS_NAME, 'multiselect__input')
    search_field.send_keys(_input)
    search_field.send_keys(Keys.RETURN)
    time.sleep(_delay)
    submit_button = _driver.find_element(By.ID, 'searchBoxSubmitButton')
    submit_button.send_keys(Keys.RETURN)
    time.sleep(_delay)

def get_lists(_driver: webdriver.Chrome, list_links: list[str]) -> str:
    # Gets the list of all the links on a result page, and append the result in the result list.
    # Returns the link for the next page if it exists.
    # Skip to the next link if 'href' not found for particular ad.
    links = WebDriverWait(_driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card__title-link')))
    for link in links:
        try:
            list_links.append(link.get_attribute("href"))
        except:
            print("Unable to get attribute \"href\", {link}: ref skipped")
            pass
    print(len(list_links))

    try:
        next_button =  WebDriverWait(_driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'pagination__link--next'))
        )
        next_page_url = next_button.get_attribute("href")
        
    except:
        next_page_url=''

    return next_page_url

def gather_results(_query: str,_max_page_counter: int, _final_list_links: list[str]):
    # Gather results fromm all request in the final result file
    for links in main(_query, _max_page_counter):
            _final_list_links.append(links)

def main(_query: str, _max_page_counter: int) -> list[str]: 
    # 
    options = webdriver.ChromeOptions()                                     # Instanciate options for Chrome Driver
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Removing USB connection error which seems to be a bug in webdriver 
    # options.add_experimental_option('extensionLoadTimeout', 60000)        # Timeout of 60 sec
    options.add_argument('--incognito')
    # options.add_argument('--headless')#not working
    driver = webdriver.Chrome(options=options)                              # Instanciate Driver with options
    driver.set_page_load_timeout(30)                                        # set a max time for the page to load


    query_list_links = list()   # Create list of links results for that particular query
    driver.get(home_url)        # Start driver with Home url
    driver.implicitly_wait(1)   # Wait for the cookie to load
    try_cookie(driver)          # Try to click the cookie
    driver.implicitly_wait(1)   # Wait for the page to load

    logfile = f"./logs/Log_file_{_query}.txt"       # Create a log file name for each thread
    with open(logfile, 'w') as input_file:          # Open log file

        start_time = perf_counter()
        input_file.write(f"Query new houses : {_query},\n{time.asctime(time.localtime())}\n")       #  Write the _query value and start date in log file
        fill_home_input_form(driver, _query, 2)                                                     # Fill the home page with query, and open result page
        next_page_url = get_lists(driver, query_list_links)                                         # Query the first page of results and returns the adress of the next page.
        # Loop trough all the next pages until no next page or counter value is reached.
        count = 1
        condition = True
        while condition:
            if next_page_url != '' and count < _max_page_counter + 1:
                driver.get(next_page_url)
                input_file.write(f"Page counter = {count}, next link : {next_page_url},\n")
                print(f"Page counter = {count}, next link : {next_page_url}")
                next_link = get_lists(driver, query_list_links)
                next_page_url = next_link
                count += 1
            # exits if max counter is reached or no more results
            else:
                condition = False
                finish_time = perf_counter()
                input_file.write(f"{len(query_list_links)} links collected,\n{time.asctime(time.localtime())},\nJob done in {round((finish_time - start_time),2)} seconds!\n")
                input_file.write(f"Last 10 links collected:\n")
                for el in query_list_links[-10:]:
                    input_file.write(f"{el}\n")
                print("Job done!")
                driver.close()
    return query_list_links


def task(_query: str, _max_number_of_page: int):
    #gather_results wrapped in a task
    print(threading.current_thread().getName(), 'Starting')
    smphr.acquire()
    gather_results(_query, _max_number_of_page, list_links)
    time.sleep(2)
    print(threading.current_thread().getName(), 'Exiting')
    smphr.release()

def start_threads():
    threads = [threading.Thread(name=f'worker/Scrap {_query}', target=task, args=(_query, max_number_of_page)) for _query in query_list]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


# Threading setup
threads = list()
cpu_count = cpu_count()
maxthreads = cpu_count
max_number_of_page = 1
smphr = threading.Semaphore(value = maxthreads)

# Launch Scrap threading job
start_threads()

# Print the length of the result list and stats
end_scrapping = perf_counter()
print(f"Total time : {round((end_scrapping - start_scrapping), 2)} seconds, or {round((round((end_scrapping - start_scrapping), 2)/60), 2)} minutes,")
print(f"{bc.FAIL}{len(list_links)}{bc.ENDC} {bc.UNDERLINE}links collected{bc.ENDC}👌, {bc.WARNING}{round((end_scrapping - start_scrapping)/len(list_links), 2)} sec per link,{bc.ENDC}" )
print_to_textfile(list_links,'./list_of_results.txt')
