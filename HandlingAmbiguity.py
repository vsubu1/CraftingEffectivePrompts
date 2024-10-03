import openai
 
# Set your OpenAI API key
openai.api_key = 'your-api-key
def handle_ambiguity_prompt(question, context):  
    prompt = "Given the following context : {context}\n\please clarify your question about {question}."
    response = openai.Completion.create(       
    engine="davinci",       
    prompt=prompt,      
    max_tokens=50,       
    temperature=0.7   
    )
   
    return response.choices[0].text.strip()
 
question = "school"
context = "In the context of education, school is an educational institution where students go and study to improve their quality of life."
ambiguous_question = "What's the role of a school?"
 
clarified_answer = handle_ambiguity_prompt

