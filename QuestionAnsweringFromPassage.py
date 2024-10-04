import openai
openai.api_key = ""
GPT_MODEL = "gpt-3.5-turbo"

document_list = """ Speech-to-Text Conversion: The first step in voice recognition is converting spoken words into text. This process, known as speech-to-text or automatic speech recognition (ASR), involves analyzing audio signals and transcribing them into written form.
2. Natural Language Understanding (NLU): Once the spoken words are converted to text, NLP techniques are applied to understand the meaning and intent behind the words. 
3. Intent Recognition: Identifying the user's intent based on the voice command is a crucial step. Virtual assistants use NLP models to recognize the specific action or task the user is requesting.
4. Response Generation: After understanding the user's intent, the virtual assistant generates an appropriate response. This can involve looking up information, performing actions, or providing relevant details.
5. Voice Synthesis (Text-to-Speech): In cases where the virtual assistant needs to respond vocally, the system uses text-to-speech (TTS) technology to convert the written response into spoken words.
 """

query = f"""Use the given passage from document_list  to answer the  question. If you don't find any answer, write "No specific topic found."

Article:
\"\"\"
{document_list}
\"\"\"

Question: Explain NLU"""

response = openai.chat.completions.create(
    messages=[
        {'role': 'system', 'content': 'You answer questions from the given passage.'},
        {'role': 'user', 'content': query},
    ],
    model=GPT_MODEL,
    temperature=0,
)

print(response.choices[0].message.content)

response1 = openai.Embedding.create(
    input="canine companions say",
    engine="text-similarity-davinci-001")

print(response1)