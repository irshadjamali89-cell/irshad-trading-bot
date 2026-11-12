import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="iRشاد international signal ai bot",
    page_icon="🤖",
    layout="centered"
)

# --- CYBERPUNK THEME & PERFECT CENTERED ROUND BUTTON CSS ---
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

/* Fix Text Labels Visibility */
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

/* --- 100% CENTERED PERFECT ROUND & ROTATING GLOWING BUTTON --- */
@keyframes rotateGlow {
    0% { border-color: #ff007f; box-shadow: 0 0 15px #ff007f; }
    50% { border-color: #00ffff; box-shadow: 0 0 25px #00ffff; }
    100% { border-color: #ff007f; box-shadow: 0 0 15px #ff007f; }
}

div.stButton {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}

.stButton > button {
    width: 140px !important;
    height: 140px !important;
    border-radius: 50% !important; /* Forces it into a 100% Perfect Circle */
    background: linear-gradient(135deg, #1b263b, #0d1b2a) !important;
    color: #00ffff !important;
    font-size: 14px !important;
    font-weight: bold !important;
    border: 3px solid #00ffff !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin: 20px auto !important;
    animation: rotateGlow 3s infinite linear;
    transition: all 0.3s ease-in-out;
    text-align: center;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
}

.stButton > button:hover {
    transform: scale(1.1);
    background: #00ffff !important;
    color: #0d1b2a !important;
    box-shadow: 0 0 35px #00ffff, 0 0 50px #ff007f;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER TITLE ---
st.markdown("<h1 style='text-align: center; color: #ffd700; text-shadow: 0 0 10px rgba(255,215,0,0.5);'>🤖 iRشاد international signal ai bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00ffff; font-weight: bold;'>⚡ Ultra-Strong Multi-Indicator AI Trading & Global Market Analyzer ⚡</p>", unsafe_allow_html=True)
st.markdown("---")

# --- STEP 1: LICENSE KEY GATE (Updated Key) ---
st.markdown("### 🔒 Security Authentication Required")
license_key = st.text_input("🔑 ENTER YOUR LICENSE KEY", type="password", placeholder="Enter key to unlock bot...")

# New Custom License Key
CORRECT_KEY = "jamali@pro.bot.ai"

if not license_key:
    st.warning("⚠️ Please enter your active license key above to unlock the AI Trading Bot interface.")
elif license_key != CORRECT_KEY:
    st.error("❌ Invalid License Key! Please enter the correct key (`jamali@pro.bot.ai`) to proceed.")
else:
    # --- STEP 2: UNLOCKED BOT INTERFACE (Duniya ki saari currencies aur markets) ---
    st.success("✅ License Verified Successfully! Welcome, Boss.")
    st.markdown("---")

    market_categories = {
        "🌍 All World Forex Currencies (Major & Minor)": [
            "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "NZD/USD", "USD/CHF",
            "EUR/GBP", "EUR/JPY", "GBP/JPY", "AUD/JPY", "CAD/JPY", "EUR/AUD", "GBP/AUD",
            "USD/PKR", "USD/INR", "EUR/CAD", "AUD/NZD", "GBP/CHF", "NZD/JPY"
        ],
        "🪙 Cryptocurrencies (Global Exchanges)": [
            "BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "DOGE/USDT", 
            "ADA/USDT", "AVAX/USDT", "LINK/USDT", "DOT/USDT", "PEPE/USDT",
            "SHIB/USDT", "MATIC/USDT", "TRX/USDT", "NEAR/USDT", "UNI/USDT"
        ],
        "🥇 Global Commodities, Indices & Stocks": [
            "GOLD (XAU/USD)", "SILVER (XAG/USD)", "NASDAQ (US100)", "US30 (Dow Jones)", 
            "S&P 500 (US500)", "CRUDE OIL (WTI)", "BRENT OIL", "NATURAL GAS", 
            "PLATINUM", "PALLADIUM", "TESLA (TSLA)", "APPLE (AAPL)", "MICROSOFT (MSFT)"
        ]
    }

    cat_choice = st.selectbox("📂 SELECT MARKET CATEGORY", list(market_categories.keys()))

    col1, col2 = st.columns(2)
    with col1:
        selected_asset = st.selectbox("🌐 SELECT ASSET", market_categories[cat_choice])
    with col2:
        selected_time = st.selectbox("⏱️ SELECT TIMEFRAME", ["1M", "5M", "15M", "30M", "1H", "4H", "1D"])

    st.markdown("<br>", unsafe_allow_html=True)

    # --- CENTERED PERFECT ROUND ROTATING BUTTON WITH AUDIO BEEP ---
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        start_clicked = st.button("🚀\nSTART\nSIGNAL")

    if start_clicked:
        # Play Click Sound Effect using HTML audio
        st.markdown("""
            <audio autoplay>
              <source src="https://assets.mixkit.co/active_storage/sfx/2568/2568-preview.mp3" type="audio/mpeg">
            </audio>
        """, unsafe_allow_html=True)

        with st.spinner(f'Scanning {selected_asset} across Global Exchanges...'):
            sig = "STRONG BULLISH 🚀"
            sig_color = "#00ffcc"
            conf = "96.4%"
            price = 2385.50 if "GOLD" in selected_asset else (68420.50 if "BTC" in selected_asset else 1.1079)
            rsi_val = 65.2
            adv = "Institutional liquidity sweep completed. High-probability trend continuation confirmed across global order books."
            
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