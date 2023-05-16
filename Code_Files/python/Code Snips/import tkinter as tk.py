import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x200")
        self.master.title("Modded Minecraft Servers Menu")
        self.create_widgets()

    def create_widgets(self):
        self.server1_button = tk.Button(self.master, text="Server 1", command=self.start_server1)
        self.server1_button.pack()

        self.server2_button = tk.Button(self.master, text="Server 2", command=self.start_server2)
        self.server2_button.pack()

        self.server3_button = tk.Button(self.master, text="Server 3", command=self.start_server3)
        self.server3_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack()

    def start_server1(self):
        subprocess.Popen(["java", "-Xms2G", "-Xmx4G", "-jar", "forge-1.16.5-36.2.8.jar", "--nogui"])

    def start_server2(self):
        subprocess.Popen(["java", "-Xms2G", "-Xmx4G", "-jar", "forge-1.15.2-31.2.47.jar", "--nogui"])

    def start_server3(self):
        subprocess.Popen(["java", "-Xms2G", "-Xmx4G", "-jar", "fabric-1.17-37.0.1.jar", "--nogui"])

root = tk.Tk()
app = Application(master=root)
app.mainloop()