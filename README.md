# Installation

Using the pyproject.toml

```$ python3 -m pip install .```


# Example use 

The user must define two objects before use:

1) world
User-defined class instance that all states have access to.
Must have at least an .update() method.
This typically holds the observations of the world (e.g. last sensor values).
The values in "world" that are used by the states MAY NOT CHANGE during 
state execution. Hence the update method could ensure that the latest sensor
readings are copied to an attribute that stays constant during state execution.

2) state_object
User-defined state with related actions. Must be a subclass of 
state_machine.StateActionBase. The guard method must be updated with a condition
that allows state entry (upon True).

```
import state_machine as sm

# Create a user-defined world model
# Not part of this package: can be anything the states must have access to
world = WorldModel()

machine = sm.StateMachine(world)
machine.add_state(name="state_1", state_object=StateObject(world))
machine.step()

```

