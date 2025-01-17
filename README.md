# Blender Render Automation Script

![Image](https://github.com/user-attachments/assets/a92ba7d8-b2d6-4bd3-a0ff-7a1bd792e19b)

## Who is this for?

- **Anyone looking to automate Blender animation rendering**: This script allows you to set up an automated rendering sequence of `.blend` files and their output locations, eliminating the need for manual intervention, so you can let it run in the background.

- **Users facing GPU overload issues in Blender**: If Blender pushes your GPU to 100% usage, leading to crashes or overheating, this script introduces customizable breaks between frames and files to reduce load, prevent system or GPU failures and overheating.

- **Those who need a reliable terminal-based rendering solution**: For users who can't rely on Blender's internal rendering system, this script offers a stable and efficient alternative for rendering animations outside of Blender.

## What it does
- Opens and renders given `.blend` files in order with `blender.exe`.
- Renders each frame of the animation as PNG images.
- Creates a video from all the rendered frames using FFmpeg.
- Supports frame delays, file delays and customizable settings for rendering and video creation.

## Requirements
Make sure you have on your system:
- `Blender` installed,
- `FFmpeg` installed,
- `render.py` script from this repository on your PC.

## Preparation

Having prepared:

- all `.blend` files with your animations (with all the render settings you want), 
- an empty folder for each `.blend` file output, 
- `render.py` in your desired location,

Open render.py file and adjust the following in the code to your needs: 

*.blend file paths:*

    # list of paths to your .blend files, make sure they are correct

    blend_files = [ 
        r"C:\path\to\your\file.blend",  # replace this with the path to your .blend file
      # r"C:\path\to\your\file2.blend",
        # ... 
        # add as many as needed
    ]
*output paths:*

    # corresponding output folder for each .blend file, make sure they are correct

    output_directories = [  
        r"C:\path\to\your\output\location",  # ensure the folder is empty to avoid overwriting existing files
      # r"C:\path\to\your\output\location2",
        # ... 
        # add needed output location for each .blend file
    ]

*delay variables & framerate:*

    frame_delay = 10  # delay (in seconds) before rendering next frame of animation
    file_delay = 60  # delay (in seconds) before processing next .blend file
    frame_rate = 60  # frame rate (frames per second) for the final video output

*FFmpeg output settings:*

    ffmpeg_command = [  # customizable ffmpeg output
            "ffmpeg",
            "-framerate", str(frame_rate),
            "-i", input_pattern,
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            output_video
        ]

*If you don’t want the FFmpeg conversion step, you can comment out the following lines:*

    print(f"Finished rendering {blend_file}. Creating video from rendered frames.")
    create_video_from_frames(output_directory, frame_rate)

Before rendering, I recommend to make sure all your `Render Properties` inside the `.blend` files are adjusted how you want them to be.

## Execution

Once adjusted and saved, open cmd and:
- navigate to location where you saved `render.py` using `cd`,
- Run the following command:
    
        "D:\Program Files (x86)\Steam\steamapps\common\Blender\blender.exe" --background --python render.py

change `"D:\...\blender.exe"` path to where your `blender.exe` is if required.

Now sit back and let the animations render! :D

(*In case you want to manually create video using FFmpeg, go where you have your rendered frames using terminal and run the following:* 
    
    ffmpeg -framerate 60 -i frame_%04d.png -c:v libx264 -pix_fmt yuv420p output.mp4
)

## Additional Tips 

- check if `Cycles Render Devices` are set how you want them to be

- play around with `Noise thershold` and `Max samples` values,
    
    - `Noise thershold` at 0.2 and 
    - `Max samples` at 200 

    seems to do the job for most renders, reducing overworking of the GPU and saving time.
- for Laptop Users with powerful GPU: 
    - Power Mode set to `best battery life` mode and
    - changing `Maximum processor state` under Processor power management settings (I set it to around 72%)
    
    can  drastically reduce overheating and overworking issues.
