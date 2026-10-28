# Topic 17: GUI Programming II

## Event handling
| | command= | bind |
|---|---|---|
| Callback gets | | |
| Fires on | | |
| Use for | | |

Event sequences I used:
Event attributes I used:

## bind, bind_all, and bindtags
(Order of callbacks. What "break" does. Most specific binding wins.)

## Virtual events
(Examples. What event_generate does.)

## after()
(Why animation and timers use it, not sleep or while loops)

## Dialogs
| Function | Returns | Cancelled returns |
|---|---|---|

## filedialog
(Four functions, filetypes, what cancel returns, paths on Windows)

## Images
(Formats plain Tk reads, PhotoImage methods, the reference trap, Pillow)

## Canvas
(Item ids, tags, create_*, move, coords, itemconfig, tag_bind)

## Menus
(Menu, add_command / checkbutton / radiobutton / cascade, accelerator vs binding, context menu)

## Closing a window
(protocol WM_DELETE_WINDOW, destroy vs quit)

## Apps I built and what each taught me
| App | Concepts it used |
|---|---|

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have



What is the difference between command= and bind()?
What does the event object contain? Name five attributes.
What does returning "break" from a binding do, and what is a bindtag?
How do you react to a windows close button?
Why does a Frame sometimes not receive key events?
What do messagebox.askyesno and askyesnocancel return?
What does askopenfilename return when the user cancels, and why does it matter?
Why does a PhotoImage sometimes not appear, and how do you fix it?
Which image formats does Tkinter read natively, and how do you show a JPEG?
What is a Canvas item id, and what are tags used for?
What is the difference between accelerator= on a menu item and a key binding?
Why must long work not run inside a callback, and which tools keep the window responsive?