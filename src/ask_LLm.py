from together import Together
import os

client = Together(api_key="31077ccaed84525917480b62ce11a5f31b988eb655bc1a9409b63ff3ad820fd7")

def query_llama_maverick(messages):

     try:
        formatted = []
        for m in messages:
            formatted.append({
                "role": m["role"],
                "content": [{"type": "text", "text": m["content"]}]
            })

        response = client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=formatted
        )

        msg = response.choices[0].message

        # ✅ Handle both formats: list or string
        if isinstance(msg.content, list):
            return msg.content[0].text
        else:
            return msg.content

     except Exception as e:
        return f"[ERROR] {str(e)}"
