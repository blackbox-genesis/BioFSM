import tellurium as te
def simulate_toggle(current_state):
    model = '''
    model toggle_switch
    # Species
    species LacI, TetR, GFP
    # Initial Concentrations
    LacI = 0;
    TetR = 0;
    GFP = 0;
    # Parameters
    k1 = 1;
    k2 = 1;
    k3 = 1;
    d1 = 0.5; 
    d2 = 0.5;
    d3 = 0.5;
    # Reactions 
    J1: -> LacI; k1
    J2: -> TetR; k2
    J3: -> GFP; k3*TetR
    # Degradation
    J4: LacI -> ; d1*LacI
    J5: TetR -> ; d2*TetR
    J6: GFP -> ; d3*GFP
    end
    '''

    if current_state == "OFF":
        model = model.replace("LacI = 0", "LacI = 10")
    elif current_state == "ON":
        model = model.replace("TetR = 0", "TetR = 10")

    r = te.loada(model)
    result = r.simulate(0, 50, 500)
    return result