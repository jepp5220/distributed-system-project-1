# Bully Algorithm
# - Each node has an unique ID
# - Each node communicates with each other and broadcasts their ID
# - The node which has the highest ID becomes the leader.

# If P receives a Coordinator message, it treats the sender as the coordinator

# When any process notices that the coordinator is no longer responding to requests, it initiates an election.

# When to elect a coordinator
# - When the system


class Node:
    def __init__(self, pid, coordinator=False, leader_id=0):
        self.PID = pid
        self.coodinator = coordinator
        self.leader_id = 0

    def announce_victory(self, list_of_nodes):
        for node in list_of_nodes:
            node.leader_id = self.PID

    def check_coordinator(self):
        pass

        msg "foo"

        if not msg == "OK":
            self.election()

    def election(self):
        pass

    def respond(self):
        """ Respond with OK if alive """
        pass

    def is_leader(self):
        return self.leader


class Network:
    def __init__(self):
        self.counter = 0
        self.nodes = []  # list of nodes

    def attach(self, node):
        self.nodes.append(node)
        self.counter += 1

    def deattach(self, PID):
        if PID < self.counter:
            self.nodes.pop(PID)
            self.counter -= 1

    def initialize(self):

        # initialize system by finding a leader
        pass

    def tick(self):
        """Represent one logic progression in time"""
        for node in self.nodes:
            node.check_coordinator()


def main():
    nw = Network()
    nw.attach(Node(1))
    nw.attach(Node(2))
    # ....

    nw.initialize()

    # sdsd

    # need to test if the coordinator  in the system goes down
    # and when a node that is not the coordinator goes down


if __name__ == "__main__":
    main()
