"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Robert Belk.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('Saying hello or goodbye!')

    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    btn = ttk.Button(frame1, text='Say Hello')
    btn.grid()
    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    btn['command'] = lambda: print('Hello!')

    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entry = ttk.Entry(frame1)
    entry.grid()

    btn2 = ttk.Button(frame1, text='Say Hello or Goodbye')
    btn2.grid()

    btn2['command'] = lambda: print_hello_or_goodbye(entry)

    entry2 = ttk.Entry(frame1)
    entry2.grid()

    btn3 = ttk.Button(frame1, text='Print your string')
    btn3.grid()

    btn3['command'] = lambda: print_string(entry, entry2)


    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    root2 = tkinter.Tk()
    root2.title('Answering Questions.')

    frame2 = ttk.Frame(root2, padding=20, )
    frame2.grid()

    inquiry = ttk.Entry(frame2)
    inquiry.grid()

    btn21 = ttk.Button(frame2, text='Hey Stranger!')
    btn21['command'] = lambda : responding(inquiry)
    btn21.grid()



    root.mainloop()
    root2.mainloop()


def print_hello_or_goodbye(entry):
    contents = entry.get()
    if contents == 'ok':
        print('Hello!')
    else:
        print('Goodbye!')


def print_string(string, n):
    number_of_times = int(n.get())
    contents = string.get()
    for k in range(number_of_times):
        print(contents)

def responding(saying):
    contents = saying.get()
    if contents == 'What is up?':
        print('The sky.')
    if contents == 'How are you?':
        print('I am fantastic!')

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
