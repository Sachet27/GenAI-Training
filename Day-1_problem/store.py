import json

class Department:
    def __init__(self, name):
        self.name= name
        self.products= []
    def add_products(self, items: list[str]):
        self.products.extend(items)

    def to_dict(self):
        return {
            "name": self.name,
            "products": self.products
        }
    
    @classmethod
    def from_dict(cls, dept_json):
        dept= cls(dept_json["name"])
        dept.products= dept_json["products"]
        return dept


class Store:
    def __init__(self, name):
        self.name= name
        self.departments=[]
    
    def add_department(self, dep_name: str):
        self.departments.append(Department(dep_name))

    def add_products(self, dep_name, products: list[str]):
        depts= [dept.name for dept in self.departments]
        dep_index= depts.index(dep_name)
        self.departments[dep_index].add_products(products) 

    def to_dict(self):
        return {
            "name": self.name,
            "departments": [dept.to_dict() for dept in self.departments]
        }
    
    @classmethod
    def from_dict(cls, store_json):
        store= cls(store_json["name"]) 
        store.departments= [Department.from_dict(dept) for dept in store_json["departments"]]
        return store
    
    
class User:
    def __init__(self, name):
        self.name= name
        self.cart= []

    def add_to_cart(self, store: Store, items: list[str]):
        for item in items:
            found= False
            for department in store.departments:
                if item in department.products:
                    self.cart.append(item)
                    found= True
                    break
            if not found:
                print(f"{item} isnt available in {store.name}")
    
    def checkout(self):
        print(f"{self.name} checked out:")
        for item in self.cart:
            print(item)
            

        
def main():
    with open('store_data.json', 'r') as file:
        store_data= json.load(file)
        store= Store.from_dict(store_data)
    
    user1= User("Sachet")
    user1.add_to_cart(store, ["makeup", "mouse", "keyboard", "blush"])
    user1.checkout()


if __name__== "__main__":
    main()


# Initial prep
# my_store= Store("Sachet shop")
# my_store.add_department("Cosmetics")
# my_store.add_department("Technology")
# my_store.add_department("Furniture")
# my_store.add_products("Cosmetics", ["makeup", "blush"])
# my_store.add_products("Technology", ["laptop", "mouse"])
# with open('store_data.json','w') as file:
#     json.dump(obj= my_store.to_dict(), fp= file, indent= 4)
    