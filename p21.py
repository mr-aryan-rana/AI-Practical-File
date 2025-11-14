from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  
model = AutoModelForCausalLM.from_pretrained("gpt2")
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)
def gpt(prompt):
    result = generator(
        prompt,
        max_new_tokens=60, 
        temperature=0.7,
        top_p=0.9,
        truncation=True,  
        pad_token_id=tokenizer.eos_token_id
    )
    return result[0]["generated_text"]
print("Type 'exit' or 'quit' to end the program.\n")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ("exit", "quit", "bye"):
        print("GPT: Goodbye!")
        break
    elif user_input in ("hii", "hello", "hi","hey"):
        print("GPT: Hello! How can I assist you today?")
        continue
    else:
        response = gpt(user_input)
        print("GPT:", response)
