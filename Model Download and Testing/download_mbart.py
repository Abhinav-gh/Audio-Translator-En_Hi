from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
save_directory = "./mbart_model"

# # download and save model
# model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")

# # import tokenizer
# tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")

# Download and save the model
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
model.save_pretrained(save_directory)

# Download and save the tokenizer
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
tokenizer.save_pretrained(save_directory)
