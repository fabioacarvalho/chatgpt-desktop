from openai import OpenAI
import asyncio
import openai

conversation_history = []


def request_chat(message, clear_history=False):

    if message:
        with open("configs.txt") as file:
            client = OpenAI(
                api_key=file.readline().split(",")[0],
            )
            arr_history = [{"role": "user", "content": msg['content']} for msg in conversation_history] if not clear_history else []

            print(f"arr_history: {arr_history}")

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=arr_history + [{"role": "user", "content": message}],
            )

            response = completion.choices[0].message
            
            # Atualizando o histórico de conversas com a resposta atual
            if response:
              conversation_history.append({"role": "assistant", "content": response.content})

            return response.content


