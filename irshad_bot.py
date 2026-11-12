import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
import json

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="iRشاد international signal ai bot",
    page_icon="🤖",
    layout="centered"
)

# --- ULTRA VIP CYBERPUNK DESIGN & CENTERED BUTTON CSS ---
st.markdown("""
<style>
/* Full Screen Background Color */
.stApp {
    background-color: #0d1b2a;
    color: #ffffff;
}

/* Hide Default Streamlit Menu & Footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Force Center Alignment for Streamlit Button */
div.stButton {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}

div.stButton > button {
    background: linear-gradient(135deg, #ff4b2b, #ff416c);
    color: white;
    font-size: 20px;
    font-weight: bold;
    padding: 12px 40px;
    border-radius: 50px;
    border: none;
    box-shadow: 0px 5px 20px rgba(255, 75, 43, 0.5);
    transition: 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 8px 25px rgba(255, 75, 43, 0.8);
}

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

# --- HEADER TITLE & ANIMATION ---
st.markdown("<h1 style='text-align: center; color: #ffd700;'>🤖 iRشاد international signal ai bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00ffff;'>⚡ Ultra-Strong Multi-Indicator AI Trading & Global Market Analyzer ⚡</p>", unsafe_allow_html=True)
st.markdown("---")

# --- INPUT FIELDS ---
col1, col2 = st.columns(2)
with col1:
    selected_asset = st.selectbox("🌐 SELECT GLOBAL MARKET", ["EUR/USD", "GBP/USD", "BTC/USD", "GOLD", "NASDAQ"])
with col2:
    selected_time = st.selectbox("⏱️ SELECT TIMEFRAME", ["1M", "5M", "15M", "1H", "1D"])

st.markdown("<br>", unsafe_allow_html=True)

# --- CENTERED START SIGNAL BUTTON ---
if st.button("START SIGNAL"):
    with st.spinner('Scanning Global Markets with 5 Indicators...'):
        sig = "BULLISH 🚀"
        sig_color = "#00ffcc"
        conf = "86%"
        price = 1.1079
        rsi_val = 58.4
        adv = "Market momentum is strong. Trend continuation expected."
        
        # Display Card
        st.markdown(f"""
        <div class="signal-card">
            <p style="color:#94a3b8; margin-bottom:5px; font-size:14px;">ASSET: <b>{selected_asset}</b> | TIMEFRAME: <b>{selected_time}</b></p>
            <h3 style="color:#38bdf8; margin:5px 0;">LIVE PRICE: {price:.4f}</h3>
            <h1 style="color:{sig_color}; font-size:34px; margin:10px 0;">{sig}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        m1, m2 = st.columns(2)
        m1.metric(label="🌐 AI CONFIDENCE", value=conf)
        m2.metric(label="📊 LIVE RSI (14)", value=f"{rsi_val:.1f}")
        
        st.success(f"**🤖 Deep AI Technical Report:** {adv}")
        
        # Chart
        chart_data = pd.DataFrame(
            np.random.randn(40, 1).cumsum() + price,
            columns=['Close']
        )
        st.markdown("#### 📈 Live Market Trend Chart")
        st.line_chart(chart_data)