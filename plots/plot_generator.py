import plotly.graph_objects as go
import polars as pl

df = pl.read_parquet("../data/backtested.parquet")

sample_fig = go.Figure()

for line in ["weekly_$50_BTCrued_cummulative", "weekly_$200_BTCrued_cummulative"]:
    sample_fig.add_trace(
        go.Scatter(
            x=df["formatted_time"].to_list(),
            y=df[line].to_list(),
            name=line,
            mode="lines",
        )
    )

sample_fig.update_layout(
    title="Time Series Comparison",
    legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"),
)

sample_fig.write_html("toggle_lines.html", include_plotlyjs="cdn")
