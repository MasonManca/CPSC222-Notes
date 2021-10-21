import pandas as pd

def warm_up_task():
    msrp_df = pd.read_csv("msrp.csv")
    
    new_row = pd.Series(["chevy corvette", 77, 2212], index = ["CarName", "ModelYear", "MSRP"])
    msrp_df = msrp_df.append(new_row, ignore_index=True)
    print(msrp_df)
    counts_ser = msrp_df["ModelYear"].value_counts()
    print(counts_ser)

    grouped_df = msrp_df.groupby("ModelYear")
    mean_ser = grouped_df["MSRP"].mean()
    print(mean_ser)


warm_up_task()