from openai import OpenAI

client = OpenAI(
  api_key='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',
)

completion = client.chat.completions.create(
  model="tts-1",
  messages=[
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

# print(completion.choices[0].message)