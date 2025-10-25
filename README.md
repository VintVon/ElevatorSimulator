# ElevatorSimulator
A Python-based elevator simulation using Tkinter that features animated movement, door control, and a prioritized floor queue system.

**Assumptions:**

Implemented a Tkinter GUI to visualize elevator behavior and simulate basic elevator operations

The elevator can service 5 floors, starting at floor 0, with the doors open

A basic building layout was created to represent floors and an elevator shaft

The elevator has a queue that optimizes itself based on the direction the elevator is moving 

The interface has an automatically updating information box with the following information fields: is the elevator moving, are the doors open, what direction the elevator is moving, what floor the elevator is on, and the queue of floors the elevator needs to visit

The elevator GUI has buttons that allow the user to input queue requests

The elevator features animated doors, opening and closing smoothly using step-based helper functions

Inter-floor movement is also smoothly animated for realistic behavior

The elevator logic is state-driven, meaning it only moves between floors when conditions allow (e.g., not already moving or doors open)


**Features not implemented: **

The number of floors is hardcoded; users cannot dynamically configure the number of floors. The simulation is not scalable for high-rise buildings.

There is only one set of floor buttons representing external calls; there is no separate interface for inside vs. outside elevator controls.

Multiple elevators were not implemented; this simulation is only for a single elevator, and coordination logic between multiple elevators was not implemented

There is no simulation of people or passenger logic; the elevator simulation simulates basic elevator operations and floor queue management.


