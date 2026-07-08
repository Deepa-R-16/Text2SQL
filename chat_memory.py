from langchain_classic.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

def save_chat(user_question, ai_answer):
    memory.chat_memory.add_user_message(user_question)
    memory.chat_memory.add_ai_message(ai_answer)

def get_chat_history():
    return memory.load_memory_variables({})["chat_history"]