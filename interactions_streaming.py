def stream_research(steps):
    for step in steps:
        yield f"Streaming: {step}"


steps = ["Search papers", "Extract facts", "Summarize"]

for output in stream_research(steps):
    print(output)
