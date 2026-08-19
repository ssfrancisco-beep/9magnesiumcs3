#

## Smart School Canteen Queue | Annex A

**Name:** Shelsy Sanchez Francisco

**Section:** 9 Magnesium

**Last Name:** Francisco

**Date:** August 18, 2026

## Step 1: Identify the Big Problem 

### Main Problem

The PSHS school canteen's lunch service procedure results in long lines and congested areas due to ineffective and inefficient ordering, payment, and food inventory management.

---

## Step 2: Identify the Sub-Problems

1. Customers may have difficulty choosing an item because the available food choices are not clearly visible while they are in line.
2. The canteen's limited space and lack of designated areas for queueing can cause congestion, making it difficult for students to move around.
3. Customers may have to wait longer because the cashier manually calculates the total cost and change for each transaction.
4. Canteen staff may not know when food items are running low, which can cause delays when customers order unavailble items and need to choose a replacement that may have a lower or higher cost.

---

## Step 3: Define Computational Thinking Approaches

| Sub-Problem | CT Skill | Proposed solution | 
|---|---|---|
| Limited Food Visibility | Abstraction | Since most customers buy meals during lunch breaks, only the relevant information, such as the available meals and their prices, can be displayed on whiteboards or printed menus at the entrance or before the counter. | 
| Unorganized Queueing Areas | Decomposition | The canteen could be divided into designated areas for ordering and payment, and a separate area for food pickup, with the queue arranged to follow the canteen's layout so that it does not extend outside. | 
| Manual Payment Calculation | Algorithm Design | Computers with programmed applications could be used to automatically calculate the total cost and change, reducing the cashier's task to mainly entering the customer's payment and returning the change. The same system could also track food inventory, allowing customers to be informed when an item is unavailable before or during their order. |
| Untracked Food Inventory | Pattern Recognition | The system could record the quantity of each food item and monitor changes in stock throughout the day. It could identify patterns in which items are frequently sold our or reach a low quantity and notify the canteen staff when they need to be restocked. |

---

## Step 4: Algorithmic Solution

### Selected Sub Problem

Sub-Problem 3 | Customers may have to wait longer because the cashier manually calculates the total cost and change for each transaction.

### Pseudocode

START

    Display food menu and prices
    Customer selects food items
    Calculate total cost
    Display total cost
    Receive customer's payment

    IF payment is greater than or equal to total cost THEN 
        Calculate change
        Display change
        Give change to customer
        Record transaction
    ELSE
        Display "Insufficient payment"
    END IF
    
END







