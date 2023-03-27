# Calculcate Total Price

## Instruction


Create a program calculates the total price of items that we want to buy.

> `When program starts it will display the list of items, using available_parts dictionary ` 

>  `Then program asks to select an item` 

>   `Then based on user selected item, the program checks if the item exist in the store or not. Because when quantity of item is 0 then it is out of stock` 

>   `Finally, if it is not out of stock we calculate total price of items and decrease quantity from the stock. This continues until user select 0. And when the loop is terminated the total price is printed to the console` 


Sample Output:

```
Please add options from the list
1: computer
2: monitor
3: keyboard
4: mouse
5: hdmi cable
6: dvd drive
0: to finish
> 1
Adding computer
> 2
Adding monitor
> 0
Total price: 700



```

## Hint

- Create dictionary for available_parts like this:

    ```
    1: computer
    2: monitor
    3: keyboard
    4: mouse
    5: hdmi cable
    6: dvd drive
    ```
- Create price_quantity dictionary with nested dictionaries.
    ```
    computer - price: 500, quantity : 10
    monitor - price: 200, quantity : 8
    keyboard - price: 500, quantity : 5
    mouse - price: 10, quantity : 0
    hdmi cable - price: 20, quantity : 7
    dvd drive - price: 50, quantity : 5
    ```

## Solution

[https://replit.com/@AppMillers/Project-27-Calculate-Price-Solution](https://replit.com/@AppMillers/Project-27-Calculate-Price-Solution)