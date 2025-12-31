class ResearchPlanner:
    def plan(self, topic):
        return [
            f"Collect sources about {topic}",
            "Analyze information",
            "Generate structured summary"
        ]


planner = ResearchPlanner()
print(planner.plan("AI in healthcare"))
