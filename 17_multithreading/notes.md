# Topic 18: Multi-threading

## Process vs thread
| | Process | Thread |
|---|---|---|
| Memory | | |
| Cost | | |
| Best for | | |
| Python tools | | |

## The GIL
(What it is, when it is released, what it means for I/O-bound vs CPU-bound code)

## Creating threads
(target/args/kwargs, subclassing, start vs run, join, daemon)

## Thread methods
| Member | Meaning |
|---|---|

## Race conditions
(What is a race? Why is counter += 1 not safe? How does a Lock fix it?)

## Synchronization tools
| Tool | Purpose | Example use |
|---|---|---|
| Lock | | |
| RLock | | |
| Semaphore | | |
| Event | | |
| Condition | | |
| Barrier | | |
| Queue | | |

## Deadlock
(Four conditions, the ordering fix, timeouts)

## ThreadPoolExecutor
(submit, map, as_completed, futures, exceptions)

## Threads and Tkinter
(Why widgets are main-thread only. The queue + after() pattern.)

## Which to choose
| Task | Choose |
|---|---|

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have


What is the difference between a process and a thread?
What is the GIL, and why does it exist?
When do threads speed up a Python program, and when do they not?
What is the difference between start() and run()?
What does join() do, and what does join(timeout) guarantee?
What is a daemon thread?
What is a race condition? Give an example.
What is the difference between Lock and RLock?
What is a deadlock, and how do you avoid one?
When would you use a Semaphore, an Event, or a Queue?
What is the difference between ThreadPoolExecutor and ProcessPoolExecutor?
Why can’t a worker thread update a Tkinter widget directly, and what do you do instead?
Why does multiprocessing on Windows need if __name__ == "__main__":?
What happens to an exception raised in a thread?