def stateless(input_text):
    return f"Reply to {input_text}"

class Stateful:
    def __init__(self):
        self.memory = []

    def respond(self, input_text):
        self.memory.append(input_text)
        return f"Context size: {len(self.memory)}"


print(stateless("Hi"))
agent = Stateful()
print(agent.respond("Hi"))
print(agent.respond("Continue"))
