from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:/Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)
url = "https://techwithtim.net"
driver.get(url)
print(driver.title)
search = driver.find_element_by_name('s')
search.clear()
search.send_keys("python", Keys.RETURN)
# print(driver.page_source)
try:
    main = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    pages = main.find_elements_by_class_name('page-numbers')
    pg = []
    for page in pages:
        pg.append(page.get_attribute('text'))
    last_page = int(pg[-2]) #grab the last page number and convert to int
    with open('f:/scraping.tsv', 'w') as f:
        f.write("Date\tTitle\tURL\tSummary\n")
    j = 1  #create a while loop to go thru all the pages with a searching result regarding python
    while j < last_page:
        main = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "main"))
        ) # this main may be redundant, not sure
        articles = main.find_elements_by_tag_name("article")
        for article in articles:
            with open('f:/scraping.tsv', 'a') as F:
                date = article.find_element_by_class_name('entry-date')
                header = article.find_element_by_css_selector('a')
                title = header.get_attribute('text')
                web = header.get_attribute('href')
                summary = article.find_element_by_class_name('entry-summary')
                print(date.text)
                print(title)
                print(web)
                print(summary.text)
                print('****************************************')
                F.write(f"{date.text}\t{title}\t{web}\t{summary.text}\n")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "next"))
                )
        element.click()
        j += 1
#     driver.back()
#     link = driver.find_element_by_link_text("Python Programming")
#     link.click()
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     element.click()
except:
    print('Error')
#How do I deal with the random ads page when I scraped the web page by page


