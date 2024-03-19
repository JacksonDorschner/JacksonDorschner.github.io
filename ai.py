import ollama

def aiResponse():
  msgContent = input() + " (respond as if you were a therapist/mental health expert.)"
  message = {'role': 'user', 'content': msgContent}

  for part in ollama.chat(model='mistral', messages=[message], stream=True):
    return (part['message']['content'])