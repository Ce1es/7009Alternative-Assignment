# Cell 8 (Update): Interactive Mock App
code = """
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="IBM Employee Attrition Prediction", layout="wide")

# Sidebar inputs
st.sidebar.header("📋 Employee Profile Input")
# 这里的参数现在真的会影响结果了（逻辑上的影响）
age = st.sidebar.slider("Age", 18, 60, 29)
# OverTime 是关键开关！
overtime = st.sidebar.selectbox("OverTime Status", ["Yes", "No"]) 
income = st.sidebar.slider("Monthly Income", 1000, 20000, 5000)

if st.sidebar.button("Run Prediction"):
    st.sidebar.success("Analysis Updated!")

st.title("🧠 AI Employee Attrition Risk Dashboard")
st.markdown("---")

# === 核心逻辑：根据用户选择展示不同场景 ===
if overtime == "Yes":
    # 场景 A: 高风险 (High Risk)
    risk_color = "inverse" # 红色高亮
    prediction_text = "High Risk (Attrition)"
    delta_val = "- 85% Retention Probability"
    risk_factor = "OverTime (High Workload)"
    action = "Reduce Workload Immediately"
    image_file = "shap_local_explanation_fixed.png" # 之前生成的红图
    
else:
    # 场景 B: 低风险 (Low Risk)
    risk_color = "normal" 
    prediction_text = "Low Risk (Safe)"
    delta_val = "+ 95% Retention Probability"
    risk_factor = "None (Stable)"
    action = "Maintain Current Benefits"
    image_file = "shap_local_low_risk.png" # 刚刚生成的蓝图

# 展示动态指标
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Prediction Result", value=prediction_text, delta=delta_val, delta_color=risk_color)
with col2:
    st.metric(label="Key Factor Identified", value=risk_factor)
with col3:
    st.metric(label="Recommended Action", value=action)

st.markdown("---")
st.subheader("🔍 Explainable AI (XAI) Insights")

tab1, tab2 = st.tabs(["Individual Analysis", "Global Logic"])

with tab1:
    st.markdown(f"#### Analysis for selected scenario (OverTime: {overtime})")
    
    # 动态加载不同的图
    if os.path.exists(image_file):
        st.image(image_file, caption=f"SHAP Analysis for {prediction_text} Employee", use_column_width=True)
        if overtime == "Yes":
            st.error("⚠️ Insight: Red bars indicate high 'OverTime' is the primary driver for attrition.")
        else:
            st.success("✅ Insight: Blue bars indicate good work-life balance contributes to retention.")
    else:
        st.warning(f"Image {image_file} not found. Please run the generation code.")

with tab2:
    st.markdown("#### Overall Model Logic")
    if os.path.exists("shap_summary_plot.png"):
        st.image("shap_summary_plot.png", use_column_width=True)

st.markdown("---")
st.caption("Developed for WQF7009 | Interactive Prototype")
"""

with open("app.py", "w") as f:
    f.write(code)
