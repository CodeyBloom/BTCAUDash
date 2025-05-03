import polars as pl


def backtest(df: pl.DataFrame) -> pl.DataFrame:
    """This will construct a backtested dataframe for visualization purposes"""
    return (
        df.with_columns(
            # Add a column for the formatted time
            pl.from_epoch(pl.col("timestamp"), time_unit="ms").alias("formatted_time"),
        )
        .with_columns(
            # Add the columns for weekly recurring investment
            pl.when(pl.col("formatted_time").dt.weekday() == 6)
            .then(50)
            .otherwise(0)
            .alias("weekly_$50"),
            pl.when(pl.col("formatted_time").dt.weekday() == 6)
            .then(200)
            .otherwise(0)
            .alias("weekly_$200"),
        )
        .with_columns(
            # Add the columns for bitcoin accrued from weekly recurring investment
            (pl.col("weekly_$50") / pl.col("price")).alias("weekly_$50_BTCrued"),
            (pl.col("weekly_$200") / pl.col("price")).alias("weekly_$200_BTCrued"),
        )
        .with_columns(
            # Add the cummulative sum of both bitcoin accrued and investment amounts
            pl.col("weekly_$50").cum_sum().alias("weekly_$50_cummulative"),
            pl.col("weekly_$200").cum_sum().alias("weekly_$200_cummulative"),
            pl.col("weekly_$50_BTCrued")
            .cum_sum()
            .alias("weekly_$50_BTCrued_cummulative"),
            pl.col("weekly_$200_BTCrued")
            .cum_sum()
            .alias("weekly_$200_BTCrued_cummulative"),
        )
        .with_columns(
            # Calcluate the returns
            (
                (
                    (pl.col("weekly_$50_BTCrued_cummulative") * pl.col("price"))
                    - pl.col("weekly_$50_cummulative")
                )
                / pl.col("weekly_$50_cummulative")
            ).alias("$50_DCA_returns"),
            (
                (
                    (pl.col("weekly_$200_BTCrued_cummulative") * pl.col("price"))
                    - pl.col("weekly_$200_cummulative")
                )
                / pl.col("weekly_$200_cummulative")
            ).alias("$200_DCA_returns"),
        )
    )


pretest = pl.read_parquet("raw_data.parquet")
tested = backtest(pretest)
tested.write_parquet("backtested.parquet")
