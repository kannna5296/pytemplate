import pandas as pd
import numpy as np

# 対象者の基礎データ
# 年度ごとに対象者が決まる
df = pd.DataFrame(
    data=[
        [1, 1],
        [2, np.nan],
        [np.nan, 2],
        [np.nan, np.nan],
    ],
    columns=["id1", "id2"],
)

print(df)

aa = df[["id1", "id2"]].notna()
print()
print(aa)
bb = aa.any(axis=1)
print()
print(bb)
cc = bb.all()
print()
print(cc)
