import os
from pdf_file import get_pdf_file
from gtts import gTTS
from converter import pdf_to_audio

root_dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir_path, get_pdf_file())

if __name__ == '__main__':
    speaker = gTTS(pdf_to_audio(file_path), lang='ru').save('test.mp3')
