from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")


wait = WebDriverWait(driver, 20)
top_10_list = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, '//h2[@id="top-10-web-application-security-risks"]/following::ul[1]/li/a')
))

data = []
for link in top_10_list:
    name = link.text.strip()
    url = link.get_attribute("href")
    if name and url:
        data.append({"name": name, "url": url})
        print(f"{name}: {url}")

with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["name", "url"])
    writer.writeheader()
    writer.writerows(data)

driver.quit()
