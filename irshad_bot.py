import streamlit as st
import pandas as pd
import urllib.request
import json
import os
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="iRشاد international signal ai bot",
    page_icon="📈",
    layout="centered"
)

# --- ULTRA VIP CYBERPUNK & ANIMATED DESIGN ---
st.markdown("""
<style>
    /* Full Screen Background Color */
    .stApp {
        background: radial-gradient(circle at top, #0f172a 0%, #050811 50%, #020617 100%);
        color: #ffffff;
    }

    /* Hide Default Streamlit Menu & Footer for Clean App Look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Gol Photo Logo with Neon Cyan & Gold Glow */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .logo-img {
        width: 135px;
        height: 135px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #06b6d4;
        box-shadow: 0 0 25px #06b6d4, 0 0 50px rgba(6, 182, 212, 0.5);
        transition: transform 0.3s ease;
    }
    .logo-img:hover {
        transform: scale(1.06);
        border-color: #facc15;
        box-shadow: 0 0 30px #facc15;
    }

    /* Title Styling */
    .bot-title {
        text-align: center;
        font-size: 28px;
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
        font-size: 14px;
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

# --- TOP HEADER: ROUND PHOTO LOGO & BOT NAME ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

possible_paths = [
    "irshad_logo.jpg",
    os.path.join(os.path.expanduser("~"), "Desktop", "irshad_logo.jpg"),
    os.path.join(os.getcwd(), "irshad_logo.jpg")
]

logo_html = ""
for path in possible_paths:
    if os.path.exists(path):
        img_b64 = get_base64_image(path)
        logo_html = f'<div class="logo-container"><img src="data:image/jpeg;base64,{img_b64}" class="logo-img"></div>'
        break

if logo_html:
    st.markdown(logo_html, unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align:center; font-size:65px;'>👑</div>", unsafe_allow_html=True)

st.markdown("<div class='bot-title'>iRشاد international signal ai bot</div>", unsafe_allow_html=True)
st.markdown("<div class='bot-subtitle'>⚡ Live Multi-Indicator AI Trading & Market Analyzer Pro ⚡</div>", unsafe_allow_html=True)
st.markdown("---")

# --- LIVE ASSET & TIMEFRAME SELECTOR ---
asset_tickers = {
    "Gold (XAU/USD)": "GC=F",
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "USD/JPY": "JPY=X",
    "AUD/USD": "AUDUSD=X",
    "Bitcoin (BTC/USD)": "BTC-USD",
    "Ethereum (ETH/USD)": "ETH-USD"
}

col1, col2 = st.columns(2)
with col1:
    selected_asset = st.selectbox("📊 SELECT MARKET PAIR:", list(asset_tickers.keys()))
with col2:
    selected_time = st.selectbox("⏱️ SELECT TIMEFRAME:", ["1m", "5m", "15m"])

# --- STRONGEST TECHNICAL ANALYSIS ENGINE (EMA + RSI + MACD + BOLLINGER) ---
def analyze_strong_market(ticker, interval):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval={interval}&range=1d"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=10)
        data = json.loads(res.read().decode('utf-8'))
        
        closes = [c for c in data['chart']['result'][0]['indicators']['quote'][0]['close'] if c is not None]
        if len(closes) < 25:
            return "WAIT ⏳", "50%", closes[-1] if closes else 0.0, 50.0, "Data load ho raha hai, dubara click karein.", None

        df = pd.DataFrame(closes, columns=['Close'])
        
        # 1. EMA 9 & EMA 21
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        
        # 2. RSI (14)
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # 3. MACD
        ema12 = df['Close'].ewm(span=12, adjust=False).mean()
        ema26 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = ema12 - ema26
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

        # 4. Bollinger Bands (20)
        df['SMA20'] = df['Close'].rolling(window=20).mean()
        df['STD20'] = df['Close'].rolling(window=20).std()
        df['Upper_Band'] = df['SMA20'] + (df['STD20'] * 2)
        df['Lower_Band'] = df['SMA20'] - (df['STD20'] * 2)

        last_price = df['Close'].iloc[-1]
        ema9 = df['EMA9'].iloc[-1]
        ema21 = df['EMA21'].iloc[-1]
        rsi = df['RSI'].iloc[-1]
        macd = df['MACD'].iloc[-1]
        macd_sig = df['Signal_Line'].iloc[-1]
        upper_b = df['Upper_Band'].iloc[-1]
        lower_b = df['Lower_Band'].iloc[-1]

        score = 0
        reasons = []

        # EMA Check
        if ema9 > ema21:
            score += 2
            reasons.append("EMA9 > EMA21 (Uptrend)")
        else:
            score -= 2
            reasons.append("EMA9 < EMA21 (Downtrend)")

        # MACD Check
        if macd > macd_sig:
            score += 2
            reasons.append("MACD Bullish")
        else:
            score -= 2
            reasons.append("MACD Bearish")

        # RSI Check
        if rsi < 32:
            score += 3
            reasons.append(f"RSI Oversold ({rsi:.1f})")
        elif rsi > 68:
            score -= 3
            reasons.append(f"RSI Overbought ({rsi:.1f})")
        else:
            reasons.append(f"RSI Neutral ({rsi:.1f})")

        # Bollinger Band Check
        if last_price <= lower_b:
            score += 2
            reasons.append("Lower Band Bounce")
        elif last_price >= upper_b:
            score -= 2
            reasons.append("Upper Band Rejection")

        if score >= 1:
            signal = "UP (CALL 🟢)"
            sig_color = "#10b981"
            confidence = f"{min(86 + abs(score)*2, 98)}%"
            advice = " | ".join(reasons) + " — Strong Buying Momentum!"
        else:
            signal = "DOWN (PUT 🔴)"
            sig_color = "#ef4444"
            confidence = f"{min(86 + abs(score)*2, 98)}%"
            advice = " | ".join(reasons) + " — Strong Selling Pressure!"

        return signal, sig_color, confidence, last_price, rsi, advice, df['Close'].tail(35)

    except Exception as e:
        return "ERROR ⚠️", "#facc15", "0%", 0.0, 50.0, f"Network ya Market Data Error: {str(e)}", None

# --- ROTATING ROUND START BUTTON ---
if st.button("START\nSIGNAL"):
    ticker = asset_tickers[selected_asset]
    with st.spinner("Live Market candles aur 4 Heavy Indicators scan ho rahe hain..."):
        sig, sig_color, conf, price, rsi_val, adv, chart_data = analyze_strong_market(ticker, selected_time)
    
    if price > 0:
        st.markdown(f"""
        <div class="signal-card">
            <p style="color:#94a3b8; margin-bottom:5px; font-size:14px;">ASSET: <b>{selected_asset}</b> | TIMEFRAME: <b>{selected_time}</b></p>
            <h3 style="color:#38bdf8; margin:5px 0;">LIVE ENTRY: {price:.4f}</h3>
            <h1 style="color:{sig_color}; font-size:36px; margin:10px 0;">{sig}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        m1, m2 = st.columns(2)
        m1.metric(label="🎯 SIGNAL ACCURACY", value=conf)
        m2.metric(label="📊 LIVE RSI (14)", value=f"{rsi_val:.1f}")
        
        st.success(f"💡 **AI Technical Analysis:** {adv}")
        
        if chart_data is not None:
            st.markdown("#### 📈 Live Market Movement Chart")
            st.line_chart(chart_data)
    else:
        st.error(adv)