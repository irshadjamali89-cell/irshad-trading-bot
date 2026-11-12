import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="Irshad Jamali AI Trading Bot",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #080d18;
    color: white;
}
h1,h2,h3 {
    color: #00d9ff !important;
}
.stButton>button {
    background: linear-gradient(90deg,#006eff,#00d9ff);
    color: white;
    border-radius: 12px;
    font-weight: bold;
    width: 100%;
}
[data-testid="stMetric"] {
    background: #111d30;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #087dba;
}
</style>
""", unsafe_allow_html=True)

LICENSE = "jamali@.154"

st.title("🤖 IRSHAD JAMALI AI BOT")
st.caption("ADVANCED MARKET ANALYSIS SYSTEM")

# LICENSE
key = st.text_input("🔐 Enter License Key", type="password")

if key != LICENSE:
    st.warning("Please enter your valid license key.")
    st.stop()

st.success("License Activated")

# CURRENCY
currencies = {
    "Gold (XAUUSD)": "GC=F",
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "USD/JPY": "JPY=X",
    "AUD/USD": "AUDUSD=X",
    "USD/CAD": "CAD=X",
    "USD/CHF": "CHF=X",
    "NZD/USD": "NZDUSD=X",
    "Bitcoin": "BTC-USD",
    "Ethereum": "ETH-USD"
}

col1, col2 = st.columns(2)

with col1:
    market = st.selectbox(
        "Select Market",
        list(currencies.keys())
    )

with col2:
    interval = st.selectbox(
        "Timeframe",
        ["5m", "15m", "30m", "1h", "1d"]
    )

risk = st.slider("Risk Percentage", 0.5, 3.0, 1.0)

if st.button("🚀 START BOT ANALYSIS"):

    ticker = currencies[market]

    try:
        with st.spinner("AI Robot analyzing market..."):

            data = yf.download(
                ticker,
                period="5d",
                interval=interval,
                progress=False,
                auto_adjust=True
            )

            if data.empty:
                st.error("Market data unavailable.")
                st.stop()

            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)

            close = data["Close"].dropna()

            if len(close) < 30:
                st.error("Not enough market data.")
                st.stop()

            # EMA 20
            ema20 = close.ewm(span=20, adjust=False).mean()

            # RSI 12
            delta = close.diff()
            gain = delta.clip(lower=0)
            loss = -delta.clip(upper=0)

            avg_gain = gain.ewm(
                alpha=1/12,
                adjust=False
            ).mean()

            avg_loss = loss.ewm(
                alpha=1/12,
                adjust=False
            ).mean()

            rs = avg_gain / avg_loss.replace(0, np.nan)
            rsi = 100 - (100 / (1 + rs))

            price = float(close.iloc[-1])
            ema = float(ema20.iloc[-1])
            rsi_value = float(rsi.iloc[-1])

            # SIGNAL
            if price > ema and rsi_value > 50:
                signal = "BUY"
                direction = "BULLISH"

            elif price < ema and rsi_value < 50:
                signal = "SELL"
                direction = "BEARISH"

            else:
                signal = "WAIT"
                direction = "SIDEWAYS"

            # ATR STOP LOSS
            high = data["High"]
            low = data["Low"]

            previous_close = close.shift(1)

            tr = pd.concat([
                high - low,
                (high - previous_close).abs(),
                (low - previous_close).abs()
            ], axis=1).max(axis=1)

            atr = float(tr.ewm(span=14).mean().iloc[-1])

            if not np.isfinite(atr) or atr <= 0:
                st.error("ATR calculation unavailable.")
                st.stop()

            if signal == "BUY":
                sl = price - (atr * 1.5)
                tp = price + (atr * 3)

            elif signal == "SELL":
                sl = price + (atr * 1.5)
                tp = price - (atr * 3)

            else:
                sl = np.nan
                tp = np.nan

            st.divider()

            st.subheader("🤖 ROBOT MARKET REPORT")

            a, b, c = st.columns(3)

            a.metric("Market Price", round(price, 5))
            b.metric("EMA 20", round(ema, 5))
            c.metric("RSI 12", round(rsi_value, 2))

            if signal == "BUY":
                st.success("🟢 BUY SIGNAL")

            elif signal == "SELL":
                st.error("🔴 SELL SIGNAL")

            else:
                st.warning("🟡 WAIT - No clear signal")

            st.subheader("📊 Trade Plan")

            x, y, z = st.columns(3)

            x.metric("ENTRY", round(price, 5))

            if signal != "WAIT":
                y.metric("STOP LOSS", round(sl, 5))
                z.metric("TAKE PROFIT", round(tp, 5))
            else:
                y.metric("STOP LOSS", "Not set")
                z.metric("TAKE PROFIT", "Not set")

            st.write("Market Direction:", direction)

            st.write(
                "Signal Time:",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            st.subheader("📈 Price Chart")

            chart = pd.DataFrame({
                "Price": close,
                "EMA 20": ema20
            })

            st.line_chart(chart)

            st.subheader("📋 Recent Market Data")
            st.dataframe(data.tail(10))

            st.info(
                "Signals are indicator-based, not guaranteed. "
                "Verify spreads, execution and market conditions "
                "before any real trade."
            )

    except Exception as e:
        st.error(f"Analysis Error: {e}")

st.divider()
st.caption("© Irshad Jamali | AI Trading Dashboard")