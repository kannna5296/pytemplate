

def analyze_max_intensity(df):
    """最大震度分析"""
    print("=== 最大震度分析 ===")

    # 最大震度ランキング
    print("\n最大震度ランキング（上位3位）:")
    intensity_counts = df["max_intensity"].value_counts().sort_index(ascending=False)
    for i, (intensity, count) in enumerate(intensity_counts.head(3).items(), 1):
        print(f"{i:2d}位: 震度{intensity} - {count}回")

        # その震度の詳細情報（日時、震源、マグニチュード）
        intensity_data = df[df["max_intensity"] == intensity].sort_values(
            "time", ascending=False
        )
        print("    詳細:")
        for _, row in intensity_data.iterrows():  # 全ての件数を表示
            print(f"      {row['time']} - {row['region']} - M{row['magnitude']}")
        print()

    return intensity_counts
