class InteractionSession:
    def __init__(self):
        self.turns = []

    def send(self, user_input):
        self.turns.append({"role": "user", "content": user_input})
        response = f"Model response to: {user_input}"
        self.turns.append({"role": "model", "content": response})
        return response


session = InteractionSession()
print(session.send("Explain AI agents"))
print(session.send("Give a real example"))
