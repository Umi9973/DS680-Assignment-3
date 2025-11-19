import json
import os

# Load prompts from JSON file
with open("prompts/consent_prompts_en.json", "r") as f:
    prompts = json.load(f)

# Simulated generation function (replace this with actual API call to OpenAI or Ollama)
def generate_response(prompt_text, model_name="gpt-4", temperature=0.7):
    # Placeholder response
    return f"[Simulated response from {model_name}]: '{prompt_text[:60]}...'"

# Output directory
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# Output file for generated responses
output_file = os.path.join(output_dir, "responses_modelA.jsonl")
with open(output_file, "w") as out_f:
    for prompt in prompts:
        prompt_id = prompt["id"]
        text = prompt["prompt_text"]
        model_response = generate_response(text)
        record = {
            "prompt_id": prompt_id,
            "model": "modelA",
            "response": model_response
        }
        out_f.write(json.dumps(record) + "\n")

print(f"Responses saved to {output_file}")
