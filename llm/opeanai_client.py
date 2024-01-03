from openai import OpenAI
class OpenAILLM():

    def __init__(self) -> None:
        self.client = OpenAI()

    def get_embedding(self, text, model="text-embedding-ada-002"):
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input = [text], model=model).data[0].embedding

    def run(self, message):
        
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )

        return completion.choices[0].message.content