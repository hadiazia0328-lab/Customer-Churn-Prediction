import sys
from datetime import datetime
from pathlib import Path

import streamlit as st

# Project folder setup
PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR))

from src.predict import predict_churn

# Page settings
st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊", layout="wide")

# ----------------------------------------------------------------------------
# Styling (ocean palette)
# ----------------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Manrope:wght@400;500;600;700&display=swap');
.stApp, .stApp p, .stApp label, .stApp input, .stApp button, .stApp li { font-family: 'Manrope', sans-serif; }
.stApp { background: #E6F0F7; color: #0D2B45; }
[data-testid="stHeader"] { background: transparent; }
footer { visibility: hidden; }
.block-container { padding-top: 2rem; max-width: 1150px; }
[data-testid="stSidebar"] { background: #0D2B45; }
[data-testid="stSidebar"] * { color: #EAF3F9; }
[data-testid="stSidebarHeader"] { height: 2.2rem; min-height: 2.2rem; padding: 0.4rem 0.8rem; }
[data-testid="stSidebarUserContent"] { padding-top: 0 !important; }
h1, h2, h3, .serif { font-family: 'Fraunces', Georgia, serif !important; color: #0D2B45; letter-spacing: -.01em; }
[data-testid="stVerticalBlockBorderWrapper"] { background: #F7FBFD; border-color: #B7D4E6 !important; border-radius: 18px; }
[data-baseweb="select"] > div, .stNumberInput input { border-radius: 10px; }
.card { background: #F7FBFD; border: 1px solid #B7D4E6; border-radius: 18px; padding: 20px 22px; margin-bottom: 16px; }
.card.t { background: #DCEAF3; }
.card h3 { margin: 0 0 4px 0; font-size: 19px; }
.kl { color: #3F6578; font-size: 14px; margin: 0; }
.kpi { font-family: 'Fraunces', serif; font-size: 38px; font-weight: 700; line-height: 1.15; margin: 6px 0 2px 0; }
.bw { margin-bottom: 14px; }
.bw .h { display: flex; justify-content: space-between; font-size: 14px; }
.bt { height: 9px; border-radius: 5px; background: #C9DDEA; margin-top: 5px; overflow: hidden; }
.bt i { display: block; height: 100%; border-radius: 5px; background: #1E5A6E; }
.bw.up .bt i { background: #9A6B2C; }
.pill { display: inline-block; margin-top: 10px; padding: 5px 14px; border-radius: 99px; font-weight: 700; font-size: 14px; }
.pill.leave { background: #DCC8AA; color: #0D2B45; }
.pill.stay { background: #6BA7A0; color: #0D2B45; }
.pill.idle { background: #F7FBFD; color: #3F6578; }
.gauge { width: 150px; height: 150px; border-radius: 50%; display: grid; place-items: center;
         background: conic-gradient(#1E5A6E calc(var(--p) * 1%), #B7D4E6 0); }
.gauge span { width: 114px; height: 114px; border-radius: 50%; background: #DCEAF3; display: grid; place-items: center;
              font-family: 'Fraunces', serif; font-size: 34px; font-weight: 700; }
.hero { display: flex; gap: 20px; align-items: center; flex-wrap: wrap; }
.row { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #C9DDEA; font-size: 14px; }
.row:last-child { border-bottom: 0; }
.row small { color: #3F6578; display: block; }
.row b { font-family: 'Fraunces', serif; font-size: 20px; }
.step { display: flex; gap: 14px; }
.step .n { flex: none; width: 34px; height: 34px; border-radius: 50%; background: #1E5A6E; color: #F7FBFD;
           display: grid; place-items: center; font: 700 16px 'Fraunces', serif; }
.step p { margin: 0; font-size: 14px; color: #3F6578; }
.score { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
.score div { flex: 1; min-width: 120px; padding: 12px; border-radius: 12px; background: #DCEAF3; font-size: 13px; }
.score b { display: block; font-family: 'Fraunces', serif; font-size: 17px; }
div.stButton > button[kind="primary"] { background: #1E5A6E; border: 0; color: #F7FBFD; border-radius: 12px; padding: .7rem; font-weight: 700; }
div.stButton > button[kind="primary"]:hover { background: #164A5B; }
div.stButton > button[kind="secondary"] { border-radius: 99px; border: 1px solid #B7D4E6; background: transparent; color: #0D2B45; }
/* sidebar navigation */
[data-testid="stSidebar"] div.stButton > button { justify-content: flex-start !important; text-align: left !important; border: 0; border-radius: 12px;
  padding: .62rem .9rem; font-weight: 600; background: transparent; color: #B7D4E6; }
[data-testid="stSidebar"] div.stButton > button > div { width: 100%; justify-content: flex-start !important; text-align: left !important; }
[data-testid="stSidebar"] div.stButton > button p { color: inherit; font-size: 15px; text-align: left !important; width: 100%; }
[data-testid="stSidebar"] div.stButton > button:hover { background: rgba(183,212,230,.13); color: #FFFFFF; }
[data-testid="stSidebar"] div.stButton > button[kind="primary"] { background: #1E5A6E; color: #FFFFFF; box-shadow: inset 3px 0 0 #DCC8AA; }
[data-testid="stSidebar"] div.stButton { margin-bottom: -6px; }
.sbnote { position: fixed; left: 16px; bottom: 16px; width: min(18.5rem, calc(100vw - 2rem)); z-index: 5; padding: 14px; border-radius: 14px; background: #163A56; border: 1px solid rgba(183,212,230,.15); font-size: 13px; line-height: 1.5; color: #B7D4E6; }
/* home */
[data-testid="stVerticalBlockBorderWrapper"]:has(.hero-marker) { background: #DCEAF3; }
.greet { font-size: 15px; font-weight: 600; color: #1E5A6E; margin-bottom: 4px; }
.herot { font-family: 'Fraunces', serif; font-size: 32px; font-weight: 700; line-height: 1.15; margin-bottom: 6px; }
.card.sky { background: #DCEAF3; border-color: #B7D4E6; }
.card.sand { background: #F4EBDD; border-color: #DCC8AA; }
.card.sky p.body { font-size: 15px; line-height: 1.7; margin: 0; color: #0D2B45; }
.check { display: flex; gap: 10px; font-size: 15px; margin-bottom: 9px; }
.check b { color: #2C7A72; }
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Form definition (values match what predict_churn expects)
# ----------------------------------------------------------------------------
YES_NO = ["Yes", "No"]
NO_YES = ["No", "Yes"]
ADDONS = ["security", "backup", "device", "tech", "tv", "movies"]

# form key -> column name used by the model
KEYMAP = {
    "gender": "gender", "senior": "SeniorCitizen", "partner": "Partner", "dependents": "Dependents",
    "tenure": "tenure", "phone": "PhoneService", "lines": "MultipleLines", "internet": "InternetService",
    "security": "OnlineSecurity", "backup": "OnlineBackup", "device": "DeviceProtection",
    "tech": "TechSupport", "tv": "StreamingTV", "movies": "StreamingMovies", "contract": "Contract",
    "paperless": "PaperlessBilling", "payment": "PaymentMethod", "monthly": "MonthlyCharges",
    "total": "TotalCharges",
}
DEFAULTS = dict(
    gender="Female", senior=0, partner="Yes", dependents="No", tenure=12, phone="Yes", lines="No",
    internet="Fiber optic", security="No", backup="No", device="No", tech="No", tv="No", movies="No",
    contract="Month-to-month", paperless="Yes", payment="Electronic check", monthly=70.0, total=840.0,
)
EXAMPLES = {
    "leave": dict(DEFAULTS, tenure=3, monthly=85.0, total=255.0),
    "stay": dict(
        DEFAULTS, gender="Male", dependents="Yes", tenure=58, lines="Yes", internet="DSL", security="Yes",
        backup="Yes", device="Yes", tech="Yes", contract="Two year", paperless="No",
        payment="Credit card (automatic)", monthly=68.0, total=3944.0,
    ),
}


def normalize():
    """Keep dependent fields valid: no internet -> add-ons are 'No internet service', no phone -> 'No phone service'."""
    s = st.session_state
    if s.internet == "No":
        for k in ADDONS:
            s[k] = "No internet service"
    else:
        for k in ADDONS:
            if s[k] == "No internet service":
                s[k] = "No"
    if s.phone == "No":
        s.lines = "No phone service"
    elif s.lines == "No phone service":
        s.lines = "No"


def run_prediction():
    normalize()
    snap = {k: st.session_state[k] for k in KEYMAP}
    customer_data = {KEYMAP[k]: v for k, v in snap.items()}
    try:
        result = predict_churn(customer_data)
        prob = max(0.0, min(100.0, float(result["churn_probability"])))
        leave = result["churn_prediction"] == "Yes"
        st.session_state.result = dict(leave=leave, prob=prob, snap=snap)
        st.session_state.error = None
        item = dict(time=datetime.now().strftime("%H:%M"), contract=snap["contract"], tenure=snap["tenure"],
                    monthly=snap["monthly"], prob=prob, leave=leave)
        st.session_state.history = ([item] + st.session_state.history)[:6]
    except Exception as error:
        st.session_state.error = str(error)


def tips(d, leave):
    if not leave:
        t = ["No urgent action. Keep the service quality steady."]
        if d["contract"] == "Month-to-month":
            t.append("A 12-month plan could make this customer even more loyal.")
        return t
    t = []
    if d["contract"] == "Month-to-month":
        t.append("Offer a 12-month plan with a loyalty discount.")
    if d["payment"] == "Electronic check":
        t.append("Move them to automatic payment with a small bill credit.")
    if d["internet"] != "No" and (d["security"] == "No" or d["tech"] == "No"):
        t.append("Offer a free trial of online security or tech support.")
    if d["internet"] == "Fiber optic" and d["monthly"] > 80:
        t.append("Review their plan price against what they actually use.")
    if d["tenure"] <= 12:
        t.append("Schedule a friendly check-in call within the first year.")
    return (t or ["Reach out personally and ask what would make them stay."])[:4]


# ----------------------------------------------------------------------------
# HTML helpers
# ----------------------------------------------------------------------------
def card(title, body, sub="", tint=False, cls=""):
    s = f"<p class='kl' style='margin-bottom:14px'>{sub}</p>" if sub else ""
    return f"<div class='card{' t' if tint else ''} {cls}'><h3>{title}</h3>{s}{body}</div>"


def bars(items, cls="", max_value=100.0):
    return "".join(
        f"<div class='bw {cls}'><div class='h'><span>{l}</span><b>{v}%</b></div>"
        f"<div class='bt'><i style='width:{min(100, v / max_value * 100):.0f}%'></i></div></div>"
        for l, v in items
    )


def ul(items):
    return "<ul style='margin:0;padding-left:20px;font-size:14px'>" + "".join(
        f"<li style='margin-bottom:6px'>{i}</li>" for i in items) + "</ul>"


# ----------------------------------------------------------------------------
# State and sidebar
# ----------------------------------------------------------------------------
PAGES = ["Home", "Predict churn", "How it works"]
NAV_ICONS = {"Home": "🏠", "Predict churn": "📈", "How it works": "ℹ️"}
st.session_state.setdefault("page", "Home")


def set_page(name):
    st.session_state.page = name


with st.sidebar:
    st.markdown(
        "<div style='display:flex;align-items:center;gap:12px;padding:0 4px 18px;margin-bottom:10px;border-bottom:1px solid rgba(183,212,230,.18)'>"
        "<svg width='40' height='40' viewBox='0 0 34 34'><rect width='34' height='34' rx='10' fill='#1E5A6E'/>"
        "<path d='M6 19 Q11 12 17 19 T28 19' fill='none' stroke='#DCC8AA' stroke-width='2.6' stroke-linecap='round'/>"
        "<path d='M6 25 Q11 18 17 25 T28 25' fill='none' stroke='#6BA7A0' stroke-width='2.6' stroke-linecap='round'/></svg>"
        "<div><div style='font-family:Fraunces,serif;font-weight:700;font-size:20px;line-height:1.1;color:#fff'>Churn Predictor</div>"
        "<div style='font-size:12px;color:#B7D4E6'>Telecom customers</div></div></div>",
        unsafe_allow_html=True,
    )
    for p in PAGES:
        st.button(f"{NAV_ICONS[p]}  {p}", key=f"nav_{p}", on_click=set_page, args=(p,), use_container_width=True,
                  type="primary" if st.session_state.page == p else "secondary")
    st.markdown("<div class='sbnote'>💡 <b>Good to know</b><br>This model provides an estimate, not a guarantee.</div>",
                unsafe_allow_html=True)
page = st.session_state.page

for k, v in DEFAULTS.items():
    st.session_state.setdefault(k, v)
    st.session_state[k] = st.session_state[k]  # keep values when switching pages
for k, v in dict(total_touched=False, result=None, error=None, history=[]).items():
    st.session_state.setdefault(k, v)
    st.session_state[k] = st.session_state[k]


def go_predict():
    st.session_state.page = "Predict churn"


# ----------------------------------------------------------------------------
# Page: Home
# ----------------------------------------------------------------------------
if page == "Home":
    with st.container(border=True):
        t, btn = st.columns([3, 1], vertical_alignment="center")
        t.markdown(
            "<span class='hero-marker'></span><div class='greet'>Hello 👋 Welcome back</div>"
            "<div class='herot'>Ready to predict customer churn?</div>"
            "<p class='kl'>Enter a customer’s details and see whether they may stay or leave the company.</p>",
            unsafe_allow_html=True)
        btn.button("Start predicting", type="primary", on_click=go_predict, use_container_width=True)

    hist = st.session_state.history
    n = len(hist)
    leaving = sum(1 for h in hist if h["leave"])
    avg = f"{sum(h['prob'] for h in hist) / n:.0f}%" if n else "–"
    k1, k2, k3 = st.columns(3)
    k1.markdown(f"<div class='card t'><p class='kl'>Predictions this session</p><div class='kpi'>{n}</div></div>", unsafe_allow_html=True)
    k2.markdown(f"<div class='card'><p class='kl'>May leave</p><div class='kpi'>{leaving}</div></div>", unsafe_allow_html=True)
    k3.markdown(f"<div class='card'><p class='kl'>Average churn probability</p><div class='kpi'>{avg}</div></div>", unsafe_allow_html=True)

    st.markdown(card(
        "💙 Key Features",
        "<div style='display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:2px 28px'>"
        + "".join(f"<div class='check'><b>✓</b><span>{x}</span></div>" for x in [
            "Interactive and easy to use", "Based on real customer data",
            "Built with Machine Learning", "Simple and clean design"])
        + "</div>",
        cls="sand"), unsafe_allow_html=True)

    a, b = st.columns(2)
    a.markdown(card(
        "Churn at a glance",
        bars([("Month-to-month contract", 42.7), ("One-year contract", 11.3), ("Two-year contract", 2.8),
              ("Fiber optic internet", 41.9), ("DSL internet", 19.0), ("No internet", 7.4)], "up", 50),
        "Typical figures from the public Telco churn dataset. Your own data may differ."), unsafe_allow_html=True)
    if hist:
        rows = "".join(
            f"<div class='row'><span>{h['contract']}<small>{h['tenure']} months · ${h['monthly']:.0f}/mo · {h['time']}</small></span>"
            f"<b style='color:{'#9A6B2C' if h['leave'] else '#2C7A72'}'>{h['prob']:.0f}%</b></div>" for h in hist)
        b.markdown(card("Recent predictions", rows, "Newest first."), unsafe_allow_html=True)
    else:
        b.markdown(card("Recent predictions", "<p class='kl'>Nothing yet. Your predictions will show up here.</p>"), unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Page: Predict
# ----------------------------------------------------------------------------
elif page == "Predict churn":
    st.title("Predict customer churn")
    st.info("This model provides an estimate, not a guarantee.")

    def sync_total():
        if not st.session_state.total_touched:
            st.session_state.total = round(st.session_state.tenure * st.session_state.monthly, 2)

    def touch_total():
        st.session_state.total_touched = True

    def load_example(name):
        for k, v in EXAMPLES[name].items():
            st.session_state[k] = v
        st.session_state.total_touched = True
        run_prediction()

    normalize()
    no_net = st.session_state.internet == "No"
    no_phone = st.session_state.phone == "No"

    form, result = st.columns([7, 5], gap="large")

    with form:
        with st.container(border=True):
            st.subheader("Customer Information")
            st.caption("Fill in the details below to get a churn prediction.")
            c1, c2 = st.columns(2)
            with c1:
                st.selectbox("Gender", ["Female", "Male"], key="gender")
                st.selectbox("Senior Citizen", [0, 1], key="senior", format_func=lambda x: "Yes" if x else "No")
                st.selectbox("Has Partner?", YES_NO, key="partner")
                st.selectbox("Has Dependents?", YES_NO, key="dependents")
                st.number_input("Tenure (months)", min_value=0, max_value=100, step=1, key="tenure", on_change=sync_total)
                st.selectbox("Phone Service", YES_NO, key="phone")
                st.selectbox("Multiple Lines", ["No phone service"] if no_phone else NO_YES, key="lines", disabled=no_phone)
                st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], key="internet")
                st.selectbox("Online Security", ["No internet service"] if no_net else YES_NO, key="security", disabled=no_net)
                st.selectbox("Online Backup", ["No internet service"] if no_net else YES_NO, key="backup", disabled=no_net)
            with c2:
                st.selectbox("Device Protection", ["No internet service"] if no_net else YES_NO, key="device", disabled=no_net)
                st.selectbox("Tech Support", ["No internet service"] if no_net else YES_NO, key="tech", disabled=no_net)
                st.selectbox("Streaming TV", ["No internet service"] if no_net else YES_NO, key="tv", disabled=no_net)
                st.selectbox("Streaming Movies", ["No internet service"] if no_net else YES_NO, key="movies", disabled=no_net)
                st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], key="contract")
                st.selectbox("Paperless Billing", YES_NO, key="paperless")
                st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)",
                                                "Credit card (automatic)"], key="payment")
                st.number_input("Monthly Charges ($)", min_value=0.0, step=0.05, format="%.2f", key="monthly", on_change=sync_total)
                st.number_input("Total Charges ($)", min_value=0.0, step=0.05, format="%.2f", key="total", on_change=touch_total)

            if st.button("Predict Churn", type="primary", use_container_width=True):
                run_prediction()
            e1, e2, e3 = st.columns([2, 2, 2], vertical_alignment="center")
            e1.markdown("<span class='kl'>Try an example:</span>", unsafe_allow_html=True)
            e2.button("Likely to leave", on_click=load_example, args=("leave",), use_container_width=True)
            e3.button("Likely to stay", on_click=load_example, args=("stay",), use_container_width=True)

    with result:
        r = st.session_state.result
        if st.session_state.error:
            st.error(f"Prediction failed: {st.session_state.error}")
        if r is None:
            st.markdown(
                "<div class='card t'><h3>Prediction Result</h3><div class='hero' style='margin-top:12px'>"
                "<div class='gauge' style='--p:0'><span>–</span></div>"
                "<div><p class='kl'>Estimated churn probability</p><span class='pill idle'>Waiting for prediction</span></div></div></div>",
                unsafe_allow_html=True)
        else:
            p, leave = r["prob"], r["leave"]
            band = "Low" if p < 30 else "Moderate" if p < 60 else "High"
            stale = ""
            if r["snap"] != {k: st.session_state[k] for k in KEYMAP}:
                stale = "<p style='color:#9A6B2C;font-weight:600;font-size:13px;margin:12px 0 0'>Details changed. Press Predict Churn to update.</p>"
            st.markdown(
                f"<div class='card t'><h3>Prediction Result</h3><div class='hero' style='margin-top:12px'>"
                f"<div class='gauge' style='--p:{p:.0f}'><span>{p:.0f}%</span></div>"
                f"<div><p class='kl'>Estimated churn probability</p>"
                f"<span class='pill {'leave' if leave else 'stay'}'>{'⚠️ Customer may leave' if leave else '✅ Customer may stay'}</span>"
                f"<p class='kl' style='margin-top:10px'>Risk level: <b>{band}</b></p></div></div>{stale}"
                f"<p class='kl' style='margin-top:14px;font-size:12px'>Probability is the model’s estimate and should not be treated as a certainty.</p></div>",
                unsafe_allow_html=True)
            st.markdown(card("Ideas to keep this customer" if leave else "Keep it that way",
                             ul(tips(r["snap"], leave)), "General tips based on the details you entered."),
                        unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Page: How it works
# ----------------------------------------------------------------------------
else:
    st.title("How it works")
    st.caption("From customer details to a churn prediction in four steps.")

    def step(n, title, text):
        return f"<div class='card step'><div class='n'>{n}</div><div><h3>{title}</h3><p>{text}</p></div></div>"

    a, b = st.columns(2)
    a.markdown(step(1, "Enter customer details", "Fill in 19 details about the customer: who they are, which services they use and how they pay."), unsafe_allow_html=True)
    b.markdown(step(2, "The model scores the customer", "The details are sent to the trained churn model, which compares them with patterns it learned from past customers."), unsafe_allow_html=True)
    a.markdown(step(3, "Read the result", "You get a verdict (may leave or may stay) and an estimated churn probability."), unsafe_allow_html=True)
    b.markdown(step(4, "Act on it", "For customers who may leave, use the ideas shown next to the result to reach out before they go."), unsafe_allow_html=True)

    a, b = st.columns(2)
    a.markdown(card("What the model looks at", ul([
        "<b>About the customer:</b> gender, senior citizen, partner, dependents",
        "<b>Services:</b> phone, multiple lines, internet, security, backup, device protection, tech support, streaming",
        "<b>Account and billing:</b> tenure, contract, paperless billing, payment method, monthly and total charges"]),
        "Nineteen details in three groups."), unsafe_allow_html=True)
    b.markdown(card("Good to know", ul([
        "With no internet service, the add-on services are set automatically.",
        "With no phone service, Multiple Lines is set automatically.",
        "Total charges fill in from tenure and monthly charges until you type your own.",
        "The model gives an estimate, not a guarantee."])), unsafe_allow_html=True)

    st.markdown(card("How to read the probability",
        "<div class='score'><div><b>Under 30%</b>Low risk</div><div><b>30% to 59%</b>Moderate risk</div>"
        "<div><b>60% and up</b>High risk</div></div>"
        "<p class='kl' style='margin-top:14px;font-size:12px'>The verdict (may leave or may stay) comes straight from the model. "
        "The risk level is only a simple label for the probability.</p>"), unsafe_allow_html=True)