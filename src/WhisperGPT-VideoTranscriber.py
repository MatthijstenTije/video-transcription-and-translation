from openai import OpenAI
import os

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

directory_path = 'files/videos'
transcripts_path = 'files/transcripts'

video_files = [file for file in os.listdir(directory_path) if file.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

for video_file_name in video_files:
    video_path = os.path.join(directory_path, video_file_name)
    
    with open(video_path, "rb") as video_file:
        audio_response = client.audio.transcriptions.create(
        model = "whisper-1",
        file = video_file
        )
        
    transcript = audio_response.text
    
    prompt = f"""Transform the uploaded transcript, between parentheses with the following two steps:
     Step 1 - Proofread it without changing its structure 
     Step 2 - If it is not in English, translate it to English
     ```{transcript}```"""
    
    
    chat_response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {"role":"system",
         "content": "Act as a helpful assistant"},
        {"role":"user",
        "content":prompt}
    ],
    temperature = 0)
    
    transcript_file_path = os.path.join(transcripts_path, f"{os.path.splitext(video_file_name)[0]}.txt")
    
    with open(transcript_file_path, 'w') as transcript_file:
            transcript_file.write(chat_response.choices[0].message.content)
