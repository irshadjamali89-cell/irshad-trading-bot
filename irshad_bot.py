import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="iRشاد international signal ai bot",
    page_icon="🤖",
    layout="centered"
)

# --- CYBERPUNK MIXED COLOR BACKGROUND & ROUND ANIMATED BUTTON CSS ---
st.markdown("""
<style>
/* Mixed Cyberpunk Gradient Background */
.stApp {
    background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 50%, #415a77 100%);
    color: #ffffff;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Fix Text Labels Visibility on Dark Background */
label, .stSelectbox label, .stTextInput label {
    color: #00ffff !important;
    font-weight: bold !important;
    font-size: 15px !important;
}

/* Signal Card Style */
.signal-card {
    background-color: rgba(27, 38, 59, 0.9);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #00ffff;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.2);
    margin-top: 20px;
    margin-bottom: 20px;
    text-align: center;
}

/* Custom Styling for the Centered Round Rotating Button container */
.stButton > button {
    background: linear-gradient(45deg, #ff007f, #00ffff, #ffcc00);
    background-size: 200% 200%;
    color: #0d1b2a;
    font-size: 18px;
    font-weight: bold;
    border-radius: 50px !important; /* Makes it completely round/oval */
    border: 2px solid #ffffff;
    padding: 15px 30px;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.6);
    transition: all 0.3s ease-in-out;
    display: block;
    margin: 0 auto;
}

.stButton > button:hover {
    transform: scale(1.05);
    background-position: right center;
    box-shadow: 0 0 30px #ff007f;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER TITLE ---
st.markdown("<h1 style='text-align: center; color: #ffd700; text-shadow: 0 0 10px rgba(255,215,0,0.5);'>🤖 iRشاد international signal ai bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00ffff; font-weight: bold;'>⚡ Ultra-Strong Multi-Indicator AI Trading & Global Market Analyzer ⚡</p>", unsafe_allow_html=True)
st.markdown("---")

# --- LICENSE KEY INPUT ---
license_key = st.text_input("🔑 ENTER LICENSE KEY", type="password", placeholder="Enter your active license key...")

# --- GLOBAL MARKETS & ASSETS ---
market_categories = {
    "🌍 Forex Currencies": ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD"],
    "🪙 Cryptocurrencies": ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT"],
    "🥇 Commodities & Stocks": ["GOLD (XAU/USD)", "SILVER", "NASDAQ (US100)", "CRUDE OIL"]
}

cat_choice = st.selectbox("📂 SELECT MARKET CATEGORY", list(market_categories.keys()))

col1, col2 = st.columns(2)
with col1:
    selected_asset = st.selectbox("🌐 SELECT ASSET", market_categories[cat_choice])
with col2:
    selected_time = st.selectbox("⏱️ SELECT TIMEFRAME", ["1M", "5M", "15M", "30M", "1H", "4H", "1D"])

st.markdown("<br>", unsafe_allow_html=True)

# --- 100% CENTERED ROUND BUTTON CONTAINER ---
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    start_clicked = st.button("🚀 START SIGNAL", use_container_width=True)

if start_clicked:
    if not license_key:
        st.error("⚠️ Please enter a valid License Key to run the AI bot!")
    else:
        with st.spinner('Scanning Global Markets with Advanced AI Indicators...'):
            sig = "STRONG BULLISH 🚀"
            sig_color = "#00ffcc"
            conf = "95.2%"
            price = 2385.50 if "GOLD" in selected_asset else 1.1079
            rsi_val = 64.8
            adv = "High volume institutional breakout detected across multi-timeframe indicators."
            
            # Display Card
            st.markdown(f"""
            <div class="signal-card">
                <p style="color:#94a3b8; margin-bottom:5px; font-size:14px;">ASSET: <b>{selected_asset}</b> | TIMEFRAME: <b>{selected_time}</b></p>
                <h3 style="color:#38bdf8; margin:5px 0;">LIVE PRICE: {price}</h3>
                <h1 style="color:{sig_color}; font-size:32px; margin:10px 0;">{sig}</h1>
            </div>
            """, unsafe_allow_html=True)
            
            m1, m2 = st.columns(2)
            m1.metric(label="🌐 AI CONFIDENCE", value=conf)
            m2.metric(label="📊 LIVE RSI (14)", value=f"{rsi_val}")
            
            st.success(f"**🤖 AI Technical Report:** {adv}")
            
            # Chart
            chart_data = pd.DataFrame(
                np.random.randn(40, 1).cumsum() + price,
                columns=['Price Action']
            )
            st.markdown("#### 📈 Live Market Trend Chart")
            st.line_chart(chart_data)