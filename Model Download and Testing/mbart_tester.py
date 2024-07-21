# Test if the model is downloaded successfully with the following code snippet:

from transformers import MBartForConditionalGeneration, MBart50TokenizerFast, pipeline

# Define the directory where the model and tokenizer are saved
load_directory = "./mbart_model"

# Load the model and tokenizer from the saved directory
model = MBartForConditionalGeneration.from_pretrained(load_directory)
tokenizer = MBart50TokenizerFast.from_pretrained(load_directory, src_lang="en_XX")

input_text = "Hello. Here is some text. This is just for testing"

# convert sentences to tensors
model_inputs = tokenizer(input_text, return_tensors="pt", padding=True)
# translate from English to Hindi
generated_tokens = model.generate(
    **model_inputs,
    forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
)
translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(translation)
