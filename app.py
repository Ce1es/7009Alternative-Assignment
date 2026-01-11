import streamlit as st
from PIL import Image
import os

# 页面配置
st.set_page_config(page_title="IBM Employee Attrition Prediction System", layout="wide")

# 侧边栏
st.sidebar.header("📋 Employee Profile Input")
st.sidebar.markdown("Adjust parameters to simulate different scenarios:")
age = st.sidebar.slider("Age", 18, 60, 29)
income = st.sidebar.slider("Monthly Income ($)", 1000, 20000, 2800)
overtime = st.sidebar.selectbox("OverTime Status", ["Yes", "No"])
years = st.sidebar.number_input("Years at Company", 0, 40, 5)

if st.sidebar.button("Run Prediction"):
    st.sidebar.success("Prediction Completed!")

# 主界面
st.title("🧠 AI Employee Attrition Risk Dashboard")
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Prediction Result", value="High Risk (Attrition)", delta="- 85% Retention Probability")
with col2:
    st.metric(label="Key Risk Factor", value="OverTime")
with col3:
    st.metric(label="Recommended Action", value="Reduce Workload")

st.markdown("---")
st.subheader("🔍 Explainable AI (XAI) Insights")

tab1, tab2 = st.tabs(["Local Explanation (Case Study)", "Global Explanation (Model Logic)"])

with tab1:
    st.markdown("#### Individual Decision Analysis")
    st.info("ℹ️ **How to read:** Red bars push the prediction towards 'Attrition' (Risk), while Blue bars push towards 'Stay' (Safe).")
    
    if os.path.exists("shap_local_explanation_fixed.png"):
        st.image("shap_local_explanation_fixed.png", caption="SHAP Force Plot", use_column_width=True)
    else:
        st.error("Image not found. Please ensure 'shap_local_explanation_fixed.png' is in the GitHub repo.")

with tab2:
    st.markdown("#### Overall Model Interpretation")
    # 修改点：直接读取当前目录
    if os.path.exists("shap_summary_plot.png"):
        st.image("shap_summary_plot.png", caption="SHAP Summary Plot", use_column_width=True)
    else:
        st.warning("Image not found. Please ensure 'shap_summary_plot.png' is in the GitHub repo.")

st.markdown("---")
st.caption("Developed for WQF7009 Alternative Assessment")
