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
    # Dark background
    paper_bgcolor="rgba(0,0,0,0)",  # Transparent background
    plot_bgcolor="rgba(0,0,0,0)",  # Transparent plot area
    # White text and grid lines
    font_color="white",
    title_font_color="white",
    legend_font_color="white",
    # Grid styling
    xaxis=dict(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.1)",
        tickfont=dict(color="white"),
        title_font=dict(color="white"),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.1)",
        tickfont=dict(color="white"),
        title_font=dict(color="white"),
    ),
    # Legend positioning
    legend=dict(
        orientation="h", y=1.1, x=0.5, xanchor="center", font=dict(color="white")
    ),
)

sample_fig.write_html("toggle_lines.html", include_plotlyjs="cdn")
