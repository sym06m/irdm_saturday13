class InteractionTransport:
    def send(self, message):
        return f"Sent: {message}"

    def receive(self):
        return "Received model response"


transport = InteractionTransport()
print(transport.send("User query"))
print(transport.receive())
