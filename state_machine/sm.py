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
    Template class for all state-action classes
    """

    def __init__(self, world_model):
        self.world = world_model
        return
    
    def guard(self):
        return False
    
    def on_entry(self):
        return
    
    def update(self):
        return
    
    def on_exit(self):
        return


class StateMachine(object):
    """
    Generic state machine
    """

    def __init__(self, world_model):
        """
        =INPUT=
            world_model - class instance
                Must contain an .update() method that updates the "world" state,
                after which it must remain fixed until the next update call.
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