from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

template = ChatPromptTemplate([
    ('system', 'This is a intelligent {domain} bot'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

prompt = template.invoke({
    'domain' : 'Customer Support',
    'chat_history' : chat_history,
    'query' : 'What is my refund status'
})

print(prompt)