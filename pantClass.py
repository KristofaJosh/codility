class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount_val):
        return self.price - (self.price * discount_val)


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary, pants_sold=None, total_sales = 0):
        if pants_sold is None:
            pants_sold = []

        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = pants_sold
        self.total_sales = total_sales

    def sell_pants(self, obj):
        self.pants_sold.append(obj)

    def calculate_sales(self):
        for item in self.pants_sold:
            self.total_sales += item.price
        return self.total_sales

    def display_sales(self):
        for item in self.pants_sold:
            print(f'color: {item.color}, waist_size: {item.waist_size}, length: {item.length}, price: {item.price}')

    def calculate_commission(self, percentage):
        return percentage * self.total_sales


pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
print(salesperson.first_name)
print(salesperson.last_name)
print(salesperson.employee_id)
print(salesperson.salary)
print(salesperson.pants_sold)
print(salesperson.total_sales)
salesperson.sell_pants(pants_one)
print(salesperson.pants_sold[0].color)
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

print(len(salesperson.pants_sold))


print(round(salesperson.calculate_sales(), 2))
print(round(salesperson.calculate_commission(.1), 2))

salesperson.display_sales()