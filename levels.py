from fsm_engine import State, BioFSM

def load_toggle_switch():
    #Define states
    state_a = State("OFF", is_gfp_on=False, description="LacI active, GFP repressed")
    state_b = State("ON", is_gfp_on=True, description="TetR active, GFP expressed")

    #Define transitions
    state_a.add_transitions("IPTG", "ON")
    state_b.add_transitions("aTc", "OFF")

    fsm = BioFSM(states=[state_a, state_b], initial_state_name="OFF")
    return fsm