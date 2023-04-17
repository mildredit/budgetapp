
class Category:
  
    def __init__(self, name):
      self.name = name
      self.ledger = list()

    def __str__(self):
      title = f"{self.name:*^30}\n"
      items = ""
      total = 0
      for item in self.ledger:
        items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
        total += item['amount']
        
      output = title + items + "Total: " + str(total)
      return output 

    def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
      if(self.check_funds(amount)):
        self.ledger.append({"amount": -amount, "description": description})
        return True
      return False 


    def get_balance(self):
      total_cash = 0
      for item in self.ledger:
        total_cash += item["amount"]
      return total_cash

    def transfer(self, amount, category):
      if(self.check_funds(amount)):
        self.withdraw(amount,"Transfer to " + category.name)
        category.deposit(amount, "Transfer from " + self.name)
        return True
      return False 

    def check_funds(self, amount):
      if(self.get_balance() >= amount):
        return True
      return False 

def create_spend_chart(categories):
  category_names = []
  spent = []
  final_spent = []

  for category in categories:
    total = 0
    for i in category.ledger:
      if i['amount'] < 0:
        total -= i['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for percents in spent:
    final_spent.append(round(percents/sum(spent), 2)*100)
    
  graph_return = "Percentage spent by category\n"

  axis = range(100,-10,-10)

  for label in axis:
    graph_return += str(label).rjust(3) + "| "
    for percents in final_spent:
      if percents >= label:
        graph_return += "o  "
      else:
        graph_return += "   "
    graph_return += "\n"

  graph_return += "    ----" + ("---" * (len(category_names) - 1))
  graph_return += "\n     "

  len_longest = 0

  for names in category_names:
    if len_longest < len(names):
      len_longest = len(names)

  for i in range(len_longest):
    for names in category_names:
      if len(names) > i:
        graph_return += names[i] + "  "
      else:
        graph_return += "   "
    if i < len_longest - 1:
      graph_return += "\n     "

  return graph_return 
