# SG11 Polymorphism Activity 2

1. 

a. What is duck typing, as explained in the video?

According to Bro Code's video, Learn Python DUCK TYPING in 4 minutes, duck typing follows the adage, "If it looks like a duck and quacks like a duck, it must be a duck." Duck typing is another way of achieving polymorphism aside from inheritance. Based on my understanding, it means that as long as an object possesses the necessary attributes or methods required for a particular operation, it can be treated accordingly, regardless of its actual class or type.

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

The Car class needed to have the speak() method so that it could work inside the same loop as Dog and Cat, even without inheriting from the Animal class. Based on my understanding, duck typing does not depend on which class an object belongs to. Instead, it focuses on whether the object has the necessary method to perform the required operation. In this case, since the loop calls the speak() method, the Car class must also implement it to work within the same loop.

2. Python Code

[Activity 2.2 Source Code](q2/sg11_polymorphism_a1.py)

3. How does the code in 2.2 demonstrate polymorphism?

The code in 2.2 demonstrates polymorphism through duck typing, as objects from different classes can execute the same function as long as they possess the required method. Although the Drone class may not conventionally be considered a vehicle since it does not transport people or goods, it can still be passed into the start_trip() function because it has a move() method. This demonstrates that duck typing focuses on the methods an object possesses rather than the class it belongs to, allowing objects of different classes to be treated similarly and perform the same operation in their own ways.