import openai 

def askGPT(text):
  openai.api_key = "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"
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = text,
    temperature = 8.6,
    max_tokens = 150,
     )
     return print(response.choices[0].text)
     
     def main():
       while True:
         print('GPT: Ask me a question bobo ka\n')
         python = input ()
         askGPT(myOn)
         print('\n')
         
         main()
