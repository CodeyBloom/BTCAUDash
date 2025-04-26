# BTCAUDash

BTCAUdash is a streamlit dashboard to show the results of backtesting various simple strategies for onboarding to Bitcoin(BTC) from the Australian Dollar(AUD).

## Motivation

I'm an aspiring ML Engineer and I wanted to work on a portfolio project that would have some real world value in my own life. I'm also interested in Misean economics and casually invest in BTC. I wanted to see if I could use my data skills to determine what my best strategy for buying BTC in Australia would be, and thought that would be a nice avenue to explore in a portfolio project.

## Tech

I'm currently using httpx to consume the data. I want to use Polars to build my own backtesting library. I will probably use Plotly and Streamlit for the visuals. If I do any model training it will probably be with XGBoost, but I may use Pytorch as well.

## Strategies

The default strategy I currently employ is DCA. This is buying a set amount of Bitcoin at a set time every week. I want to backtest a couple of other strategies against this to see if any generate alpha (better returns) over it. The first will be SMA between BTC and Tether(USDT). What this means is once I onboard into BTC, I can alternate between BTC and USDT depending on which is performing worse against it's long running mean. Using USDT here will avoid network fees from leaving the network if I do the exchanges on a platform like Binance or Coinbase, reducing the long run overheads of the strategy. I will implement more backtests after I get theese preliminaries in place.
