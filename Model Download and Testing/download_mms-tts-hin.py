from transformers import VitsTokenizer, VitsModel

# Define the directory to save the model and tokenizer
save_directory = "./mms-tts-hin"

# Download and save the tokenizer
tokenizer = VitsTokenizer.from_pretrained("facebook/mms-tts-hin")
tokenizer.save_pretrained(save_directory)

# Download and save the model
model = VitsModel.from_pretrained("facebook/mms-tts-hin")
model.save_pretrained(save_directory)
