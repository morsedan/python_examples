from category import Category

class Store:
    def __init__(self, name, categories=[]):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"Welcome to {self.name}!"
        i = 1
        for cat in self.categories:
            output += f"\n{i}. {cat.name}"
            i += 1

        return output

a_store = Store("Pet Store", [Category("Toys", ["chew toy", "cat nip", "ball"]),
                              Category("Fish"),
                              Category("Bedding/Cages"),
                              Category("Food") ])

print(a_store)
choice = int(input("Please choose a category (#): "))
print(choice)

# SHOULD add some error handling to our input parser
# ex. non-integer data, ints outside of (0-size_of_categories)
while choice != 0:
    print(a_store.categories[choice - 1])
    print(a_store)
    choice = int(input("Please choose a category (#): "))


print("Thanks for stopping by!")