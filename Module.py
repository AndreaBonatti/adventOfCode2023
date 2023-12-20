class Module:  # not broadcast module
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":  # Flip-flop
            self.memory = "off"
        else:  # Conjunction
            self.memory = {}

    def __repr__(self):
        return (self.name + "{type = " + self.type + ", outputs = " +
                ",".join(self.outputs) + ", memory = " + str(self.memory) + "}")
