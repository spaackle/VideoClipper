import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox

class VideoClipper:

    def __init__(self, master):
        self.master = master
        master.title("Video Clipper")
        master.geometry("200x160")

        self.file_label = tk.Label(master, text="Select Video File:")
        self.file_label.pack()
        self.file_button = tk.Button(master, text="Choose File", command=self.choose_file)
        self.file_button.pack()

        self.start_label = tk.Label(master, text="Start Time (mm:ss):")
        self.start_label.pack()
        self.start_entry = tk.Entry(master)
        self.start_entry.pack()

        self.end_label = tk.Label(master, text="End Time (mm:ss):")
        self.end_label.pack()
        self.end_entry = tk.Entry(master)
        self.end_entry.pack()

        self.save_button = tk.Button(master, text="Save", command=self.save_clip)
        self.save_button.pack()

    def choose_file(self):
        self.video_file = filedialog.askopenfilename()

    def browse_output(self):
        # Sets the output folder
        self.output_folder = "C:\Clips"

    def save_clip(self):
        start_time = self.start_entry.get()
        end_time = self.end_entry.get()

        output_file = os.path.splitext(os.path.basename(self.video_file))[0] + "-output.mp4"
        output_file = os.path.join(self.output_folder, output_file)

        file_exists = os.path.exists(output_file)
        counter = 1

        while file_exists:
            output_file = os.path.splitext(os.path.basename(self.video_file))[0] + "-output" + str(counter) + ".mp4"
            output_file = os.path.join(self.output_folder, output_file)
            file_exists = os.path.exists(output_file)
            counter += 1

        command = ['ffmpeg', '-i', self.video_file, '-vcodec', 'h264_nvenc', '-ss', start_time, '-to', end_time, '-c', 'copy', output_file]

        os.system(' '.join(command))

        messagebox.showinfo("Video Clipper", "Clip saved as {}".format(output_file))

root = tk.Tk()
root.eval('tk::PlaceWindow . center')
app = VideoClipper(root)
app.browse_output()
root.mainloop()
