"""Shared input, row accounting, and proportion summaries for Q3–Q6."""

import pandas as pd
from statsmodels.stats.proportion import proportion_confint


def load_processed(root):
    """Read the shared outputs of notebook 01 without repeating its cleaning."""
    path = root / "data" / "processed" / "traffic_accidents_clean.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Missing {path}. Run 01_collection_exploration.ipynb first.")
    data = pd.read_csv(path, parse_dates=["crash_date"])
    print(f"{path.relative_to(root)}: {len(data):,} rows, {data.shape[1]} columns")
    return data


def restrict(data, mask, reason):
    """Log row changes for an analysis-specific filter."""
    result = data.loc[mask].copy()
    print(f"{reason}: {len(data):,} -> {len(result):,} rows ({len(data) - len(result):,} excluded)")
    return result


def event_summary(data, groups, outcome):
    """Count events and compute their proportion and 95% Wilson interval."""
    summary = data.groupby(groups, observed=True)[outcome].agg(
        crashes="size", events="sum"
    ).reset_index()
    summary["pct"] = 100 * summary["events"] / summary["crashes"]
    low, high = proportion_confint(summary["events"], summary["crashes"], method="wilson")
    summary["low_pct"] = 100 * low
    summary["high_pct"] = 100 * high
    return summary
