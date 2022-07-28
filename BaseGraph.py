import enum

class RelationshipTypes(enum.Enum):
    Married = 1
    Divorced = 2
    Sibling = 3
    Parent_Offspring = 4
    Parent_AdoptedOffspring = 5


class Graph:
    def __init__(self):
        self.node = None
        #self.edge_list = []
        self.graph = dict()

    def add_node(self, node):
        if self.checkIfExists(node):
            return "Already added"
        self.graph[node] = []
        return node

    def add_edge(self, existing_node, new_node, relationship):
        if not self.checkIfExists(new_node):
            return f"Not found {new_node.name}"
        if not self.checkIfExists(existing_node):
            return f"Not found {existing_node.name}"

        self.graph[new_node].append((existing_node, RelationshipTypes[relationship].value))

        self.graph[existing_node].append((new_node, RelationshipTypes[relationship].value))
        return "Success"

    def edit_node(self, node, new_node):
        if not self.checkIfExists(node):
            return f"Not found {node.name}"

        relationship_lst = self.graph[node]
        del self.graph[node]
        self.graph[new_node] = relationship_lst
        # update object in other person's list
        for person in self.graph.keys():
            for conn in self.graph[person]:
                if conn[0] == node:
                    new_relationship_tuple = (new_node, conn[1])
                    self.graph[person].remove(conn)
                    self.graph[person].append(new_relationship_tuple)
        return "Success"

    def edit_edge(self, first_node, second_node, relationship):
        if not self.checkIfExists(first_node):
            return f"Not found {first_node.name}"
        if not self.checkIfExists(second_node):
            return f"Not found {second_node.name}"
        # update first node relationship list
        for connection in self.graph[first_node]:
            if connection[0] == second_node:
                new_relationship_tuple = (second_node, RelationshipTypes[relationship].value)
                self.graph[first_node].remove(connection)
                self.graph[first_node].append(new_relationship_tuple)

        # update second node relationship list
        for connection in self.graph[second_node]:
            if connection[0] == first_node:
                new_relationship_tuple = (first_node, RelationshipTypes[relationship].value)
                self.graph[second_node].remove(connection)
                self.graph[second_node].append(new_relationship_tuple)
        return "Success"

    def delete_node(self, node):
        if not self.checkIfExists(node):
            return f"Not found {node.name}"
        # delete node relationships
        for conn in self.graph[node]:
            for subconn in self.graph[conn[0]]:
                if subconn[0] == node:
                    self.graph[conn[0]].remove(subconn)
                    break
        del self.graph[node]
        return "Success"

    def delete_edge(self, first_node, second_node):
        if not self.checkIfExists(first_node):
            return f"Not found {first_node.name}"
        if not self.checkIfExists(second_node):
            return f"Not found {second_node.name}"
        for conn in self.graph[first_node]:
            if conn[0] == second_node:
                self.graph[first_node].remove(conn)

        for conn in self.graph[second_node]:
            if conn[0] == first_node:
                self.graph[second_node].remove(conn)

        return "Success"

    # helper methods
    def checkIfExists(self, node):
        for person in self.graph.keys():
            if person.name.lower() == node.name.lower() and person.age == node.age and person.gender == node.gender:
                return True
        return False

    def find_person_in_FamilyTree(self, node):
        for person in self.graph.keys():
            if person.name.lower() == node.name.lower() and person.age == node.age and person.gender == node.gender:
                return person
        return None

