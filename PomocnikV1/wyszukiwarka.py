from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome"
chromedriver = r"C:\Users\Szymek\Downloads\chromedriver"
USERNAME = "us3r123"
PASSWORD = "qqwweerr"

#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path=chromedriver)
doWyszukania = "airpods"
driver.get("https://www.pepper.pl/search?q=" + doWyszukania)
j = 0;
for i in range(1, 20):
    if j <= 5:
        try:
            nazwa = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/section/div[1]/article[" + str(i) + "]/div/div[3]/strong/a")
            cena = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/section/div[1]/article[" + str(i) + "]/div/div[3]/span/span[1]/span")
            print("Nazwa produktu: " + nazwa.get_attribute('title'))
            print("Cena: " + cena.text)

            j = j + 1;
        except:
            continue

print(driver.current_url)
#driver.quit()