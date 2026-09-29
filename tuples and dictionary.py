students_tuple = ("Jay", "Anvi", "Naina")

print("Original Tuple -", students_tuple)
students_tuple = students_tuple + ("Jainisha",)

change_tuple = list(students_tuple)

change_tuple[0] = "Harshita"

students_tuple = tuple(change_tuple)

temp_tuple = list(students_tuple)

temp_tuple.remove("Naina")

students_tuple = tuple(temp_tuple)

print("New Tuple -", students_tuple)
students_dict = {1: "Jay", 2: "Kabir", 3: "Naina"}

print("Original Dictionary -", students_dict)
students_dict[4] = "Jainisha"

students_dict[2] = "Anvi"

del students_dict[3]

print("New Dictionary -", students_dict)
