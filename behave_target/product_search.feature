Feature: Test target website

Scenario: adding products to cart
    Given that we have gone to https://www.target.com/
     When we search for "snickers"
     Then we find products from "snickers"
     AND we add the third product to cart
     AND we find products from "snickers" in cart

Scenario: laundry products made by tide or persil
    Given that we have gone to https://www.target.com/
     When we search for "laundry"
     Then we find products from "tide"
     AND we find products from "persil" 
     
Scenario Outline: concatenate various things
    Given that we have gone to https://www.target.com/
     When we search for "<product>"
     Then we find products from "<company>"

 Examples: Various products
   | product  | company |
   | switch | nintendo  |
   | cheese | Kraft  |
   | milk | horizon |




