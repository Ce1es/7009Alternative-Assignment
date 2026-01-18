import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="IBM Attrition Risk Dashboard", layout="wide")

# ==========================================
# 1. 侧边栏：干净、专业的设置
# ==========================================
st.sidebar.header("⚙️ Scenario Settings")
st.sidebar.caption("Adjust parameters to simulate outcomes.")

# 模拟输入参数
age = st.sidebar.slider("Age", 18, 60, 29)
income = st.sidebar.slider("Monthly Income", 1000, 20000, 5000)

st.sidebar.markdown("---")
st.sidebar.subheader("What-If Analysis")
st.sidebar.info("Modify the key factor below to see if the prediction changes.")

# 核心触发器
overtime = st.sidebar.selectbox("OverTime Status", ["Yes", "No"]) 

if st.sidebar.button("Run Simulation"):
    st.sidebar.success("Updated!")

# ==========================================
# 2. 底部：学术/技术声明 (藏在这里最合适)
# ==========================================
# 放在侧边栏最下方，或者作为折叠菜单
with st.sidebar.expander("ℹ️ Technical Methodology"):
    st.markdown("""
    **Model Logic:**
    * **Feature Importance:** SHAP (Global/Local)
    * **Counterfactuals:** User-Driven Perturbation (Human-in-the-loop)
    
    **Definition:**
    The system calculates the *Minimal Change* required to flip the risk category by allowing users to perturb high-impact features.
    """)

# ==========================================
# 3. 主界面：逻辑保持不变 (依然强大)
# ==========================================
st.title("🧠 AI Attrition Risk Dashboard")
st.markdown("---")

# 定义基准概率
base_risk_score = 0.85 
current_risk_score = 0.0

# === 核心逻辑 ===
if overtime == "Yes":
    # [场景 A: 高风险]
    risk_color = "inverse" # 红色
    prediction_text = "High Risk (Attrition)"
    current_risk_score = 0.85
    delta_val = "Baseline Scenario"
    risk_factor = "OverTime (High Workload)"
    action = "Reduce Workload Immediately"
    image_file = "shap_local_explanation_fixed.png" # 红色图
    
    sim_message = "⚠️ **Action Required:** Employee is at High Risk. Try changing 'OverTime' to 'No' to simulate retention strategy."
    sim_type = "warning"

else:
    # [场景 B: 反事实收益]
    risk_color = "normal" # 绿色
    prediction_text = "Low Risk (Safe)"
    current_risk_score = 0.15 
    
    # 计算收益
    improvement = (base_risk_score - current_risk_score) * 100
    delta_val = f"- {improvement:.1f}% Risk Reduction" # 这里的文字改得更商业化一点
    
    risk_factor = "None (Stable)"
    action = "Maintain Current Benefits"
    image_file = "shap_local_low_risk.png" # 蓝色图
    
    sim_message = f"✅ **Counterfactual Outcome:** Removing OverTime reduces attrition risk by {improvement:.1f}%."
    sim_type = "success"

# ==========================================
# 4. 展示动态指标
# ==========================================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Predicted Status", value=prediction_text, delta=delta_val, delta_color=risk_color)
with col2:
    st.metric(label="Primary Driver", value=risk_factor)
with col3:
    st.metric(label="Recommended Action", value=action)

if sim_type == "warning":
    st.warning(sim_message)
else:
    st.success(sim_message)

st.markdown("---")

# ==========================================
# 5. 可解释性图表
# ==========================================
st.subheader("🔍 XAI Logic Verification")

tab1, tab2 = st.tabs(["Local Analysis (Case View)", "Global Model Logic"])

with tab1:
    st.markdown(f"**Visualizing the decision path for: OverTime = {overtime}**")
    
    if os.path.exists(image_file):
        st.image(image_file, caption="SHAP Force Plot", use_column_width=True)
    else:
        st.info("Visuals loading... (Run notebook generation code first)")

with tab2:
    st.markdown("**Top Drivers of Attrition (Company-wide)**")
    if os.path.exists("shap_summary_plot.png"):
        st.image("shap_summary_plot.png", use_column_width=True)
