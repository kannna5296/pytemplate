import pandas as pd

# 対象者の基礎データ
# 年度ごとに対象者が決まる
df1 = pd.DataFrame(
    data=[
        [2023, 1],
        [2023, 2],
        [2023, 3],
        [2023, 4],
        [2024, 1],
        [2024, 2],
        [2024, 3],
        [2024, 4],
    ],
    columns=["fiscal_year", "id"],
)

# それぞれが受診を受けたかどうか
df2 = pd.DataFrame(
    data=[[2023, 1, True], [2023, 2, True], [2024, 3, False], [2024, 4, False]],
    columns=["fiscal_year", "id", "has_checkup"],
)

print("====== いわゆる普通のマージ ======")
# マージ
merged_df = pd.merge(df1, df2, how="left", on=["id", "fiscal_year"])

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
print("\nMerged DataFrame:")
print(merged_df)
