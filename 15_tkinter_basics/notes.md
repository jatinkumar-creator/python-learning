# Topic 16: GUI Programming I (Tkinter)

## What Tkinter is
(Built in, wrapper over Tcl/Tk, event-driven, the five-step recipe)

## Widgets I used
| Widget | Purpose | Key options | How to read its value |
|---|---|---|---|
| Label | | | |
| Entry | | | |
| Text | | | |
| Button | | | |
| Frame / LabelFrame | | | |
| Checkbutton / Radiobutton | | | |
| Listbox | | | |

## Variables
| Class | Holds | Methods |
|---|---|---|
| StringVar | | |
| IntVar | | |
| DoubleVar | | |
| BooleanVar | | |

## Layout managers
| | pack | grid | place |
|---|---|---|---|
| Idea | | | |
| Options | | | |
| Best for | | | |

The golden rule about mixing them:

## Responsiveness
(Why time.sleep freezes the window, how after() fixes it, when threads are needed)

## Class-based apps
(Subclassing tk.Tk, why super().__init__(), Toplevel)

## tk vs ttk
(Differences)

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have


What is Tkinter, and what does mainloop() do?
What is the difference between Entry and Text? How do you read each one?
What are the three layout managers, and when do you use each?
Why cant you mix pack and grid in the same container, and how do you combine them anyway?
Why must a buttons command be func and not func()?
How do you pass an argument to a buttons command, and what is the late-binding trap in a loop?
What is a StringVar, and why use one instead of calling get() on the widget?
Why does time.sleep() freeze a Tkinter window, and what do you use instead?
What is a Frame for, and what does pack_propagate(False) do?
What is the difference between Tk and Toplevel?
What is the difference between tkinter and tkinter.ttk widgets?
Why does label = Label(root).pack() leave label as None?