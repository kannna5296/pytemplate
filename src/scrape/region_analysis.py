import pandas as pd


def analyze_most_frequent_region(df):
    """最も頻度の高い震源値を分析"""
    print("=== 最頻震源値分析 ===")

    # 震源（region）の頻度を計算
    region_counts = df["region"].value_counts()

    print("\n震源頻度ランキング（上位10位）:")
    for i, (region, count) in enumerate(region_counts.head(10).items(), 1):
        print(f"{i:2d}位: {region} - {count}回")

    # 最も頻度の高い震源
    most_frequent_region = region_counts.index[0]
    most_frequent_count = region_counts.iloc[0]

    print(f"\n最も頻度の高い震源:")
    print(f"震源: {most_frequent_region}")
    print(f"発生回数: {most_frequent_count}回")
    print(f"全体に占める割合: {most_frequent_count/len(df)*100:.2f}%")

    return most_frequent_region, most_frequent_count
