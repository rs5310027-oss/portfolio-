import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Choose stock
stock = "AAPL"

# Download stock data
df = yf.download(stock, start="2024-01-01", end="2025-01-01")

# Moving averages
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# Create chart
fig = go.Figure()

# Stock price
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['Close'],
    mode='lines',
    name='Close Price'
))

# MA20
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['MA20'],
    mode='lines',
    name='20-Day MA'
))

# MA50
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['MA50'],
    mode='lines',
    name='50-Day MA'
))

fig.update_layout(
    title=f"{stock} Stock Price Analysis",
    xaxis_title="Date",
    yaxis_title="Price (USD)"
)

fig.show()