import streamlit as st
import random

def run_level2_feedback():
    st.set_page_config(page_title="BioFSM Level 2", layout="centered")

    st.markdown("""
        <style>
        body { background-color: #0f0f0f; color: #f0f0f0; }
        .stButton>button { background-color: #222; color: white; border: 1px solid #555; }
        .stAlert { border-radius: 0.5em; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🧬 Level 2: Feedback Frenzy")

    # ----- Sidebar Hints & How to Win -----
    with st.sidebar:
        st.markdown("## 📘 How to Win")
        st.markdown("""
        - Survive **10+ turns**.
        - Output must be `ON` in **≥ 4 turns**.
        - Inputs:
          - 🧴 IPTG disables LacI
          - 💬 AHL activates TetR (if LacI is OFF)
          - 🔁 aTc resets system
        - Mutations & feedback appear randomly.
        """)

        st.markdown("## 🧠 Hints")
        if st.checkbox("Show Strategic Hints", value=False):
            circuit = st.session_state.get("Level2_Circuit", {})
            inputs = st.session_state.get("Level2_Inputs", {})
            if circuit.get("LacI") == "ON" and not inputs.get("IPTG"):
                st.info("🧴 Use IPTG to disable LacI.")
            elif circuit.get("LacI") == "OFF" and not inputs.get("AHL"):
                st.info("💬 LacI is off — use AHL to trigger TetR.")
            elif circuit.get("TetR") == "ON" and circuit.get("Output") == "ON":
                st.info("💡 Output is ON — now protect it!")
            elif inputs.get("aTc"):
                st.info("🔁 aTc resets all — useful in danger.")

    # ----- State Setup -----
    defaults = {
        "Level2_Circuit": {"LacI": "ON", "TetR": "OFF", "Output": "OFF", "Feedback": False, "CI": "OFF"},
        "Level2_Turn": 1,
        "Level2_Inputs": {"IPTG": False, "AHL": False, "aTc": False},
        "Level2_Mutations": [],
        "Level2_OutputStreak": 0,
        "Level2_OutputONCount": 0,
        "Level2_Won": False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    turn = st.session_state.Level2_Turn if isinstance(st.session_state.Level2_Turn, int) else 0
    circuit = st.session_state.Level2_Circuit
    if "CI" not in circuit:
        circuit["CI"] = "OFF"
    inputs = st.session_state.Level2_Inputs

    st.subheader(f"🌒 Turn `{turn if not st.session_state.Level2_Won else '🏁'}`")

    # Display current circuit state
    st.markdown(f"""
    **⚙️ Circuit State:**  
    - 🧬 LacI: `{circuit['LacI']}`  
    - 🧪 CI (Inhibitor): `{circuit['CI']}`  
    - 🦠 TetR: `{circuit['TetR']}`  
    - 💡 Output: `{circuit['Output']}`  
    - ☢️ Feedback: `{"ON ⚠️" if circuit['Feedback'] else "OFF ✅"}`
    """)

    # ----- Input Panel -----
    st.markdown("### 🧪 Input Panel")
    col1, col2, col3 = st.columns(3)
    if col1.button("🧴 Apply IPTG"):
        inputs["IPTG"] = True
    if col2.button("💬 Add AHL"):
        inputs["AHL"] = True
    if col3.button("🔁 Apply aTc (Reset)"):
        inputs["aTc"] = True

    # ----- Random Mutation (20% chance) -----
    if not st.session_state.Level2_Won and random.random() < 0.15:
        mutated = random.choice(["LacI", "TetR", "Feedback", "CI"])
        st.session_state.Level2_Mutations.append((turn, mutated))
        if mutated == "LacI":
            circuit["LacI"] = "OFF"
        elif mutated == "TetR":
            circuit["TetR"] = "ON"
        elif mutated == "CI":
            circuit["CI"] = "ON"
        elif mutated == "Feedback":
            circuit["Feedback"] = not circuit["Feedback"]
        st.error(f"☣️ Mutation triggered: `{mutated}` flipped!")

    # ----- Apply Input Logic -----
    if inputs["IPTG"]:
        circuit["LacI"] = "OFF"
        if circuit["TetR"] == "ON" and random.random() < 0.1:
            circuit["CI"] = "ON"
            st.warning("⚠️ CI inhibitor triggered unexpectedly!")

    if inputs["AHL"] and circuit["LacI"] == "OFF" and circuit["CI"] == "OFF":
        circuit["TetR"] = "ON"
    if circuit["TetR"] == "ON" and circuit["CI"] == "OFF":
        circuit["Output"] = "ON"
    if inputs["aTc"]:
        circuit["LacI"] = "ON"
        circuit["TetR"] = "OFF"
        circuit["Output"] = "OFF"
        circuit["CI"] = "OFF"
        circuit["Feedback"] = False
        st.warning("🔁 System reset — all core components cleared.")


    # ----- Feedback Check -----
    if circuit["Feedback"] and circuit["Output"] == "ON":
        st.error("💥 Feedback trap triggered! Output was ON during feedback.")
        st.markdown("🧨 **GAME OVER** — synthetic meltdown.")
        st.stop()

    # ----- Output Streak Tracking -----
    if circuit["Output"] == "ON":
        st.session_state.Level2_OutputStreak += 1
        st.session_state.Level2_OutputONCount += 1
    else:
        st.session_state.Level2_OutputStreak = 0

    st.success(f"✅ Output: `{circuit['Output']}`")
    st.markdown(f"🔥 Streak: `{st.session_state.Level2_OutputStreak}`")
    st.markdown(f"🧮 Total Output ON: `{st.session_state.Level2_OutputONCount}`")

    # ----- Win Check -----
    if not st.session_state.Level2_Won and turn >= 10 and st.session_state.Level2_OutputONCount >= 4:
        st.session_state.Level2_Won = True
        st.balloons()
        st.success("🎉 Victory! You survived feedback hell.")
        st.markdown("🥇 Level 2 complete. Onward to Level 3!")

    # ----- Clear Inputs -----
    st.session_state.Level2_Inputs = {"IPTG": False, "AHL": False, "aTc": False}

    # ----- Turn Advance -----
    if not st.session_state.Level2_Won:
        st.session_state.Level2_Turn = int(st.session_state.Level2_Turn) + 1 if str(st.session_state.Level2_Turn).isdigit() else 1

    # ----- Mutation History (Optional)
    with st.expander("📉 Mutation Log"):
        if st.session_state.Level2_Mutations:
            for t, m in st.session_state.Level2_Mutations:
                st.markdown(f"Turn `{t}` → `{m}` flipped")
        else:
            st.markdown("No mutations yet.")

    # ----- Reset Button -----
    st.divider()
    if st.button("🔄 Restart Level 2"):
        for key, value in defaults.items():
            st.session_state[key] = value
        st.rerun()
