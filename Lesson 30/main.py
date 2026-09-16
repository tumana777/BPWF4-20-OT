# from dotenv import load_dotenv
# load_dotenv()
from pyexpat.errors import messages

# from anthropic import Anthropic
#
# client = Anthropic()
#
# message = client.messages.create(
#     model="claude-sonnet-4-5",
#     max_tokens=1000,
#     messages=[
#         {"role": "user", "content": "what is the capital of France?"}
#     ]
# )
#
# print(message.content[0].text)

# from anthropic import Anthropic
#
# client = Anthropic()
#
# message = client.messages.create(
#     model="claude-sonnet-4-5",
#     max_tokens=1000,
#     messages=[
#         {"role": "user", "content": "Write a Python function to calculate the factorial of a number."}
#     ]
# )
#
# print(message.content[0].text)
# print("=" * 30)
# print(message.usage.input_tokens)
# print(message.usage.output_tokens)
# print("=" * 30)

# from anthropic import Anthropic
#
# client = Anthropic()
#
# message = client.messages.create(
#     model="claude-sonnet-4-5",
#     system="You are a C++ programmer.",
#     max_tokens=1000,
#     messages=[
#         {"role": "user", "content": "Write a function that returns sum of two numbers."}
#     ]
# )
#
# print(message.content[0].text)
# print("=" * 30)
# print(message.usage.input_tokens)
# print(message.usage.output_tokens)
# print("=" * 30)

# from anthropic import Anthropic
#
# client = Anthropic()
#
# messages = [
#     {"role": "user", "content": "What is function?"},
#     {"role": "assistant", "content": "A function is a block of code designed to perform a particular task. It takes input, processes it, and returns an output. Functions help in organizing code, making it reusable and easier to read."},
#     {"role": "user", "content": "Give me an example"},
# ]
#
# message = client.messages.create(
#     model="claude-sonnet-4-5",
#     system="You are a Python programmer.",
#     max_tokens=1000,
#     messages=messages
# )
#
# print(message.content[0].text)
# print("=" * 30)
# print(message.usage.input_tokens)
# print(message.usage.output_tokens)
# print("=" * 30)

from anthropic import Anthropic

client = Anthropic()

messages = []

while True:
    message = input("You: ")

    if message == "exit":
        break

    messages.append({"role": "user", "content": message})

    response = client.messages.create(
        system="You are a Python teacher.",
        model="claude-sonnet-4-5",
        max_tokens=1000,
        messages=messages
    )

    answer = response.content[0].text

    print(f"Assistant: {answer}")

    messages.append({"role": "assistant", "content": answer})


























