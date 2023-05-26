import os
os.environ['OPENAI_API_KEY'] = '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'
import openai
models = openai.Model.list()
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", 
                                               messages=[{"role": "user", 
                                                          "content": "给我写一个方文山风格的歌词"}])

print(chat_completion.choices[0].message.content)