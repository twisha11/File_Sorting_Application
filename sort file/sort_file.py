from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os, shutil


class Sorting_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Arrange File")
        self.root.geometry("1350x690+0+0")

        self.logo_icon = PhotoImage(file="img/f1.png")

        self.fst_lbl = Label(self.root, text="Files Sorting Application", image=self.logo_icon, compound=LEFT,
                             bg="#850962", fg="white", anchor="w", font=('times new roman', 40, 'bold'))
        self.fst_lbl.pack(fill=X)

        # -----------------------
        lbl_select = Label(self.root, text="Select Path:", font=('times new roman', 20, 'bold'))
        lbl_select.place(x=100, y=100)

        self.var_folder = StringVar()
        self.txt_select = Entry(self.root, state='readonly', textvariable=self.var_folder,
                                font=('times new roman', 20, 'bold'), width=55)
        self.txt_select.place(x=250, y=100)

        brw_btn = Button(self.root, text="Browser", bg="black", fg="white", font=('times new roman', 20, 'bold'),
                         cursor="hand2", activebackground="#4a4a48", activeforeground="white", command=self.browse)
        brw_btn.place(x=1040, y=97, width=150, height=40)

        hr_line = Label(self.root, bg='lightgray')
        hr_line.place(x=50, y=160, height=2, width=1250)

        # -----------------------
        self.img_extention = ["image", ".png", ".jpg", ".gif", ".jfif", ".webp", ".JPG", ".PNG", ".GIF"]
        self.audio_extention = ["audio", ".amr", ".mp3"]
        self.video_extention = ["video", ".mp4", ".avi", ".mpeg4", ".3gp"]
        self.doc_extention = ["document", ".doc", ".docx", ".ppt", ".xlsx", ".pptx", ".zip",
                              ".rar", ".pdf", ".txt", ".PPT", ".RAR", "DOC", ".ZIP"]
        self.folders = {"image": self.img_extention,
                        "audio": self.audio_extention,
                        "video": self.video_extention,
                        "document": self.doc_extention}

        # lbl_extention = Label(self.root, text="Various Support Extension:", font=('times new roman', 20, 'bold'))
        # lbl_extention.place(x=100, y=170)
        #
        # self.img_box = ttk.Combobox(self.root, values=self.img_extention, font=('times new roman', 15),
        #                             state="readonly", justify=CENTER)
        # self.img_box.current(0)
        # self.img_box.place(x=100, y=210)
        #
        # self.audio_box = ttk.Combobox(self.root, values=self.audio_extention, font=('times new roman', 15),
        #                               state="readonly", justify=CENTER)
        # self.audio_box.current(0)
        # self.audio_box.place(x=400, y=210)
        #
        # self.video_box = ttk.Combobox(self.root, values=self.video_extention, font=('times new roman', 15),
        #                               state="readonly", justify=CENTER)
        # self.video_box.current(0)
        # self.video_box.place(x=700, y=210)
        #
        # self.doc_box = ttk.Combobox(self.root, values=self.doc_extention, font=('times new roman', 15),
        #                             state="readonly", justify=CENTER)
        # self.doc_box.current(0)
        # self.doc_box.place(x=1000, y=210)

        # --------------------

        self.img_icon = PhotoImage(file="img/Image.png")
        self.audio_icon = PhotoImage(file="img/audio.png")
        self.video_icon = PhotoImage(file="img/video1.png")
        self.doc_icon = PhotoImage(file="img/Document1.png")
        self.other_icon = PhotoImage(file="img/question.png")

        frame1 = Frame(self.root, relief=RIDGE, bg="white", bd=2)
        frame1.place(x=60, y=250, width=1230, height=300)

        self.lbl_t = Label(frame1, font=('times new roman', 20), text="Total Files :", bg="white")
        self.lbl_t.place(x=30, y=20)

        self.img_lbl = Label(frame1, image=self.img_icon,
                             compound=TOP, font=('times new roman', 15), bd=2, relief=RAISED)
        self.img_lbl.place(x=30, y=70, width=200, height=210)

        self.audio_lbl = Label(frame1, bd=2, relief=RAISED, image=self.audio_icon,
                               compound=TOP, font=('times new roman', 15))
        self.audio_lbl.place(x=270, y=70, width=200, height=210)

        self.video_lbl = Label(frame1, bd=2, relief=RAISED, image=self.video_icon,
                               compound=TOP, font=('times new roman', 15))
        self.video_lbl.place(x=510, y=70, width=200, height=210)

        self.doc_lbl = Label(frame1, bd=2, relief=RAISED, image=self.doc_icon,
                             compound=TOP, font=('times new roman', 15))
        self.doc_lbl.place(x=750, y=70, width=200, height=210)

        self.help_lbl = Label(frame1, bd=2, relief=RAISED, image=self.other_icon,
                              compound=TOP, font=("times new roman", 15))
        self.help_lbl.place(x=990, y=70, width=200, height=210)

        # ------------------

        lbl1 = Label(self.root, text="Status", font=('times new roman', 20, 'bold'))
        lbl1.place(x=100, y=580)

        self.lbl2 = Label(self.root, text=" ", font=('times new roman', 18, 'bold'), fg="green")
        self.lbl2.place(x=300, y=580)

        self.lbl3 = Label(self.root, text=" ", font=('times new roman', 18, "bold"), fg="blue")
        self.lbl3.place(x=500, y=580)

        self.lbl4 = Label(self.root, text=" ", font=('times new roman', 18, 'bold'), fg="red")
        self.lbl4.place(x=700, y=580)

        self.clr_btn = Button(self.root, text="Clear", bg="orange", font=('times new roman', 20, 'bold'),
                              cursor="hand2", activebackground="orange", command=self.clear)
        self.clr_btn.place(x=900, y=580, width=150, height=40)

        self.start_btn = Button(self.root, text="Start", state=DISABLED, bg="green", fg="white",
                                font=('times new roman', 20, 'bold'),
                                cursor="hand2", activebackground="green", activeforeground="white",
                                command=self.start_fun)
        self.start_btn.place(x=1100, y=580, width=150, height=40)

    def total_count(self):
        image = 0
        audio = 0
        video = 0
        document = 0
        other = 0
        self.count = 0
        cmbine_list = []

        for i in self.all_file:
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                self.count += 1
                ext = "." + i.split(".")[-1]
                for folder_name in self.folders.items():
                    # print(folder_name)
                    for x in folder_name:
                        cmbine_list.append(x)

                    if ext.lower() in folder_name[1] and folder_name[0] == "image":
                        image += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "audio":
                        audio += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "video":
                        video += 1
                    if ext.lower() in folder_name[1] and folder_name[0] == "document":
                        document += 1
        for i in self.all_file:
            if os.path.isfile(os.path.join(self.directry, i)) == True:
                ext = "." + i.split(".")[-1]
                if ext.lower() not in cmbine_list:
                    other += 1
        self.img_lbl.config(text="All Image\n" + str(image))
        self.audio_lbl.config(text="All Audio\n" + str(audio))
        self.video_lbl.config(text="All Video\n" + str(video))
        self.doc_lbl.config(text="All document\n" + str(document))
        self.help_lbl.config(text="Other Files\n" + str(other))
        self.lbl_t.config(text="Total Files: " + str(self.count))

    def browse(self):
        op = filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op != None:
            self.var_folder.set(str(op))
            self.directry = self.var_folder.get()
            self.other_name = "other"
            self.rename_folder()
            self.all_file = os.listdir(self.directry)
            # length = len(self.all_file)
            # count = 1
            self.total_count()
            self.start_btn.config(state=NORMAL)

    def start_fun(self):
        if self.var_folder.get() != "":
            self.clr_btn.config(state=DISABLED)

            count1 = 0
            for i in self.all_file:
                if os.path.isfile(os.path.join(self.directry, i)) == True:
                    count1 += 1
                    self.create_move(i.split(".")[-1], i)
                    self.lbl2.config(text="Total : " + str(self.count))
                    self.lbl3.config(text="moved : " + str(count1))
                    self.lbl4.config(text="Left : " + str(self.count - count1))

                    self.lbl2.update()
                    self.lbl3.update()
                    self.lbl4.update()
                # print(f"Total Files: {length}|Done:{count}|Left:{length - count}")

            messagebox.showinfo("success", "Work done successfully")
            self.start_btn.config(state=DISABLED)
            self.clr_btn.config(state=NORMAL)
        else:
            messagebox.showerror("Error", "Please select file")

    def clear(self):
        self.start_btn.config(state=DISABLED)
        self.var_folder.set("")
        self.lbl2.config(text="")
        self.lbl3.config(text="")
        self.lbl4.config(text="")
        self.img_lbl.config(text="")
        self.audio_lbl.config(text="")
        self.video_lbl.config(text="")
        self.doc_lbl.config(text="")
        self.help_lbl.config(text="")

    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry, folder)):
                os.rename(os.path.join(self.directry, folder), os.path.join(self.directry, folder.lower()))

    def create_move(self, ext, file_name):
        global find
        find = False
        for folder_name in self.folders:
            if "." + ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry, folder_name))
                shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, folder_name))
                find = True
                break
        if find != True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry, self.other_name))
            shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, self.other_name))


root = Tk()
obj = Sorting_App(root)
root.mainloop()
