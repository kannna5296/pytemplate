import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://typhoon.yahoo.co.jp/weather/jp/earthquake/list/?sort=1&key=1&b=54201"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

rows = soup.select("tr")[1:]  # ヘッダーを除く
data = []
for r in rows:
    cols = r.find_all("td")
    if len(cols) >= 4:
        data.append({
            "time": cols[0].text.strip(),
            "region": cols[1].text.strip(),
            "magnitude": cols[2].text.strip(),
            "max_intensity": cols[3].text.strip()
        })
df = pd.DataFrame(data)
print(df.head())
