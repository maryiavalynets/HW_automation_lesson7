Feature: Test for Amazon Sign in and Cart

Scenario: Logged out user sees Sign in page when clicking Orders
  Given Open amazon page
  When Click on Returns and Orders button
  Then Sign in page shows

Scenario: 'Your Shopping Cart is empty' shown if no product added
  Given Open amazon page
  When Click on the cart icon
  Then The Amazon Cart is empty