from abc import ABC

# sinais_entrada -> entrada do tipo f(ST, emergencyButton...)
ST = bool(0),
emergencyButton = bool(0),
levelSensor = bool(0),
pressure_1 = float(0),
pressure_2 = float(0),
intake_pressure = float(35),
outlet_pressure = float(250)

class State:
    def __init__(self, name, weight, trigger, amount):
        self.name = str(name)
        self.weight = int(weight)
        self.trigger = bool(trigger)
        self.amount = int(amount)

# lista de estados da rede de Petri           
gnv_supply = State("gnv supply", 1, 0, 1)
compression1 = State("compression 1", 2, 0, 1)
heat_exchange1 = State("heat exchange 1", 1, 0, 1)
compression2 = State("compression 2", 1, 0, 1)
heat_exchange2 = State("heat exchange 2", 1, 0, 1)
storage = State("storage", 1, 0, 1)
            
class Arc:
    """
    Define o arco na rede de petri
    """
    def __init__(self, state, amount):
        self.state = state
        self.amount = amount

    """
    Métodos de verificação do gatilho, saída e entrada de fichas (se o peso W for = número de fichas, gatilho autorizado)
    """

class TriggerOut(Arc):
    def triggerOut(self):
        self.place.weight -= 1  

    @staticmethod    
    def verify_trigger(self):
        return self.weight >= self.amount
        
class TriggerIn(Arc):
    def triggerIn(self):
        self.place.weight += 1

class Transition:
    """
    Define a transição pela somatória de arcos in e arcos out
    """  
    def __init__(self, arcs_in, arcs_out):
        self.arcs_out = set(arcs_out)
        self.arcs_in = set(arcs_in)
        self.arcs = self.arcs_out.union(arcs_in)
        
    def transition(self):
        not_blocked = all(arc.verify_trigger() for arc in self.arcs_out)
        if not_blocked:
            for arc in self.arcs:
                arc.verify_trigger()
        return not_blocked
    
# lista de transições da rede de petri

start_button = 1
inlet_valve1 = 0
preheat_exchange1 = 0
inlet_valve2 = 0
preheat_exchange2 = 0

class PetriNet:
    def __init__(self, transitions):
        self.transitions = transitions

    def start(self, start_sequence, pt):
        for name in start_sequence:
            t = self.transitions[name]
            t.trigger()

    ts = []
    ts = dict(
        t1 = Transition(
            TriggerOut(ts)
        )
    )

petri_net = PetriNet(ts)
petri_net.start(start_sequence, ps)