import bpy
import time
import os
import subprocess

blend_files = [  
    r"C:\path\to\your\file.blend",  
]

output_directories = [  
    r"C:\path\to\your\output\location", 
]

frame_delay = 10  
file_delay = 60  
frame_rate = 60  


def render_blend_file(blend_file, output_directory):
    try:
        bpy.ops.wm.open_mainfile(filepath=blend_file)

        start_frame = bpy.context.scene.frame_start
        end_frame = bpy.context.scene.frame_end

        bpy.context.scene.render.image_settings.file_format = 'PNG'
        os.makedirs(output_directory, exist_ok=True)

        for frame in range(start_frame, end_frame + 1):
            bpy.context.scene.frame_set(frame)
            bpy.context.scene.render.filepath = f"{output_directory}/frame_{frame:04d}.png"
            bpy.ops.render.render(write_still=True)
            print(f"Rendered frame {frame} from {blend_file}")
            time.sleep(frame_delay)
    except Exception as e:
        print(f"Error rendering {blend_file}: {e}")


def create_video_from_frames(output_directory, frame_rate):
    try:
        input_pattern = os.path.join(output_directory, "frame_%04d.png")
        output_video = os.path.join(output_directory, "output.mp4")

        ffmpeg_command = [  
            "ffmpeg",
            "-framerate", str(frame_rate),
            "-i", input_pattern,
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            output_video
        ]

        print(f"Creating video from frames in {output_directory}")
        result = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print(f"Video successfully created: {output_video}")
        else:
            print(f"Error creating video: {result.stderr.decode('utf-8')}")
    except Exception as e:
        print(f"Error during video creation: {e}")


if len(blend_files) != len(output_directories):
    raise ValueError("The number of blend files and output directories must be the same!")

for blend_file, output_directory in zip(blend_files, output_directories):
    print(f"Starting render for {blend_file} with output to {output_directory}")
    render_blend_file(blend_file, output_directory)

    print(f"Finished rendering {blend_file}. Creating video from rendered frames.")
    create_video_from_frames(output_directory, frame_rate)

    print(f"Finished processing {blend_file}. Waiting {file_delay} seconds before next file.")
    time.sleep(file_delay)
