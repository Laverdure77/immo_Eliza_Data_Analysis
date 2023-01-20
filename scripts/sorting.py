def get_province(_zip):
    if


# def create_country_leaderboard(df):
#     country_df = df.groupby("country")[["sales", "refunds"]].sum()
#     country_df.rename(index=str.lower, inplace=True)
#     country_df.reset_index(inplace=True)
#     country_df.sort_values(by="sales", inplace=True)
#     return country_df


# def create_country_leaderboard(df):
#     return (
#         df.groupby("country")[["sales", "refunds"]]
#           .sum()
#           .rename(index=str.lower)
#           .reset_index()
#           .sort_values(by="sales")
#     )