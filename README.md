# Selenium Homework

https://insider-portal.atlassian.net/wiki/spaces/OPT/pages/3454140458/5.Basic+Selenium+Proje+devi

## Test Scenario

- Open the browser
- Navigate to the Automation Exercise website
- Verify that the home page is displayed successfully
- Click on the Products button
- Hover over the first product and click "Add to cart"
- Click "Continue Shopping"
- Hover over the second product and click "Add to cart"
- Click "View Cart"
- Verify that both products are added to the cart
- Verify product price, quantity and total amount

## Requirements

- Chrome WebDriver is used
- The project is written in Python
- No Page Object Model (POM) is used, everything is in a single file
- Locators are defined at the top of the file
- Driver is closed after test execution (tearDown)
- Assertions are used in each step
