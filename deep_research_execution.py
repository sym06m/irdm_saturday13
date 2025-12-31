class ResearchAgent:
    def __init__(self, plan):
        self.plan = plan
        self.results = []

    def execute(self):
        for step in self.plan:
            self.results.append(f"Completed: {step}")
        return self.results


plan = [
    "Collect sources",
    "Analyze data",
    "Write report"
]

agent = ResearchAgent(plan)
print(agent.execute())
