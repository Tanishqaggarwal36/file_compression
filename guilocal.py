from tkinter import *
from compressmodule import compress,decompress
from tkinter import filedialog
def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title='Select a file to compress')
    return filename
def open_file1():
    filename=filedialog.askopenfilename(initialdir='/',title='Select a file to decompress')
    return filename
def compression(i,o):
    compress(i,o)
    output_entry.delete(0,END)
def decompression(i,o):
    decompress(i,o)
    o_entry.delete(0,END)
    
window=Tk()
window.title("Compression engine")
window.geometry("600x400")
bg=PhotoImage(file='compression.png')
Label(window,i=bg).pack()


output_entry=Entry(window,font=('Arial',12),bg="#A0CFEC").place(x=400,y=30)
output_label=Label(window,text="Name of the compressed file",bg="#EBF4FA",fg="#43ABC9",font=('Arial',20)).place(x=40,y=20)
o_entry=Entry(window,font=('Arial',12),bg="#A0CFEC").place(x=400,y=115)
o_label=Label(window,text="Name of the decompressed file",fg="#43ABC9",bg="#EBF4FA",font=('Arial',20)).place(x=10,y=100)


compress_button=Button(window,text="Compress",font=('Arial',12),fg="#3A5F0B",bg="#01F9C6",command=lambda: compression(open_file(),output_entry.get()))
decompress_button=Button(window,text="Decompress",font=('Arial',12),fg="#3A5F0B",bg="#01F9C6",command=lambda: decompression(open_file1(),o_entry.get()))
compress_button.place(x=400,y=60)
decompress_button.place(x=400,y=150)


window.mainloop()

