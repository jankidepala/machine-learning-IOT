# Chains
# Chains are the fundamental principle that holds various AI components in LangChain to provide context-aware responses. A chain is a series of automated actions from the user's query to the model's output. For example, developers can use a chain for:
# • Connecting to different data sources.
# • Generating unique content.
# • Translating multiple languages.
# • Answering user queries. 

# Chains are made of links. 
# Each action that developers string together to form a chained sequence is called a link. 
# With links, developers can divide complex tasks into multiple, smaller tasks. 
# Examples of links include:
# • Formatting user input. 
# • Sending a query to an LLM. 
# • Retrieving data from cloud storage.
# • Translating from one language to another.
# In the LangChain framework, a link accepts input from the user and passes it to the LangChain libraries for processing. LangChain also allows link reordering to create different AI workflows. 

# LCEL
# Developers then use the chain building blocks or LangChain Expression Language (LCEL) 
# to compose chains with simple programming commands. 

# The chain() function passes a link's arguments to the libraries. 
# The execute() command retrieves the results. 
# Developers can pass the current link result to the following link or return it as the final output. 

#Chain Parallel
