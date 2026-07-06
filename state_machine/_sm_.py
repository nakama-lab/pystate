"""
Generic state machine and state actions
"""

class WorldModelBase(object):
    """
    This is a stub.
    """
    def __init__(self):
        return

    def update(self):
        return


class StateActionBase(object):
    """
    Parent class for all state-action (sub)classes
    """

    def __init__(self, world_model):
        """
        Parent class for all state-action (sub)classes
                
        =INPUT=
            world_model - class instance
                See docstring of StateMachine
        """
        self.world = world_model
        return
    
    def guard(self):
        """
        State entry is possible when returns True
        """
        return False
    
    def on_entry(self):
        """
        Executed once, upon entry from another state
        """
        return
    
    def update(self):
        """
        Executed for as long as in this state
        """
        return
    
    def on_exit(self):
        """
        Executed once, upon exit to another state
        """
        return


class StateMachine(object):
    """
    Generic state machine
    """

    def __init__(self, world_model):
        """
        =INPUT=
            world_model - class instance
                Instance of user-defined WorldModel class. All instances of
                StateActionBase must gain access to the same world_model instance.
                The world_model instance must have at least an .update() method
                that takes no inputs. This method may copy the latest sensor
                values to attributes of world_model, to remain constant during
                the execution of a state action.
        """

        self.world = world_model
        self.state_actions = {}
        self.current_state = None
        return
    

    def add_state(self, state_name, state_object):
        """
        Add state and related actions to state machine.
        The first added state will also be the initial state.

        =INPUT=
            state_name - string
            state_objects - class instance
                Instance of (a subclass of) StateActionBase.
        """
        self.state_actions.update({state_name, state_object})
        if self.current_state is None:
            self.current_state = state_name
        return


    def remove_state(self, state_name):
        """
        =INPUT=
            state_name - string
        """
        if state_name in self.state_actions.keys():
            del self.state_actions[state_name]
        return


    def step(self):
        """
        To be executed every time step
        Calls .update() of world model before executing a state step.

        # ASSUMPTIONS
            Only one guard can be true at a time. If two evaluate to true,
            the state of the first evaluated one is entered.
        """

        # Update world model to act on
        self.world.update()

        # Check all guards. It is assumed at most 1 gaurd can be true at a time.
        # Arbitration is left to the state definitions. Not resolved here.
        for state_name, state_object in self.state_actions.items():            
            
            if state_object.guard():

                # Perform exit action of previous state
                self.state_actions[self.current_state].on_exit()

                # Perform transition
                self.status.current_state = state_name

                # Execute entry action of new state
                self.state_actions[self.current_state].on_entry()

                break
            
        # Execute the action of the current state
        self.state_actions[self.current_state].update()

        return