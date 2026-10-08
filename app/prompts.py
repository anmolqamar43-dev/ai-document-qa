def zero_shot_prompt(question):
    """
    Zero-shot prompting:
    The model receives only the question.
    """
    return f"""
Answer the following question clearly and accurately.

Question:
{question}

Provide a concise and easy-to-understand answer.
"""


def few_shot_prompt(question):
    """
    Few-shot prompting:
    The model receives examples before answering.
    """
    return f"""
Answer the question using the examples below as a guide.

Example 1:
Question: What is Python?
Answer: Python is a high-level programming language used
for software development, automation, data science, and AI.

Example 2:
Question: What is Artificial Intelligence?
Answer: Artificial Intelligence is a field of computer science
that enables machines to perform tasks that normally require
human intelligence.

Example 3:
Question: What is Machine Learning?
Answer: Machine Learning is a branch of AI that allows computers
to learn patterns from data and make predictions or decisions.

Now answer this question:

Question:
{question}

Provide a clear and concise answer.
"""


def role_based_prompt(question):
    """
    Role-based prompting:
    The model is assigned the role of a technical expert.
    """
    return f"""
You are an expert AI and technical document analyst.

Your task is to answer the user's question accurately,
clearly, and in an educational manner.

Explain technical concepts in simple language.
Avoid unnecessary information.

Question:
{question}

Provide a clear and relevant answer.
"""