import numpy as np

def simulate_toggle(current_state):
    # Mock time points
    time = np.linspace(0, 50, 500)
    # GFP levels depend on state
    if current_state == "ON":
        gfp = 10 * (1 - np.exp(-0.1 * time))  # rising GFP curve
    else:
        gfp = 10 * np.exp(-0.1 * time)       # decaying GFP curve

    # Create a structured array similar to Tellurium output
    # First column: time, second column: GFP
    result = np.column_stack((time, gfp))

    # Mock colnames attribute for compatibility with plotting
    class ResultWrapper:
        def __init__(self, data):
            self.data = data
            self.colnames = ["time", "GFP"]

        def __getitem__(self, item):
            return self.data[item]

    return ResultWrapper(result)
