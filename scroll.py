from tkinter import *

root = Tk()
root.title("Scrollable Frame")
root.geometry("800x600")

#add a canvas
canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

#add the scrollbar
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

#mousethingies ig. ne. eigentlich nicht. bwah
#iguess tell the canvas to scroll using the scrollbar? scroll. scroll. scrool. scccroolllll. scrooll. scroll.
canvas.configure(yscrollcommand=scrollbar.set)

#create the frame that will actually be scrolled
scrollable_frame = Frame(canvas)
#bind the frame into the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#do the scroll logic....????????????????????
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

for i in range(30):
    Label(scrollable_frame, text=f"Item {i+1}", width=20).pack(pady=5)

root.mainloop()
