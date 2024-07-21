from pydub import AudioSegment

# Load the saved audio file
audio_segment = AudioSegment.from_wav("./sessionAudiofiles/end_result.wav")

# Slow down the audio by a factor (e.g., 0.75 for 75% of the original speed)
slow_audio_segment = audio_segment._spawn(audio_segment.raw_data, overrides={
    "frame_rate": int(audio_segment.frame_rate * 0.75)
}).set_frame_rate(audio_segment.frame_rate)

# Export the slowed audio to a new file
slow_audio_segment.export("end_result_slow_output.wav", format="wav")

print("Slowed audio and processed audio saved to ./slow_output.wav")

# # Optional: Play the slowed audio directly in the notebook
# from IPython.display import Audio
# Audio("slow_output.wav")