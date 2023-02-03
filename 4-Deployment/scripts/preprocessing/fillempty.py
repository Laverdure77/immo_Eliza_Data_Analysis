import pandas as pd

# Fill the df missing values with 0
def fillempty(_df : pd.DataFrame) -> pd.DataFrame:
    _df = _df.fillna(value = 0)
    return _df
