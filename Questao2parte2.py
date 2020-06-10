import Questao2

pizza_maker = Questao2.Concrete_pizza_maker()
print('Ingredients: '+ pizza_maker.get_ingredients()+
   '; Cost: '+str(pizza_maker.get_cost())+'; sales tax = '+str(pizza_maker.get_tax()))

pizza_maker = Questao2.Molho(pizza_maker)
print('Ingredients: '+ pizza_maker.get_ingredients()+
   '; Cost: '+str(pizza_maker.get_cost())+'; sales tax = '+str(pizza_maker.get_tax()))

pizza_maker = Questao2.Queijo(pizza_maker)
print('Ingredients: '+ pizza_maker.get_ingredients()+
   '; Cost: '+str(pizza_maker.get_cost())+'; sales tax = '+str(pizza_maker.get_tax()))

pizza_maker = Questao2.Massa(pizza_maker)
print('Ingredients: '+ pizza_maker.get_ingredients()+
   '; Cost: '+str(pizza_maker.get_cost())+'; sales tax = '+str(pizza_maker.get_tax()))
