from tkinter import *
from compressmodule import compress,decompress
def compression(i,o):
    compress(i,o)
def decompression(i,o):
    decompress(i,o)
window=Tk()


window.title("Compression engine")
window.geometry("550x350")

bg=PhotoImage(file='compression.png')
Label(window,i=bg).place(x=0,y=0)


input_entry = Entry(window,font="Arial")
output_entry=Entry(window,font="Arial")
input_label=Label(window,text="File to be compressed",font="Arial",fg="blue")
output_label=Label(window,text="Name of the compressed file",font="Arial",fg="blue")
i_entry = Entry(window,font="Arial")
o_entry=Entry(window,font="Arial")
i_label=Label(window,text="File to be decompressed",font="Arial",fg="blue")
o_label=Label(window,text="Name of the decompressed file",font="Arial",fg="blue")

compress_button=Button(window,text="Compress",font="Arial",fg="green",command=lambda: compression(input_entry.get(),output_entry.get()))
decompress_button=Button(window,text="Decompress",font="Arial",fg="green",command=lambda: decompression(i_entry.get(),o_entry.get()))

input_label.grid(row=0,column=0)
input_entry.grid(row=0,column=1)
output_label.grid(row=1,column=0)
output_entry.grid(row=1,column=1)
i_label.grid(row=4,column=0)
i_entry.grid(row=4,column=1)
o_label.grid(row=5,column=0)
o_entry.grid(row=5,column=1)
compress_button.grid(row=2,column=1)
decompress_button.grid(row=6,column=1)

window.mainloop()

