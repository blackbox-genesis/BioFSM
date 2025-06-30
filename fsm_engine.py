class State:
    def __init__(self, name, is_gfp_on=False, description=""):
        self.name = name
        self.is_gfp_on = is_gfp_on
        self.description = description
        self.transitions = {} #input_signal: next_state

    def add_transitions(self, input_signal, next_state_name):
        self.transitions[input_signal] = next_state_name

class BioFSM:
    def __init__(self, states, initial_state_name):
        self.states = {state.name: state for state in states}
        self.initial_state_name = initial_state_name
        self.current_state = self.states[initial_state_name]
        self.history = []

    def reset(self):
       self.current_state = self.states[self.initial_state_name]
       self.history = []

    def transition(self, input_signal):
        if input_signal in self.current_state.transitions:
            next_state_name = self.current_state.transitions[input_signal]
            self.history.append((self.current_state.name, input_signal, next_state_name))
            self.current_state = self.states[next_state_name]
        else:
            self.history.append((self.current_state.name, input_signal, "No Transition"))

    def get_output(self):
     return "GFP ON" if self.current_state.is_gfp_on else "GFP OFF"

    def get_state_info(self):
     return {
        "state": self.current_state.name,
        "output": self.get_output(),
        "description": self.current_state.description
    }
