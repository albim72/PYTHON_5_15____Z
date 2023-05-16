from builder import Builder
from director import Director
from conretebuilder1 import  ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Produkt podstawowy:")
director.build_minimal_product_version()
builder.product.list_parts()

print("\n")

print("Produkt pełny:")
director.build_maximal_product_version()
builder.product.list_parts()

print("\n")
print("wersja użytkownika")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
