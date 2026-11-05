import pandas as pd


def load_raw(data_path):
    """Load the original traffic accident dataset."""
    return pd.read_csv(data_path)


def load_clean(data_path):
    """Load and apply the shared baseline preprocessing."""
    df = load_raw(data_path)

    rows_before = len(df)
    df = df.drop_duplicates().copy()
    rows_after = len(df)

    print(f"Rows before removing duplicates: {rows_before:,}")
    print(f"Rows after removing duplicates: {rows_after:,}")
    print(f"Rows removed: {rows_before - rows_after:,}")

    df["crash_date"] = pd.to_datetime(
        df["crash_date"],
        format="%m/%d/%Y %I:%M:%S %p",
        errors="raise",
    )

    injury_columns = [
        "injuries_total",
        "injuries_fatal",
        "injuries_incapacitating",
        "injuries_non_incapacitating",
        "injuries_reported_not_evident",
        "injuries_no_indication",
    ]

    df[injury_columns] = df[injury_columns].astype("int64")

    df["crash_year"] = df["crash_date"].dt.year
    df["has_injury"] = df["injuries_total"] > 0
    df["has_severe_injury"] = (
        (df["injuries_fatal"] > 0)
        | (df["injuries_incapacitating"] > 0)
    )
    df["is_weekend"] = df["crash_day_of_week"].isin([1, 7])

    df["time_period"] = pd.cut(
        df["crash_hour"],
        bins=[-1, 5, 11, 17, 23],
        labels=["Night", "Morning", "Afternoon", "Evening"],
    )

    return df
