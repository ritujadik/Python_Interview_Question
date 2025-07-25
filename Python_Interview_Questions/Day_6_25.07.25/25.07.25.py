"""
Ques-1 what is GIL in python and how does it affect threading in python?
Answer The GIL ensures only one thread exectutes Python bytecode at a time in a python process,
even if there is multiple threads.This is not true parallelism.instead the GIL switches control between
threads periodically,allowing each thread to run for a short time.
This enable python to handle I/O-bound threads concurrently but it limits performance for CPU-bound multithreading
Python threads run concurrently but not in parallel due to GIL

Que-2 When would you choose asyncio over threading?
Answer: I would choose asyncio over threading when i am dealing with I/O bound operations that involve waiting,such as network request,
reading/writing files or database queries specially when we need to perform so many task concurrently
it is more effeicient and single threaded event loop to manage multiple tasks without the overhead of creating and switching
between multiple threads.it avoids the complications of thread and safety and GIL which limit the effectiveness of multithreading
in python
Exapmle-handling thousand of client connection in web browser.
building chatting apps

Que-3 what is the diiference between concurrency and parallelism
Answer: concurrency is the process where we switch from one task to another for excution while parallelism is something where all the
task perform simultaneously

Que-4 what is the event loop in asyncio?
Answer: Event loop is the main component who manage and run the asuynchronous task.it keeps track of all the task that are scheduled to run
 and it decides when each task should be executed,paused and resumed

Ques-5 what does await keyword in python
Answer: The await keyword in Python is used inside an async function to pause the execution of that function until the awaited asynchronous operation is complete.
It tells the event loop: “Pause here, let other tasks run, and come back when the result is ready.”

Question-6 What is the difference between async def and a regular def function?
Answer: The main difference is that an async def function defines a coroutine, while a regular def function defines a normal (synchronous) function.
An async def function does not run immediately when called — instead, it returns a coroutine object that must be awaited or scheduled in an event loop to actually execute.
A regular def function executes immediately when called and runs from start to finish without pausing.

Question-7 Can you run CPU-bound tasks efficiently using asyncio? Why or why not?
Answer: No it is more effective for I/O bound task,such as file I/O, network requests, or database calls.
CPU-bound tasks require heavy computation, which blocks the single-threaded asyncio event loop, preventing it from switching between tasks. This defeats the purpose of asynchronous concurrency.

Question-8 what is coroutes in python?
Answer:A coroutine in python is a special type of function that can pause and resume its execution,allowing other tasks to run while it waits.
Coroutine are defined using async def and they are builiding blocks of asynchronous code.

Question-9 How can you run multiple asynchronous functions concurrently using asyncio?
Answer To run mutilple asynchronous function concurrently in asyncio we can use asyncio.gather() or creating a tasks using asyncio.create_task()
these methods allow multiples coroutines to run at the same time without waiting for each one to finish before starting the next.

Ex-
 import asyncio
  async def task1():
     await asyncio.sleep(1)
     print("task1 done")

  async def task2():
     await asyncio.sleep(2)
     print("task2 done")

  async def main():
     await asyncio.gather(task1(),task2())

  asyncio.run(main())

Question-10


"""