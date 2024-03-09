# Introduction to Concurrency and Parallelism in Python

In the modern day, multi-core computers have become the norm, offering unprecedented processing power and performance. With the advent, and wide-spread adoption, of multi-core architectures, developers are now able to harness the full computational power of the hardware they develop on through concurrency and parallelism. 

As the demand for computational efficiency grows, a fundamental understanding of these concepts and what it can do for you has become an indispensable tool for developers and manager alike.

In this presentation, we'll explore the fundamentals of concurrency and parallelism in Python. By the end of which, you'll be equipped with the basic knowledge needed to begin developing scalable applications or overseeing the development thereof.

# Concurrency and Paralleism Defined

## Concurrency
- A conditions that exists when at least two threads are making progress. This is a more generalized form of parallelism that can include time-slicing as a form of virtual parallelization

### Put Simply

- Concurrency is essentially a form of rapid multi-tasking. The computer is not truly working on multiple tasks at the same time, but rather it's swapping between them quickly and giving them each a few milliseconds to make some progress. This is considered "Virtual Parallelization" because to the human, it would seem the computer is doing it all at the same time.

## Parallelism
- A condition that arises when at least two threads are executing simultaneously

### Put Simply
- Parallelism occurs when the computer is truly running tasks simultaneously. 

# Foundations of Concurrency and Parallelism

To begin understanding Concurrency and Parallelism, we must first understand some basic computer hardware architecture and software concepts.

## Hardware

At the heart of concurrency and paralleism lies the Central Processing Unit (CPU). Without a multi-core CPU architecture, none of what I'll be showing in this presentation is possible.

### The CPU

The CPU is the main processing unit of the computer, which is responsible for executing hardware and/or software instructions. In the context of this presentation, we will be giving the CPU instructions through the Python scripting language.

#### CPU Cores

A CPU is composed of at least one Processing Core. A core is the smallest physical unit of a CPU which is capable of executing instructions independently.

Most modern CPUs have more than one core, known as a multi-core CPU. Some common variations are Dual-Core (2 cores) and Quad-Core (4 cores).

** Side Note: You may also see cores referred to as threads or hardware threads. In the context of this presentation, I will refer to software threads as threads and hardware threads as cores. These are the threads we will be creating ourselves in code manually by leveraging some built-in Python utilities which we will cover later.

##### Physical vs Logical (or Virtual) Cores

When we begin to interact with Python to see how many cores a computer has, we will be faced with the concept of a Logical (also known as Virtual) Core and Physical Core.

Simply put, a Physical Core is an actual CPU Core built into the architecture of the CPU.

On the other hand, many modern CPUs provide support for Logical Cores through Hyperthreading. Hyperthreading enables a single CPU core to appear as two or more cores to the Operating System by providing some duplicated hardware architecture. This allows the core to process multiple commands in parallel, improving the overall CPU throughput. 

As an example, let's say we have a quad-core CPU. In terms of physical cores, we have 4 of them. However, let's assume this CPU supports Hyperthreading with 2 logical threads per core. Therefore, we could in theory run 8 tasks simultaneously.

I won't delve deeper into this as it's out of scope for the presentation, but it's important to know it exists.

## Software

Now that we understand some basic hardware architecture and it's terminology, we can move on to understanding the software side of concurrency and parallelism.

### Processes

A process is a software concept, and in the context of Operating Systems, you can simply think of them as any running instance of a program. They are the smallest unit of instructions which can be executed independently and are self encapsulating.

A process consists of the executable code instructions for the program, an allocation of memory, and some other resources.

Bringing it back to our hardware, a single CPU core can run a single process at a time. 

#### Processes and Python

Any time we run a Python script, by default it is assigned to a single process with a single thread of execution. Any standard Python script that does not explicitly utilize concurrency and/or parallelism will remain like this for the life of the program. This type of code is known as Sequential Code.

Beyond Python, this is how almost all popular programming languages operate.

### Threads

A thread is the smallest executable unit of instructions within a process. They cannot stand alone and share the same memory allocation and resources as all other threads in the parent process. 

##### Conceptualization of Processes and Threads

One way that I like to think about the relationship between processes and threads is to frame it in the context of an office.

We can think of a process as the entirety of the office. It's resources include the printers, computers, and other office supplies.

A thread can be thought of as an individual employee. They are the smallest unit of an office. They share the office resources with other employees and can only perform their job when given access to those resources.

You can have a small business with a single office (even a home office) and a single owner/operator, but that owner/operator cannot work without the resources provided by that office. Inversely, you can have a single office in a large corporation that still follows those same rules. 

![['images/Multithreaded_process.png]]

## Bringing it all back together

Now that we've covered some basic concepts of hardware and software, let's revisit Concurrency and Parallelism. 

### Concurrency

If you remember, we defined Concurrency as two threads making progress at the same time. 

Concurrency is possible via Multithreading, the use of multiple threads in a single parent process.

### Parallelism

We defined Parallelism as when two threads are making progress at the same time. Parallelism is possible through multiprocessing and multithreading, however it's only possible through multiprocessing in Python. We'll dive into why that is in a minute.

## Understanding Parallelism and Concurrency in Python

Now that we have the foundational understanding of computer architecture and software concepts needed to understand Concurreny and Parallelism, let's talk about some Python specific implementation details.

### Quick Python Introduction

Since Python is an interpreted language that is mainly built in C (unless you're using a different implementation), your code is read and converted to instructions for the CPU when you run the code. 

This is in contrast to interpreted languages, such as C/C++, which are compiled. Meaning you must build them as computer instructions before you run them.

In the context of Python, the Global Interpreter, which handles the conversion of Python code to byte code which can be processed by the CPU, is a crucial factor in Concurrency and Parallelism.

### The Global Interpreter Lock (GIL)

The Global Interpreter must be thread-safe. When we implement concurrency and/or parallelism in our program, we can run into various synchronization issues that can lead to unexpected and invalid behavior. 

As a solution to this, Python uses something called the Global Interpreter Lock (GIL). The GIL restricts true parallelism through threads in Python as it only allows one thread to have it's code interpreted as byte code and executed at a time. This is done using a Lock, which is known as a synchronization primitive. We'll cover this later. At the moment, all you need to understand is that a lock only allows one thread or process to acquire and use it at a time. 

The reason this prevents parallelism through threads is that each Python program in a process is given a single GIL. The upside of this is that we can still achieve true parallelism through the use of multiprocessing, the use of multiple processes. 
