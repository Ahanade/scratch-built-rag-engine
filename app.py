import json
import os
import gradio as gr

def search_database(user_query, chunks):
    query_words = user_query.lower().replace("?", "").split()
    best_chunk = None
    highest_score = 0
    for chunk in chunks:
        score = 0
        chunk_lower = chunk.lower()
        for word in query_words:
            if word in chunk_lower:
                score += 1
        if score > highest_score:
            highest_score = score
            best_chunk = chunk
    if highest_score == 0:
        return "I'm sorry, I couldn't find any relevant information."
    return best_chunk

def generate_ai_response(question, context):
    if "couldn't find any relevant information" in context or not context:
        return "I'm sorry, I couldn't find an answer to that in the dataset."
    if "Answer:" in context:
        return context.split("Answer:")[-1].strip()
    return context


document_chunks = []
if os.path.exists("dataset.json"):
    with open("dataset.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for intent in data['intents']:
        clean_response = intent['responses'].replace("<br />", " ").replace("<br>", " ")
        for pattern in intent['patterns']:
            document_chunks.append(f"Question: {pattern} | Answer: {clean_response}")

def ask_assistant(user_question):
    context = search_database(user_question, document_chunks)
    return generate_ai_response(user_question, context)

demo = gr.Interface(
    fn=ask_assistant, 
    inputs=gr.Textbox(label="Ask a question:", placeholder="Type here..."),
    outputs=gr.Textbox(label="Response:"),
    title="🏫 Intelligent Dataset Assistant",
    description="A scratch-built RAG Engine mapping intent structures via pure python word-token loops."
)

if __name__ == "__main__":
    demo.launch()
