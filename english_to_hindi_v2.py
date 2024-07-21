# -*- coding: utf-8 -*-
"""English to Hindi_v2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rNpAC9WeqaSOIHpL7TT1wh3ryJ4kutIq
"""

# !pip install speechrecognition
# !pip install pydub

# !pip install pyaudio

import speech_recognition as sr

recognizer = sr.Recognizer()

# Path to your input (.wav only) file.
input_audio_file = "shotcutLesson.wav"

# Load audio file
with sr.AudioFile(input_audio_file) as source:
    print("Adjusting noise")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording complete file")
    recorded_audio = recognizer.record(source) #Give duration = [seconds] to do for some duration
    print("Done recording")

try:
    print("Recognizing the text")
    speech_to_text = recognizer.recognize_google(
        recorded_audio,
        language="en-US"
    )

    print("Decoded Text: {}".format(speech_to_text))

except Exception as ex:
    print(ex)

import torch

#Punctuate the text using this pre-trained model
model, example_texts, languages, punct, apply_te = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                  model='silero_te')

input_text = speech_to_text
punctuated_speech_to_text=apply_te(input_text, lan='en')
print(punctuated_speech_to_text)

# !pip install nltk

# Cell to separate punctuated speech text into sentences

import nltk
nltk.download('punkt')


# Tokenize the string into sentences
punctuated_sentences_list = nltk.sent_tokenize(punctuated_speech_to_text)

print(punctuated_sentences_list)

# #install transformers library
# !pip install transformers -U -q

# # install sentencepiece library
# !pip install sentencepiece

from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
save_directory = "./mbart_model"
load_directory = "./mbart_model"

# Load the tokenizer
tokenizer = MBart50TokenizerFast.from_pretrained(load_directory, src_lang="en_XX")

# Load the model
model = MBartForConditionalGeneration.from_pretrained(load_directory)

# # Download and save the model
# model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
# model.save_pretrained(save_directory)

# # Download and save the tokenizer
# tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
# tokenizer.save_pretrained(save_directory)

translated_pun_sentences_list=[]
for t_p_sentence in punctuated_sentences_list:

    # input sentences
    input_text = t_p_sentence

    # convert sentences to tensors
    model_inputs = tokenizer(input_text, return_tensors="pt", padding=True)
    # translate from English to Hindi
    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
    )
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    translated_pun_sentences_list.append(translation[0])
print(translated_pun_sentences_list)


# The output of the above cell should come as: Use if you don't get output. Comment everything above
# translated_pun_sentences_list=['इस वीडियो में, मैं आपको विण्डोज पर शॉर्टकट डाउनलोड करने के लिए कैसे दिखाएँगा.', 'शॉर्टकट एक मुक्त और खुला स्रोत वीडियो संपादक है।', 'चलो बस गूगल में जाएँ और खोज सभी एक शब्द और वेबसाइट पता Shotcut डॉट ऑर्ग है।', 'मैं इस वीडियो के वर्णन में लिंक शामिल करूंगा और आगे बढ़ें और सिर्फ डाउनलोड पर क्लिक करें, तो यह कानूनी रूप से मुफ्त सॉफ्टवेयर है, लेकिन आप सावधान रहना चाहिए.', 'ये विज्ञापन कुछ और के लिए हैं।', 'यह अब यहाँ से शुरू कर रहे हैं और ये बदलने के लिए जा रहे हैं यह आप के लिए अलग हो सकता है।', 'केवल सुनिश्चित करें कि वास्तविक डाउनलोड लिंक थोड़ा भ्रमित है यह सिर्फ एक सादा पाठ है।', 'आप उसके ऊपर कर सकते हैं और क्लिक करें और तो इनमें से किसी भी वास्तव में काम करेगा।', 'आप शायद जिप से बचना चाहते हैं और केवल 64-बिट या 32-बिट इंस्टॉलर को प्राप्त कर सकते हैं और यह कोई बात नहीं है कि आप.', 'एक या दो साइट से, यह सिर्फ एकाधिक विकल्पों से डाउनलोड करने के लिए है मैं यह करने के लिए जा रहा हूँ जो साइट है [UNK] से और मैं 64-बिट इंस्टॉलर करने के लिए जा रहा हूँ कि शायद आपके लिए भी अच्छा विकल्प होगा बस मेरे मन को रखें अगर आप बहुत पुराने की तरह एक पुराने कंप्यूटर है, आप 32-बिट इंस्टॉलर करना चाहते हैं या शायद एक पुराने लैपटॉप या कुछ लेकिन अधिकतर कंप्यूटर.', 'आजकल यह 64-बिट है तो यह डाउनलोड कर रहा है और मैं गति पर वीडियो रुकाएँगी।', 'यह ठीक है कि अब डाउनलोड समाप्त है तो मैं फायरफॉक्स पर डाउनलोड देख सकते हैं यहाँ क्लिक करके और यह मुझे दिखाता है।', 'मैं इस फ़ोल्डर पर क्लिक कर सकता हूँ और यह उस स्थान को खोलेगा जो मेरे कंप्यूटर पर सहेजा गया है या मैं सिर्फ फ़ाइल एक्सप्लोरर को खोल सकता हूँ और डाउनलोड में जा सकता है, जो यह मेरे कंप्यूटर पर डाउनलोड किया है और यह है.', 'शॉटकट डैश 164 तो मैं इस फ़ाइल पर क्लिक करूँगा और क्योंकि यह ज़िप नहीं है यह बस ठीक से संस्थापना शुरू कर देंगे तो यह संवाद लाता है।', 'मैं शर्तों और शर्तों से सहमत हूं।', 'मैं सिर्फ सब कुछ डिफ़ॉल्ट पर छोड़ देता हूँ और इंस्टॉल करने के लिए अगला क्लिक करता हूँ मैं इसे इस भाग पर त्वरित कर देता हूँ ठीक है वहाँ है तो शॉटकट अब मेरे कंप्यूटर पर इंस्टॉल किया गया है।', 'मैं इन सब से बंद कर सकता हूँ और यदि मैं अपने कंप्यूटर पर प्रारंभ बटन क्लिक करता हूँ और सिर्फ शॉटकट में लिखें तो यह आता है और मैं इसके लिए एक डेस्कटॉप चिह्न बना सकता है लेकिन यहाँ हम इसे है तो यह शॉटकट है और मैं सिर्फ शुरू करने के लिए आपको जल्दी दिखाएँगे.', 'तो यह यहाँ फ़िल्टर से शुरू होता है।', 'लेकिन अगर हम बदलना चाहते हैं.', 'हम सेटिंग पर क्लिक कर सकते हैं और और हम सजावट में जा सकते हैं और.', 'हम इस समयरेखा परियोजना में बदल सकते हैं की तरह है क्या यहाँ डिफ़ॉल्ट से है।', 'हम केवल यह सिर्फ अलग विकल्पों में यहाँ है तो यह लेआउट करने और क्लिप करने के लिए जा सकते हैं और वहाँ भी पूर्वनिर्धारित लेआउट करने के लिए पूर्ववत है यदि हम किसी भी अन्य अलग संवाद के रूप में चाहते हैं आप यहाँ क्लिक कर इतिहास दिखाया जा रहा है टॉगल करने के लिए दिखाया जा रहा है शिखर मीटर दिखाया जा रहा है.', 'यदि अंतरफलक पर कुछ बंद हो जाता है.', 'आप इसे वापस लाने के लिए यहाँ समयरेखा की तरह क्लिक कर सकते हैं लेकिन वीडियो के साथ शुरू करने के लिए आपको एक परियोजना नाम में टाइप करना होगा और फिर हम कुछ वीडियो में खींचेंगे और आपको प्लेलिस्ट पर क्लिक करना होगा यह सबसे महत्वपूर्ण हिस्सा है.', 'आप सिर्फ फ़ाइल खोलकर प्लेलिस्ट कर सकते हैं.', 'आप वास्तव में कई वीडियो फ़ाइलों में खींच सकते हैं और वहाँ आप इसे है कि एक shotgun आगे जाएँ और अभ्यास श्रृंखला की जाँच करने के लिए है।', 'अगर आप इस सॉफ्टवेयर का अधिक पूर्ण प्रयोग करने के लिए कैसे सीखना चाहते हैं और अन्य वीडियो देखें।', 'जहां मैं सभी गुणों और प्रकारों के मुक्त और मुक्त स्रोत सॉफ्टवेयर का प्रदर्शन करता हूं अगले वीडियो को देखने के लिए धन्यवाद।']

from transformers import VitsTokenizer, VitsModel, set_seed
import torch

load_directory = "./mms-tts-hin"

# Load the tokenizer
tokenizer = VitsTokenizer.from_pretrained(load_directory)

# Load the model
model = VitsModel.from_pretrained(load_directory)

import scipy
import torch
import soundfile as sf
for i,t_p_sentence in enumerate(translated_pun_sentences_list,1):
    print(t_p_sentence)
    inputs = tokenizer(text=t_p_sentence, return_tensors="pt")

    set_seed(555)  # make deterministic
    with torch.no_grad():
        outputs = model(inputs["input_ids"])
    outputs.waveform.shape

    # Retrieve the waveform from the outputs
    waveform = outputs.waveform.squeeze().cpu().numpy()

    # Save the waveform to a WAV file
    sav_dir="./sessionAudiofiles/"
    savePath=sav_dir+"output "+str(i)+".wav"
    sf.write(savePath, waveform, 22050)

    print("Audio saved to output ",str(i),".wav",sep="")

from pydub import AudioSegment
from pydub.silence import detect_silence

# Load the original English audio file
input_audio_file = "shotcutLesson.wav"
audio = AudioSegment.from_wav(input_audio_file)

# Detect silences in the audio
silence_threshold = -40  # dBFS (decibels relative to full scale)
min_silence_len = 500  # milliseconds
silences = detect_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_threshold)

# Calculate the durations of the silences
silence_durations = [(end - start) for start, end in silences]

# Print the silence durations
print(silence_durations)

# Make the final file
from pydub import AudioSegment
import os

# Define the directory containing the Hindi sentence WAV files
wav_dir = "./sessionAudiofiles/"
wav_files = [f"output {i}.wav" for i in range(1, len(translated_pun_sentences_list)+1)]  # THe number of sentences times

# Initialize the final output audio
final_output = AudioSegment.silent(duration=0)

# Insert silences and combine audio segments
for i, wav_file in enumerate(wav_files):
    # Load the current sentence WAV file
    sentence_audio = AudioSegment.from_wav(os.path.join(wav_dir, wav_file))
    final_output += sentence_audio

    # Add the corresponding silence if it exists
    if i < len(silence_durations):
        silence_duration = silence_durations[i]  # Duration in milliseconds
        silence_segment = AudioSegment.silent(duration=silence_duration)
        final_output += silence_segment

# Export the final output to a WAV file
final_output.export("./sessionAudiofiles/end_result.wav", format="wav")

print("Final output saved as end_result.wav in sessionAudiofiles directory")
