import time

import requests
from bs4 import BeautifulSoup

import pandas as pd


def scrape_earthquake_data():
    """複数のURLから地震データを取得し、結合したDataFrameを返す"""
    URL_BASE = "https://typhoon.yahoo.co.jp/weather/jp/earthquake/list/?sort=1&key=1&b="

    all_data = []

    # b=1からb=54201まで、100刻みでURLを生成
    for b_value in range(1, 54202, 100):
        url = URL_BASE + str(b_value)
        print(f"取得中: {url}")

        try:
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")

            rows = soup.select("tr")[1:]  # ヘッダーを除く

            for r in rows:
                cols = r.find_all("td")
                if len(cols) >= 4:
                    all_data.append(
                        {
                            "time": cols[0].text.strip(),
                            "region": cols[1].text.strip(),
                            "magnitude": cols[2].text.strip(),
                            "max_intensity": cols[3].text.strip(),
                        }
                    )

            # リクエスト間隔を空ける
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"エラー: {url} - {e}")
            continue
        except Exception as e:
            print(f"予期しないエラー: {url} - {e}")
            continue

    # 全データを結合したDataFrameを作成
    df = pd.DataFrame(all_data)
    return df


if __name__ == "__main__":
    df = scrape_earthquake_data()
    print(f"取得したデータ数: {len(df)}")
    print("\n最初の5行:")
    print(df.head())
    print("\n最後の5行:")
    print(df.tail())

    df.to_csv("earthquake_data.csv", index=False)
