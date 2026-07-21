def build_prompt(question, context):

    return f"""
You are an expert resume reviewer.

Use ONLY the context below.

If the answer cannot be found,
say that it isn't available.

Context:
{context}

Question:
{question}

Answer:
"""