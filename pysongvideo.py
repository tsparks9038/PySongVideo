from tkinter import Tk, Button, Label
from tkinter.filedialog import askopenfilename, asksaveasfilename

from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips


def generate_video():
    audio_file = askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.mp3;*.wav")])
    image_file = askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    output_file = asksaveasfilename(defaultextension=".mp4", filetypes=[("Video Files", "*.mp4")])

    if not audio_file or not image_file or not output_file:
        return

    audio = AudioFileClip(audio_file)
    image = ImageClip(image_file)
    image = image.set_duration(audio.duration)
    image = image.set_fps(24)
    video = concatenate_videoclips([image])
    video = video.set_audio(audio)
    video.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=24, preset="ultrafast")

    label_result["text"] = "Video generated successfully!"


root = Tk()
root.title("Audio and Image to Video Converter")

button_generate = Button(root, text="Generate Video", command=generate_video)
button_generate.pack(pady=20)

label_result = Label(root, text="")
label_result.pack()

root.mainloop()
