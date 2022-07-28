from BaseGraph import *

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

class FamilyTree:
    def __init__(self):
        self.family_tree = Graph()

    def add_member(self, name, gender, age):
        node = Person(name, gender, age)
        return self.family_tree.add_node(node)

    def add_relationship(self, new_member, existing_member, relationship):
        # check if exist
        if not self.family_tree.checkIfExists(new_member):
            return f'{new_member.name} does not exist'
        if not self.family_tree.checkIfExists(existing_member):
            return f'{existing_member.name} does not exist'

        # TODO: add data assertion.
        if new_member == existing_member:
            return "Cannot have a relationship to yourself"
        if relationship == "Married" and min(new_member.age, existing_member.age) < 18:
            return "Cannot get married if people are under 18 years old"
        if relationship == "Married":
            if len(self.family_tree.graph[existing_member]) > 0:
                for conn in self.family_tree.graph[existing_member]:
                    if conn[0] == new_member and \
                        conn[1] in (RelationshipTypes.Parent_AdoptedOffspring.value, RelationshipTypes.Parent_Offspring.value, RelationshipTypes.Sibling.value):
                        return "Cannot get married if people are in adopted, offspring, sibling relationships"
            if len(self.family_tree.graph[new_member]) > 0:
                for conn in self.family_tree.graph[new_member]:
                    if conn[0] == existing_member and \
                        conn[1] in (RelationshipTypes.Parent_AdoptedOffspring.value, RelationshipTypes.Parent_Offspring.value, RelationshipTypes.Sibling.value):
                        return "Cannot get married if people are in adopted, offspring, sibling relationships"

        if relationship == RelationshipTypes.Parent_AdoptedOffspring.name and max(new_member.age, existing_member.age) < 18:
            return "Cannot adopt child if you are under 18"

        self.family_tree.add_edge(existing_member, new_member, relationship)
        return "Relationship added success!"

    def edit_member(self, member, new_member):
        return self.family_tree.edit_node(member, new_member)

    def edit_relationship(self, first_member, second_member, new_relationship):
        return self.family_tree.edit_edge(first_member, second_member, new_relationship)

    def delete_member(self, member):
        return self.family_tree.delete_node(member)

    def delete_relationship(self, first_member, second_member):
        return self.family_tree.delete_edge(first_member, second_member)

def main():

    can_continue = True
    while can_continue:
        print("""Pick one of numbers to start:" 
              1. add new member 
              2. edit member
              3. delete member
              4. add new relationship
              5. edit relationship
              6. delete relationship
              7. print all family members
              """
              )
        answer = input()
        if not answer.isdigit():
            print("wrong input")
            return

        if int(answer) == 1:
            # add new member
            list = insert_member_info()
            print(list)
            print(ft.add_member(list[0], list[1], list[2]))

        elif int(answer) == 2:
            # edit member
            print("Please insert old member's name, gender, age")
            old_member_info = insert_member_info()
            old_member = Person(old_member_info[0], old_member_info[1], old_member_info[2])
            if ft.family_tree.checkIfExists(old_member):
                old_person = ft.family_tree.find_person_in_FamilyTree(old_member)
            else:
                print(f"{old_member.name} not found")
                return
            print("Please insert new member's name, gender, age")
            new_member_info = insert_member_info()
            new_member = Person(new_member_info[0], new_member_info[1], new_member_info[2])
            print(ft.edit_member(old_person, new_member))

        elif int(answer) == 3:
            # delete member
            print("Please insert member's name, gender, age you want to delete")
            delete_member_info = insert_member_info()
            delete_member = Person(delete_member_info[0], delete_member_info[1], delete_member_info[2])
            if ft.family_tree.checkIfExists(delete_member):
                delete_person = ft.family_tree.find_person_in_FamilyTree(delete_member)
            else:
                print(f"{delete_member.name} not found")
                return
            print(ft.delete_member(delete_person))

        elif int(answer) == 4:
            # add relationship
            print("Please insert first member's name, age, gender")
            member1_info = insert_member_info()
            member1 = Person(member1_info[0], member1_info[1], member1_info[2])
            print("Please insert second member's name, age, gender")
            member2_info = insert_member_info()
            member2 = Person(member2_info[0], member2_info[1], member2_info[2])
            relationship = insert_relationship_type()
            if ft.family_tree.checkIfExists(member1):
                found_member1 = ft.family_tree.find_person_in_FamilyTree(member1)
            else:
                print(f"{member1.name} not found")
                return
            if ft.family_tree.checkIfExists(member2):
                found_member2 = ft.family_tree.find_person_in_FamilyTree(member2)
            else:
                print(f"{member2.name} not found")
                return
            print(ft.add_relationship(found_member1, found_member2, relationship))

        elif int(answer) == 5:
            # edit relationship
            print("Please insert first member's name, age, gender")
            member1_info = insert_member_info()
            member1 = Person(member1_info[0], member1_info[1], member1_info[2])
            print("Please insert second member's name, age, gender")
            member2_info = insert_member_info()
            member2 = Person(member2_info[0], member2_info[1], member2_info[2])
            relationship = insert_relationship_type()
            if ft.family_tree.checkIfExists(member1):
                found_member1 = ft.family_tree.find_person_in_FamilyTree(member1)
            else:
                print(f"{member1.name} not found")
                return
            if ft.family_tree.checkIfExists(member2):
                found_member2 = ft.family_tree.find_person_in_FamilyTree(member2)
            else:
                print(f"{member2.name} not found")
                return
            print(ft.edit_relationship(found_member1, found_member2, relationship))

        elif int(answer) == 6:
            # delete relationship
            print("Please insert first member's name, age, gender")
            member1_info = insert_member_info()
            member1 = Person(member1_info[0], member1_info[1], member1_info[2])
            print("Please insert second member's name, age, gender")
            member2_info = insert_member_info()
            member2 = Person(member2_info[0], member2_info[1], member2_info[2])
            if ft.family_tree.checkIfExists(member1):
                found_member1 = ft.family_tree.find_person_in_FamilyTree(member1)
            else:
                print(f"{member1.name} not found")
                return
            if ft.family_tree.checkIfExists(member2):
                found_member2 = ft.family_tree.find_person_in_FamilyTree(member2)
            else:
                print(f"{member2.name} not found")
                return

            print(ft.delete_relationship(found_member1, found_member2))
        elif int(answer) == 7:
            for person in ft.family_tree.graph.keys():
                print(f"key person: {vars(person)}")
                for conn in ft.family_tree.graph[person]:
                    print(f"relationship list: {vars(conn[0])}, {conn[1]}")
        else:
            print("Wrong input")
            return

        print("Do you want to start another operation? reply 'Yes' or 'No'. ")
        continue_answer = input()
        if continue_answer.lower() == 'yes':
            can_continue = True
        else:
            can_continue = False


def insert_member_info():
    print("Please insert member's name:")
    name = input()
    wrong_gender_input = True
    while wrong_gender_input:
        print("Please select member's gender, Male insert 1, Female insert 2.")
        gender = input()
        global gender_name
        if int(gender) == 1:
            gender_name = "Male"
            wrong_gender_input = False
        elif int(gender) == 2:
            gender_name = "Female"
            wrong_gender_input = False
        else:
            wrong_gender_input = True
            print("Wrong input")
    wrong_age_input = True
    while wrong_age_input:
        print("please insert member's age:")
        age = input()
        wrong_age_input = False
        if not age.isdigit():
            wrong_age_input = True
            print("Wrong input")
    return [name, gender_name, int(age)]

def insert_relationship_type():
    wrong_relationship_type = True
    while wrong_relationship_type:
        print("""
                Please choose their relationship:
                1. Married 
                2. Divorced
                3. Sibling 
                4. Parent and Offspring 
                5. Parent and AdoptedOffspring      
                """)
        type = input()
        global type_name
        if int(type) == 1:
            type_name = "Married"
            wrong_relationship_type = False
        elif int(type) == 2:
            type_name = "Divorced"
            wrong_relationship_type = False
        elif int(type) == 3:
            type_name = "Sibling"
            wrong_relationship_type = False
        elif int(type) == 4:
            type_name = "Parent_Offspring"
            wrong_relationship_type = False
        elif int(type) == 5:
            type_name = "Parent_AdoptedOffspring"
            wrong_relationship_type = False
        else:
            print("Wrong input")
            wrong_relationship_type = True

    return type_name

def add_family_members():
    # family 1
    patrick = ft.add_member("Patrick Earnshaw", "Male", 63)
    hannah = ft.add_member("Hannah Earnshaw", "Female", 62)
    ft.add_relationship(patrick, hannah, "Married")
    catherine = ft.add_member("Catherine Earnshaw", "Female", 41)
    hindley = ft.add_member("Hindley Earnshaw", "Male", 26)
    ft.add_relationship(catherine, hindley, "Sibling")
    ft.add_relationship(catherine, patrick, "Parent_Offspring")
    ft.add_relationship(catherine, hannah, "Parent_Offspring")
    ft.add_relationship(hindley, patrick, "Parent_Offspring")
    ft.add_relationship(hindley, hannah, "Parent_Offspring")

    #family 2
    andrew = ft.add_member("Andrew Linton", "Male", 64)
    dolores = ft.add_member("Dolores Linton", "Female", 54)
    ft.add_relationship(andrew, dolores, "Divorced")
    isabella = ft.add_member("Isabella Linton", "Female", 30)
    edgar = ft.add_member("Edgar Linton", "Male", 37)
    heathcliff = ft.add_member("Heathcliff Linton", "Male", 22)
    ft.add_relationship(isabella, edgar, "Sibling")
    ft.add_relationship(isabella, heathcliff, "Sibling")
    ft.add_relationship(edgar, heathcliff, "Sibling")
    ft.add_relationship(isabella, andrew, "Parent_Offspring")
    ft.add_relationship(isabella, dolores, "Parent_Offspring")
    ft.add_relationship(edgar, andrew, "Parent_Offspring")
    ft.add_relationship(edgar, dolores, "Parent_Offspring")
    ft.add_relationship(heathcliff, andrew, "Parent_AdoptedOffspring")
    ft.add_relationship(heathcliff, dolores, "Parent_AdoptedOffspring")

    # family 3
    frances = ft.add_member("Frances Byler", "Male", 27)
    ft.add_relationship(hindley, frances, "Married")
    hareton = ft.add_member("Hareton Earnshaw", "Male", 19)
    ft.add_relationship(hareton, hindley, "Parent_AdoptedOffspring")
    ft.add_relationship(hareton, frances, "Parent_AdoptedOffspring")

    #family 4
    ft.add_relationship(catherine, edgar, "Married")
    cathy = ft.add_member("Cathy Linton", "Female", 20)
    ft.add_relationship(cathy, catherine, "Parent_Offspring")
    ft.add_relationship(cathy, edgar, "Parent_Offspring")

    #family 5
    linton = ft.add_member("Linton Heathcliff", "Male", 18)
    ft.add_relationship(linton, isabella, "Parent_Offspring")
    #family 6
    ft.add_relationship(linton, heathcliff, "Parent_Offspring")

    # family 7
    ft.add_relationship(hareton, cathy, "Married")
    #family 8
    ft.add_relationship(cathy, linton, "Divorced")



if __name__ == '__main__':
    ft = FamilyTree()
    add_family_members()
    main()






