# ILA 3-1: Applying the Four Pillars of OOP

**Name:** Shelsy Sanchez Francisco

**Section:** 9 Magnesium

**Last Name:** Francisco

**Date:** August 18, 2026

## Sari-Sari Store Inventory System

### Scenario

Consider the case of the sari-sari store and imagine a simple inventory system for it. One would consider having variables for the quantity of the items being sold inside. Let’s say the store sold 5 items. That would mean having 5 variables for the quantity of each item. What about the name of each item? You could fix the name of each item or you could store them in another set of 5 variables for later editing. How about the price? That would mean another set of 5 variables. So far, we’ve created 15 variables for 5 items! Not exactly the most optimal solution. 

You will also need functions for adding items, removing items, and displaying the items. With your current knowledge in programming, how would you design a solution for the given store?

Draft a proposal showing your solution on how to solve the situation above. You can use flowcharts and pseudocodes to illustrate. Some groups will be selected to present their solutions.


### Problem

The current approach to the inventory system required too many separate variables to store information about each product. This can make the program difficult to organize, maintain, and expand. If more products are added, more variables and additional code would have to be created manually.


### Solution

In this scenario, Object Oriented Programming (OOP) is a key paradigm to create a more organized and scalable solution. Instead of creating separate variables for every product, a Product class can serve as a template containing the common attributes of a product, such as its name, quantity, and price. 

## PSEUDOCODE
```text
CLASS Product

    DATA FIELDS:
        name
        quantity
        print
    
    METHOD displayInfo
        DISPLAY name, quantity, and price
    END METHOD

    METHOD addProduct
        INCREASE quantity by the amount added
        DISPLAY "Product added successfully"
    END METHOD

    METHOD removeProduct
        IF quantity to remove is less than or equal to quantity THEN
            DECREASE quantity by the amount removed
            DISPLAY "Product removed successfully"
        ELSE
            DISPLAY "Not enough stock"
        END IF
    END METHOD

END CLASS

CREATE Product product 1
SET product1.name = "Notebook"
SET product1.quantity = 20
SET product1.price = 50

CREATE Product product 1
SET product1.name = "Ballpen"
SET product1.quantity = 20
SET product1.price = 15

DISPLAY product1 information
DISPLAY product2 information

ADD 10 notebooks to product1
REMOVE 5 notebooks to product1

DISPLAY updated product1 information
```
---

### 1. Encapsulation

Encapsulation can be used in the sari-sari store inventory system by keeping everything related to a product, such as its name, quantity and price, within the Product class. As a result, there would be no need for duplicate tracking through separate variables outside the class because each product object already contains and manages its own information. Furthermore, keeping these related data fields together prevents unnecessary information from being scattered throughout the program. Therefore, the inventory system becomes more organized, easier to maintain, and less prone to errors caused by duplicated or mismatched data.


### 2. Abstraction

Abstraction can be used in the sari-sari store inventory system by exposing only the essential operations needed to manage products, such as adding, removing, and displaying items, while hiding the complex details of how these operations are performed. For instance, the user can use an add_item() method without needing to know how the program updates the product’s quantity internally. In this way, abstraction makes the inventory system user-friendly because users only interact with the necessary features while the complex implementation remains hidden.

### 3. Inheritance

Inheritance can be used in the sari-sari store inventory system by creating a general Product class that contains common properties such as name, quantity, and price, which other product classes can inherit. This will be practically useful when more products are added because each new product can inherit these existing properties instead of having them defined separately. As a result, the program can maintain a consistent structure for its products while avoiding unnecessary repetition of the same attributes.


### 4. Polymorphism

Polymorphism can be used in the sari-sari store inventory system by allowing the same method or function to work with different product objects. For example, the display() method can be used for different types of products, but its behavior can change depending on the object that uses it. Thus, the same function name can produce different outputs for different objects, allowing the inventory system to handle various products without needing a separate function for each one.

**EXAMPLE INPUT AND OUTPUT**
```text
INPUT:

Enter product type: Food
Enter product name: Piattos
Enter quantity: 15
Enter price: 20

Enter product type: Beverage
Enter product name: BukoRap
Enter quantity: 10
Enter price: 25

Enter operation: Display Products

OUTPUT:

--- PRODUCT INFORMATION ---
Product Type: Food
Product Name: Piattos
Quantity: 15
Price: ₱20

--- PRODUCT INFORMATION ---
Product Type: Beverage
Product Name: BukoRap
Quantity: 10
Price: ₱25
```

The user performs the same display() operation for both products. However, the output changes based on the type and information of the product being displayed. This demonstrates polymorphism because the same method can be used for different objects while producing different results.

## Reflection

As of the sari-sari store inventory system’s current state, encapsulation would be the most useful among the four pillars as it directly addresses the system’s main problem: the excessive number of variables. While abstraction, inheritance, and polymorphism can improve the system’s usability and flexibility, they are more useful once the basic structure of the inventory has already been organized. In comparison, encapsulation provides the foundation for organizing the product’s data before applying other OOP concepts. Therefore, it would be the most appropriate first step in improving the inventory system.
