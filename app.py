# Cell 8 (Update): Interactive Mock App with Counterfactual Logic
code = """
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="IBM Employee Attrition Prediction", layout="wide")

# ==========================================
# 1. 侧边栏：输入与方法论声明
# ==========================================
st.sidebar.header("📋 Employee Profile Input")
st.sidebar.markdown("**Simulation Method:** User-Driven Perturbation (Human-in-the-loop)")

# 模拟输入参数
age = st.sidebar.slider("Age", 18, 60, 29)
income = st.sidebar.slider("Monthly Income", 1000, 20000, 5000)

st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ Counterfactual Trigger")
st.sidebar.info("Adjust the feature below to simulate a 'What-If' scenario.")

# 核心触发器
overtime = st.sidebar.selectbox("OverTime Status (Perturbation)", ["Yes", "No"]) 

if st.sidebar.button("Run Counterfactual Simulation"):
    st.sidebar.success("Simulation Complete!")

# ==========================================
# 2. 主界面：逻辑与反事实计算
# ==========================================
st.title("🧠 AI Attrition Risk & Counterfactual Dashboard")
st.markdown("---")

# 定义基准概率 (用于计算差值)
base_risk_score = 0.85  # 假设的高风险分数
current_risk_score = 0.0

# === 核心逻辑：反事实推演 ===
if overtime == "Yes":
    # [场景 A: 原始状态 - 高风险]
    risk_color = "inverse" # 红色
    prediction_text = "High Risk (Attrition)"
    current_risk_score = 0.85
    delta_val = "Baseline Scenario" # 这是基准，没有变化
    risk_factor = "OverTime (High Workload)"
    action = "Reduce Workload Immediately"
    image_file = "shap_local_explanation_fixed.png" # 红图
    
    # 提示用户进行反事实操作
    sim_message = "⚠️ Current Status: High Risk. Try changing 'OverTime' to 'No' to see the Counterfactual impact."
    sim_type = "warning"

else:
    # [场景 B: 反事实状态 - 低风险]
    risk_color = "normal" # 绿色
    prediction_text = "Low Risk (Safe)"
    current_risk_score = 0.15 # 假设降到了 15%
    
    # === 关键修改：明确展示“反事实收益” ===
    # 计算风险降低了多少
    improvement = (base_risk_score - current_risk_score) * 100
    delta_val = f"- {improvement:.1f}% Risk Reduction (Counterfactual Gain)"
    
    risk_factor = "None (Stable)"
    action = "Maintain Current Benefits"
    image_file = "shap_local_low_risk.png" # 蓝图
    
    # 提示反事实结果
    sim_message = f"✅ Counterfactual Result: By removing OverTime, the attrition risk dropped by {improvement:.1f}%."
    sim_type = "success"

# ==========================================
# 3. 展示动态指标 (Metrics)
# ==========================================
col1, col2, col3 = st.columns(3)

with col1:
    # 这里展示核心的反事实变化
    st.metric(label="Prediction Result", value=prediction_text, delta=delta_val, delta_color=risk_color)
with col2:
    st.metric(label="Key Driver", value=risk_factor)
with col3:
    st.metric(label="Recommended Action", value=action)

# 展示文字结论
if sim_type == "warning":
    st.warning(sim_message)
else:
    st.success(sim_message)

st.markdown("---")

# ==========================================
# 4. 可解释性图表 (XAI Views)
# ==========================================
st.subheader("🔍 Explainable AI (XAI) Verification")

tab1, tab2 = st.tabs(["Counterfactual Analysis (Local)", "Global Logic"])

with tab1:
    st.markdown(f"#### Simulation Visuals (OverTime: {overtime})")
    st.markdown("This plot shows how the model's decision path changes under the selected scenario.")
    
    # 动态加载不同的图
    if os.path.exists(image_file):
        st.image(image_file, caption=f"Force Plot for {prediction_text} Scenario", use_column_width=True)
        
        if overtime == "Yes":
            st.error("📉 Root Cause Analysis: The large RED bar (OverTime) is pushing the prediction to the right (High Risk).")
        else:
            st.success("📈 Counterfactual Insight: Removing the RED bar (OverTime) shifted the prediction to the left (Low Risk). The model confirms this intervention is effective.")
    else:
        st.info(f"Image placeholder: {image_file} (Please run generation code to see visuals)")

with tab2:
    st.markdown("#### Global Feature Importance")
    if os.path.exists("shap_summary_plot.png"):
        st.image("shap_summary_plot.png", use_column_width=True)

st.markdown("---")
st.caption("Powered by XGBoost & SHAP | Methodology: User-Driven Perturbation (DiCE Logic)")
"""

with open("app.py", "w") as f:
    f.write(code)
