from moviepy.editor import VideoFileClip
import os
from PIL import Image
from moviepy.editor import ImageSequenceClip, AudioFileClip

def extract_frames_audio(video_path):
    video=VideoFileClip(video_path)
    audio=video.audio
    audio.write_audiofile("Audio_"+video_path.split('.')[0]+".wav")
    audio.close()

    if not os.path.exists('./temp'):
        os.makedirs('./temp')
    
    for i,frames in enumerate(video.iter_frames()):
        #Image.fromarray(frames).save('./temp/frame'+str(i)+'.png')  
        frame_filename = os.path.join('./temp', f"frame_{i:04d}.png")
        frame_image = Image.fromarray(frames)
        frame_image.save(frame_filename)


def create_video_from_frames_and_audio(output_video_file, fps=24):
    frame_files = [os.path.join('./temp', f) for f in sorted(os.listdir('./temp')) if f.endswith('.png')]
    video_clip = ImageSequenceClip(frame_files, fps=fps)
    
    audio_clip = AudioFileClip("Audio_demo-video.wav")
    video_clip = video_clip.set_audio(audio_clip)
    
    video_clip.write_videofile(output_video_file, codec='libx264', audio_codec='aac')
    
    print(f"Video has been created and saved to {output_video_file}")

extract_frames_audio('demo-video.mp4')
create_video_from_frames_and_audio('output_video.mp4')