class InteractionTurn:
    def __init__(self, role, content):
        self.role = role
        self.content = content


history = []
history.append(InteractionTurn("user", "Start research"))
history.append(InteractionTurn("model", "Research initialized"))

for turn in history:
    print(turn.role, ":", turn.content)
