from openai import OpenAI

client = OpenAI(
  api_key='sess-ytGZpQmYjyGN5YlTattZU3oYlHsztmNbp4zoLrc7',
  # api_key='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',
)


assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo-1106"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

print(messages.data[0].content[0].text.value)
print(len(messages.data))
