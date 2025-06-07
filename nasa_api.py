import requests
import webbrowser
import os

api_key = "M73dO4B5zrmj9QeLBfUxgkOFysf4dqcKa8MAAsmI"
url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
response = requests.get(url)
data = response.json()
print("API Response:", data)
date = data.get("date", "No date available.")
title = data.get("title", "No title available.")
explanation = data.get("explanation", "No explanation available.")
image_url = data.get("url", "")

html_content = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>NASA APOD - {title}</title>
  </head>
  <body>
    <div class="container">
      <h1>{title}</h1>
      <p><strong>Date:</strong> {date}</p>
      <img src="{image_url}" alt="NASA APOD Image" style="max-width: 100%; height: auto;" />
      <p style="margin-top: 20px">{explanation}</p>
    </div>
  </body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

webbrowser.open(f"file://{os.path.abspath('index.html')}")