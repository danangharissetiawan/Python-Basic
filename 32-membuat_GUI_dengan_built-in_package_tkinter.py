import tkinter

main_window = tkinter.Tk()


def even_tekan():
    label2 = tkinter.Label(main_window, text="akuh di tekan ^_^")
    label2.pack()


label = tkinter.Label(
    main_window, text="hallo, saya adalah \n Gui sederhana dengan \n built in package python")

tombol = tkinter.Button(main_window, text="tekan akuh", command=even_tekan)

label.pack()
tombol.pack()
main_window.mainloop()
