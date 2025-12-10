from intensity_analysis import analyze_max_intensity
from region_analysis import analyze_most_frequent_region

import pandas as pd


def analysis_earthquake_data():
    """地震データを分析"""
    df = pd.read_csv("earthquake_data.csv")

    print(f"総データ数: {len(df)}")
    print(f"データ期間: {df['time'].min()} ～ {df['time'].max()}")
    print()

    # 最頻震源値分析
    analyze_most_frequent_region(df)
    print()

    # 最大震度分析
    analyze_max_intensity(df)


if __name__ == "__main__":
    analysis_earthquake_data()
