import pandas as pd

def analysis_earthquake_data():
    """地震データを分析し、最も頻度の高い震源値を取得"""
    df = pd.read_csv("earthquake_data.csv")

    print(f"総データ数: {len(df)}")
    print(f"データ期間: {df['time'].min()} ～ {df['time'].max()}")

    # 震源（region）の頻度を計算
    region_counts = df['region'].value_counts()

    print("\n=== 震源頻度ランキング（上位10位） ===")
    for i, (region, count) in enumerate(region_counts.head(10).items(), 1):
        print(f"{i:2d}位: {region} - {count}回")

    # 最も頻度の高い震源
    most_frequent_region = region_counts.index[0]
    most_frequent_count = region_counts.iloc[0]

    print(f"\n=== 最も頻度の高い震源 ===")
    print(f"震源: {most_frequent_region}")
    print(f"発生回数: {most_frequent_count}回")
    print(f"全体に占める割合: {most_frequent_count/len(df)*100:.2f}%")

    return most_frequent_region, most_frequent_count

if __name__ == "__main__":
    most_frequent_region, count = analysis_earthquake_data()
