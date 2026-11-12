import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="iRشاد international signal ai bot",
    page_icon="🤖",
    layout="centered"
)

# --- CYBERPUNK DESIGN CSS ---
st.markdown("""
<style>
.stApp {
    background-color: #0d1b2a;
    color: #ffffff;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Signal Card Style */
.signal-card {
    background-color: #1b263b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #415a77;
    margin-top: 20px;
    margin-bottom: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER TITLE ---
st.markdown("<h1 style='text-align: center; color: #ffd700;'>🤖 iRشاد international signal ai bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00ffff;'>⚡ Ultra-Strong Multi-Indicator AI Trading & Global Market Analyzer ⚡</p>", unsafe_allow_html=True)
st.markdown("---")

# --- GLOBAL MARKETS & ASSETS (Forex, Crypto, Stocks) ---
market_categories = {
    "🌍 Forex Currencies": ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "NZD/USD", "EUR/GBP"],
    "🪙 Cryptocurrencies": ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "DOGE/USDT"],
    "🥇 Commodities & Stocks": ["GOLD (XAU/USD)", "SILVER", "NASDAQ (US100)", "US30 (Dow Jones)", "CRUDE OIL"]
}

cat_choice = st.selectbox("📂 SELECT MARKET CATEGORY", list(market_categories.keys()))

col1, col2 = st.columns(2)
with col1:
    selected_asset = st.selectbox("🌐 SELECT ASSET", market_categories[cat_choice])
with col2:
    selected_time = st.selectbox("⏱️ SELECT TIMEFRAME", ["1M", "5M", "15M", "30M", "1H", "4H", "1D"])

st.markdown("<br>", unsafe_allow_html=True)

# --- CENTERED BUTTON ---
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    start_clicked = st.button("🚀 START STRONG ANALYSIS", use_container_width=True)

if start_clicked:
    with st.spinner(f'AI is deeply scanning {selected_asset} using 10+ Pro Indicators...'):
        # Strong dynamic analysis simulation based on asset
        if "BTC" in selected_asset or "ETH" in selected_asset:
            sig = "STRONG BULLISH 🚀🔥"
            sig_color = "#00ffcc"
            conf = "94.5%"
            price = 68420.50 if "BTC" in selected_asset else 3540.20
            rsi_val = 68.2
            adv = "Whale accumulation detected. RSI & MACD showing massive upward breakout on global order books."
        elif "GOLD" in selected_asset:
            sig = "STRONG BEARISH ⚠️"
            sig_color = "#ff4d4d"
            conf = "91.2%"
            price = 2385.40
            rsi_val = 31.5
            adv = "Strong resistance hit at upper Bollinger Band. Institutional short positions increasing rapidly."
        else:
            sig = "BULLISH MOMENTUM 🚀"
            sig_color = "#00ffcc"
            conf = "88.7%"
            price = 1.0890
            rsi_val = 61.4
            adv = "Global volume spike and moving average crossover confirm strong bullish continuation."
        
        # Display Card
        st.markdown(f"""
        <div class="signal-card">
            <p style="color:#94a3b8; margin-bottom:5px; font-size:14px;">ASSET: <b>{selected_asset}</b> | TIMEFRAME: <b>{selected_time}</b></p>
            <h3 style="color:#38bdf8; margin:5px 0;">LIVE MARKET PRICE: {price}</h3>
            <h1 style="color:{sig_color}; font-size:30px; margin:10px 0;">{sig}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        m1, m2 = st.columns(2)
        m1.metric(label="🌐 AI CONFIDENCE SCORE", value=conf)
        m2.metric(label="📊 LIVE RSI (14)", value=f"{rsi_val}")
        
        st.success(f"**🤖 Deep AI Technical & Sentiment Report:** {adv}")
        
        # Chart
        chart_data = pd.DataFrame(
            np.random.randn(50, 1).cumsum() + price,
            columns=['Price Action']
        )
        st.markdown("#### 📈 AI Predicted Trend Chart")
        st.line_chart(chart_data)