from __future__ import annotations
from abc import ABC,abstractmethod
from dataclasses import dataclass
from typing import Dict


# Pricing strategy 

class PricingStrategy(ABC):
    
    @abstractmethod
    def calculate(self,subtotal: float) -> float:
        pass
    
class NoDiscount(PricingStrategy):
    def calculate(self, subtotal: float) -> float:
        return subtotal
    

class PercentageDiscount(PricingStrategy):
    def __init__ (self, percent: float):
        
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100")
        
        self.percent = percent
        
    def calculate(self, subtotal: float) -> float:
        
        discount = subtotal * (self.percent/ 100)
        return subtotal - discount
    
# ------------ Product ------------

@ dataclass(frozen=True)
class Product:
    
    sku: str
    name: str
    price: float
    
    def __post_init__(self):
        if self.price <=0:
            raise ValueError("Price must be greater than 0")
        

# ------------ Cart Item ------------

@dataclass
class CartItem:
    product: Product
    qty: int =1
    
    def subtotal(self) -> float:
        return self.product.price * self.qty
    

# ------------ Shopping Cart ------------

class ShoppingCart:
    
    def __init__ (self, strategy: PricingStrategy ):
        
        self._items: Dict[str, CartItem] ={}
        self.strategy = strategy
        
    def add (self, product: Product, qty: int = 1):
        
        if qty < 1:
            raise ValueError("Quantity must be >=1")
        
        if product.sku in self._items:
            self._items[product.sku].qty += qty
        else:
            self._items[product.sku] = CartItem(product, qty)
            
    def remove( self, sku:str):
        
        if sku not in self._items:
            raise KeyError("Product not in cart")
        
        del self._items[sku]
        
    def subtotal(self):
        return sum(item.subtotal() for item in self._items.values() )
    
    def total(self):
        
        return self.strategy.calculate(self.subtotal())
    
    def items(self):
        return list(self._items.values())