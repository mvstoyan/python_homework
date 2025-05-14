from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import pandas as pd
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")  

body = driver.find_element(By.CSS_SELECTOR, 'body')

# Найдём все результаты в li с нужным классом
li_search = body.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
print(f"Found {len(li_search)} elements:")

results = []

for i, item in enumerate(li_search, 1):
    try:
        # Title
        title_element = item.find_element(By.CLASS_NAME, "cp-title")
        title = title_element.text.strip()

        # Authors
        authors_elements = item.find_elements(By.CLASS_NAME, "cp-author-link")
        authors = "; ".join([a.text.strip() for a in authors_elements])

        # Format-Year (используем display-info-primary)
        format_year = ""
        try:
            format_info = item.find_element(By.CLASS_NAME, "cp-format-info")
            format_year_span = format_info.find_element(By.CLASS_NAME, "display-info-primary")
            format_year = format_year_span.text.strip()
        except:
            format_year = "Not available"

        # Сохраняем результат
        book_info = {
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        }
        results.append(book_info)

        print(f"\nResult {i}:")
        print(json.dumps(book_info, indent=2))

    except Exception as e:
        print(f"Error processing result {i}: {e}")

df= pd.DataFrame(results)
print(df)

df.to_csv('get_books.csv', index=False)
df.to_json('get_books.json', orient='records', lines=True)
    
driver.quit()