import streamlit as st
import pandas as pd
import urllib.request
import json

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="iRشاد international signal ai bot",
    page_icon="🔥",
    layout="centered"
)

# --- ULTRA VIP CYBERPUNK & MOVING ANIMATED DESIGN ---
st.markdown("""
<style>
    /* Full Screen Background Color */
    .stApp {
        background: radial-gradient(circle at top, #0f172a 0%, #050811 50%, #020617 100%);
        color: #ffffff;
    }

    /* Hide Default Streamlit Menu & Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Moving / Floating Animation for Header Icon */
    @keyframes moveIcon {
        0% { transform: translateY(0px) scale(1); text-shadow: 0 0 15px #06b6d4; }
        50% { transform: translateY(-8px) scale(1.08); text-shadow: 0 0 30px #facc15, 0 0 50px #38bdf8; }
        100% { transform: translateY(0px) scale(1); text-shadow: 0 0 15px #06b6d4; }
    }

    .logo-container {
        text-align: center;
        font-size: 60px;
        margin-top: 10px;
        margin-bottom: 5px;
        animation: moveIcon 3s ease-in-out infinite;
    }

    /* Title Styling */
    .bot-title {
        text-align: center;
        font-size: 26px;
        font-weight: 900;
        background: linear-gradient(90deg, #38bdf8, #facc15, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
        letter-spacing: 1px;
    }
    .bot-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* Har Waqt Ghoomne Wala (Rotating) Gol Start Button */
    @keyframes spinButton {
        0% { transform: rotate(0deg); box-shadow: 0 0 20px #ef4444, 0 0 40px #06b6d4; }
        50% { transform: rotate(180deg); box-shadow: 0 0 30px #10b981, 0 0 50px #facc15; }
        100% { transform: rotate(360deg); box-shadow: 0 0 20px #ef4444, 0 0 40px #06b6d4; }
    }

    div.stButton > button {
        width: 145px !important;
        height: 145px !important;
        border-radius: 50% !important;
        background: radial-gradient(circle, #dc2626 0%, #7f1d1d 100%) !important;
        color: #ffffff !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        letter-spacing: 1px !important;
        border: 4px dashed #38bdf8 !important;
        display: block !important;
        margin: 25px auto !important;
        animation: spinButton 6s linear infinite !important;
        cursor: pointer !important;
        text-align: center !important;
    }

    div.stButton > button:hover {
        animation-play-state: paused !important;
        background: radial-gradient(circle, #10b981 0%, #065f46 100%) !important;
        border-color: #facc15 !important;
        transform: scale(1.08) !important;
    }

    /* Signal Result Card */
    .signal-card {
        background: rgba(15, 23, 42, 0.85);
        border: 2px solid #06b6d4;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 25px rgba(6, 182, 212, 0.25);
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- LICENSE KEY SECURITY GATEWAY ---
VALID_KEYS = ["jamali@pro.bot.ai", "IRSHAD-2026-VIP"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<div class='bot-title'>🔐 iRشاد SECURE GATEWAY</div>", unsafe_allow_html=True)
    st.markdown("<div class='bot-subtitle'>Apna Master License Key darj karein</div>", unsafe_allow_html=True)
    user_key = st.text_input("Master License Key", type="password", placeholder="Enter Key Here...")
    
    if st.button("START\nUNLOCK"):
        if user_key in VALID_KEYS:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Invalid License Key! Access Denied.")
    st.stop()

# --- TOP HEADER: MOVING ICON & BOT NAME ---
st.markdown("<div class='logo-container'>😎🔥⚡</div>", unsafe_allow_html=True)
st.markdown("<div class='bot-title'>iRشاد international signal ai bot</div>", unsafe_allow_html=True)
st.markdown("<div class='bot-subtitle'>⚡ Ultra-Strong Multi-Indicator AI Trading & Global Market Analyzer ⚡</div>", unsafe_allow_html=True)
st.markdown("---")

# --- COMPLETE GLOBAL ASSETS (CURRENCIES, CRYPTO, STOCKS, METALS) ---
asset_tickers = {
    "EUR/USD (Euro / US Dollar)": "EURUSD=X",
    "GBP/USD (British Pound / US Dollar)": "GBPUSD=X",
    "USD/JPY (US Dollar / Japanese Yen)": "JPY=X",
    "AUD/USD (Australian Dollar / US Dollar)": "AUDUSD=X",
    "USD/CAD (US Dollar / Canadian Dollar)": "USDCAD=X",
    "NZD/USD (New Zealand Dollar / US Dollar)": "NZDUSD=X",
    "USD/CHF (US Dollar / Swiss Franc)": "USDCHF=X",
    "GBP/JPY (Pound / Yen)": "GBPJPY=X",
    "EUR/JPY (Euro / Yen)": "EURJPY=X",
    "EUR/GBP (Euro / British Pound)": "EURGBP=X",
    "Gold (XAU/USD)": "GC=F",
    "Silver (XAG/USD)": "SI=F",
    "Crude Oil (WTI)": "CL=F",
    "Natural Gas": "NG=F",
    "Bitcoin (BTC/USD)": "BTC-USD",
    "Ethereum (ETH/USD)": "ETH-USD",
    "Binance Coin (BNB/USD)": "BNB-USD",
    "Solana (SOL/USD)": "SOL-USD",
    "Ripple (XRP/USD)": "XRP-USD",
    "Cardano (ADA/USD)": "ADA-USD",
    "S&P 500 (US Stock Index)": "^GSPC",
    "NASDAQ (Tech Stocks Index)": "^IXIC",
    "Dow Jones (US 30)": "^DJI",
    "FTSE 100 (UK Stocks)": "^FTSE",
    "DAX (Germany Stocks)": "^GDAXI",
    "Nikkei 225 (Japan Stocks)": "^N225"
}

col1, col2 = st.columns(2)
with col1:
    selected_asset = st.selectbox("📊 SELECT GLOBAL MARKET:", list(asset_tickers.keys()))
with col2:
    selected_time = st.selectbox("⏱️ SELECT TIMEFRAME:", ["1m", "5m", "15m", "30m", "1h"])

# --- HEAVY & STRONG AI TECHNICAL ANALYSIS ENGINE ---
def analyze_heavy_market(ticker, interval):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval={interval}&range=1d"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=10)
        data = json.loads(res.read().decode('utf-8'))
        
        closes = [c for c in data['chart']['result'][0]['indicators']['quote'][0]['close'] if c is not None]
        if len(closes) < 30:
            return "WAIT ⏳", "#facc15", "50%", closes[-1] if closes else 0.0, 50.0, "Market data syncing, click again.", None

        df = pd.DataFrame(closes, columns=['Close'])
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()
        
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        ema12 = df['Close'].ewm(span=12, adjust=False).mean()
        ema26 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = ema12 - ema26
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

        df['SMA20'] = df['Close'].rolling(window=20).mean()
        df['STD20'] = df['Close'].rolling(window=20).std()
        df['Upper_Band'] = df['SMA20'] + (df['STD20'] * 2)
        df['Lower_Band'] = df['SMA20'] - (df['STD20'] * 2)

        last_price = df['Close'].iloc[-1]
        ema9 = df['EMA9'].iloc[-1]
        ema21 = df['EMA21'].iloc[-1]
        ema50 = df['EMA50'].iloc[-1]
        rsi = df['RSI'].iloc[-1]
        macd = df['MACD'].iloc[-1]
        macd_sig = df['Signal_Line'].iloc[-1]
        upper_b = df['Upper_Band'].iloc[-1]
        lower_b = df['Lower_Band'].iloc[-1]

        score = 0
        reasons = []

        if ema9 > ema21 and ema21 > ema50:
            score += 3
            reasons.append("Super Bullish EMA Alignment")
        elif ema9 < ema21 and ema21 < ema50:
            score -= 3
            reasons.append("Super Bearish EMA Alignment")
        elif ema9 > ema21:
            score += 1
            reasons.append("EMA9 > EMA21")
        else:
            score -= 1
            reasons.append("EMA9 < EMA21")

        if macd > macd_sig:
            score += 2
            reasons.append("MACD Bullish Cross")
        else:
            score -= 2
            reasons.append("MACD Bearish Cross")

        if rsi < 28:
            score += 3
            reasons.append(f"RSI Deep Oversold ({rsi:.1f})")
        elif rsi > 72:
            score -= 3
            reasons.append(f"RSI Deep Overbought ({rsi:.1f})")
        elif rsi < 45:
            score -= 1
            reasons.append(f"RSI Bearish Zone ({rsi:.1f})")
        else:
            score += 1
            reasons.append(f"RSI Bullish Zone ({rsi:.1f})")

        if last_price <= lower_b:
            score += 2
            reasons.append("Lower Bollinger Touch (Bounce)")
        elif last_price >= upper_b:
            score -= 2
            reasons.append("Upper Bollinger Touch (Drop)")

        if score >= 2:
            signal = "UP (CALL 🟢)"
            sig_color = "#10b981"
            confidence = f"{min(89 + abs(score)*2, 99.5)}%"
            advice = " | ".join(reasons) + " — Heavy Bullish Confluence!"
        elif score <= -2:
            signal = "DOWN (PUT 🔴)"
            sig_color = "#ef4444"
            confidence = f"{min(89 + abs(score)*2, 99.5)}%"
            advice = " | ".join(reasons) + " — Heavy Bearish Confluence!"
        else:
            signal = "HOLD / NEUTRAL ⚪"
            sig_color = "#facc15"
            confidence = "76%"
            advice = " | ".join(reasons) + " — Market Consolidation, Wait."

        return signal, sig_color, confidence, last_price, rsi, advice, df['Close'].tail(40)

    except Exception as e:
        return "ERROR ⚠️", "#ef4444", "0%", 0.0, 50.0, f"API Data Error: {str(e)}", None

# --- ROTATING ROUND START BUTTON ---
if st.button("START\nSIGNAL"):
    ticker = asset_tickers[selected_asset]
    with st.spinner("Scanning Global Markets with 5 Indicators..."):
        sig, sig_color, conf, price, rsi_val, adv, chart_data = analyze_heavy_market(ticker, selected_time)
    
    if price > 0:
        st.markdown(f"""
        <div class="signal-card">
            <p style="color:#94a3b8; margin-bottom:5px; font-size:14px;">ASSET: <b>{selected_asset}</b> | TIMEFRAME: <b>{selected_time}</b></p>
            <h3 style="color:#38bdf8; margin:5px 0;">LIVE PRICE: {price:.4f}</h3>
            <h1 style="color:{sig_color}; font-size:34px; margin:10px 0;">{sig}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        m1, m2 = st.columns(2)
        m1.metric(label="🎯 AI CONFIDENCE", value=conf)
        m2.metric(label="📊 LIVE RSI (14)", value=f"{rsi_val:.1f}")
        
        st.success(f"💡 **Deep AI Technical Report:** {adv}")
        
        if chart_data is not None:
            st.markdown("#### 📈 Live Market Trend Chart")
            st.line_chart(chart_data)
    else:
        st.error(adv)