import streamlit as st
from levels import load_toggle_switch
from level2_feedback import run_level2_feedback
from toggle_demo import simulate_toggle
from utils import plot_simulation

# ---------- Streamlit Page Config ----------
st.set_page_config(page_title="BioFSM", layout="centered")

# ---------- Level Selector ----------
st.sidebar.title("🧬 BioFSM Levels")
level = st.sidebar.selectbox("Select Level", [
    "Level 1: Toggle Switch",
    "Level 2: Feedback Frenzy"
])

# ---------- LEVEL 1 ----------
if level == "Level 1: Toggle Switch":
    st.title("BioFSM: Toggle Switch Simulator")
    st.markdown("Level 1: Toggle Switch - Simulate simple ON/OFF logic using IPTG and aTc")

    if "fsm" not in st.session_state:
        st.session_state.fsm = load_toggle_switch()
    if "run_sim" not in st.session_state:
        st.session_state.run_sim = False

    fsm = st.session_state.fsm

    # Display current state info
    state_info = fsm.get_state_info()
    st.subheader(f"Current State: {state_info['state']}")
    st.markdown(f"**Output:** {state_info['output']}")
    st.markdown(f"*{state_info['description']}*")

    # FSM control buttons
    st.divider()
    st.markdown("### Apply Input Signal")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Apply IPTG"):
            fsm.transition("IPTG")
            st.session_state.run_sim = False
    with col2:
        if st.button("Apply aTc"):
            fsm.transition("aTc")
            st.session_state.run_sim = False
    with col3:
        if st.button("Reset"):
            fsm.reset()
            st.session_state.run_sim = False
    with col4:
        if st.button("▶️ Run Simulation"):
            st.session_state.run_sim = True

    # Transition History
    st.divider()
    st.markdown("### Transition History")
    if fsm.history:
        for h in fsm.history:
            st.markdown(f"**{h[0]}** + '{h[1]}' → **{h[2]}**")
    else:
        st.markdown("No inputs applied yet.")

    # Simulation plot (only after Run Simulation pressed)
    if st.session_state.run_sim:
        st.divider()
        st.markdown("### 🧪 Tellurium Simulation Plot")
        try:
            result = simulate_toggle(fsm.current_state.name)
            img_buf = plot_simulation(result)
            st.image(img_buf, caption="GFP expression over time (Simulated)", use_container_width=True)
        except Exception as e:
            st.error(f"Simulation failed: {e}")

    # Unlock Level 2
    if state_info['output'] == "GFP ON":
        st.session_state.Level2_Unlocked = True

    # Restart Level
    st.divider()
    if st.button("🔄 Restart Level"):
        st.session_state.fsm = load_toggle_switch()
        st.session_state.run_sim = False

# ---------- LEVEL 2 ----------
elif level == "Level 2: Feedback Frenzy":
    if st.session_state.get("Level2_Unlocked"):
        run_level2_feedback()
    else:
        st.warning("🔒 Complete Level 1 (GFP ON) to unlock Level 2")
        st.stop()
