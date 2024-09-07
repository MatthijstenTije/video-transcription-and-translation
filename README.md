# video-transcription-and-translation
This repository provides a Python script that leverages OpenAI's API to automate the transcription and translation of video files. The script processes videos from a specified directory, extracts their audio, transcribes it using the Whisper model, and then proofreads and translates the transcript into English, if necessary, using GPT-4.

## Usage Instructions

### Prepare Video Files
Place the video files you wish to process in the files/videos directory. The script supports the following video file formats: .mp4, .avi, .mov, and .mkv.

### Run the Script
Execute the script by running in your terminal.

```bash
python script_name.py
```

The output transcripts will be saved in the files/transcripts directory.

## API Requirements

To use this script, you need access to OpenAI's API:
- Whisper Model: For audio transcription.
- GPT-4 Model: For proofreading and translating the transcriptions.
For a step-by-step guide on how to obtain an OpenAI API Key check out the following [article.](https://tilburg.ai/2024/03/openai-api-tutorial-python/)

