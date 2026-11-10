from models import load_text_model, generate_text

model = load_text_model()
prompts = ["The cat is on the table.", "Explain what a neural network is.", "Students are learning Python. "
"They are building an application to translate English texts into French."]
for prompt in prompts:
    print("Prompt:")
    print(prompt)
    print("")
    print("Resposta:")
    print(generate_text(model, prompt))

    print("\n--------------------\n")