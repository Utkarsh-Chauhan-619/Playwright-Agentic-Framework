# Test Plan — https://www.saucedemo.com/ — 2026-05-14T00:00:00Z

## 1. Application Overview
SauceDemo is a demo e-commerce website provided by Sauce Labs for testing purposes. It simulates an online store where users can log in, browse products, add items to cart, and complete checkout. Key user journeys include authentication (login/logout), product browsing and selection, cart management, and a multi-step checkout process. The site includes error handling for invalid inputs and maintains session state for authenticated users.

## 2. Pages Discovered
| Page Name          | URL / Route                | Description                                      |
|--------------------|----------------------------|--------------------------------------------------|
| Login              | /                          | Login form with username and password fields     |
| Products           | /inventory.html            | Product catalog with add to cart buttons         |
| Cart               | /cart.html                 | Cart view with items, remove, and checkout       |
| Checkout Step One  | /checkout-step-one.html    | Customer information form (first name, last name, zip) |
| Checkout Step Two  | /checkout-step-two.html    | Order summary and payment details                |
| Checkout Complete  | /checkout-complete.html    | Order confirmation page                          |

## 3. Page Objects Required
| Class Name      | File                     | Responsibilities                                  |
|-----------------|--------------------------|---------------------------------------------------|
| BasePage        | pages/base_page.py       | Shared helpers, wait utilities, common selectors  |
| LoginPage       | pages/login_page.py      | Handle login form, error messages                 |
| ProductsPage    | pages/products_page.py   | Product list interactions, add to cart            |
| CartPage        | pages/cart_page.py       | Cart item management, checkout initiation         |
| CheckoutPage    | pages/checkout_page.py   | Multi-step checkout forms and completion          |

## 4. Fixtures Required
| Fixture Name       | Scope    | Description                                        |
|--------------------|----------|----------------------------------------------------|
| base_url           | session  | Target URL from pytest.ini or CLI                   |
| browser_context    | function | Fresh isolated browser context per test            |
| authenticated_page | function | Page fixture with user logged in                    |

## 5. Test Cases

### Tier: Smoke
| ID     | Title                        | Page Object(s) | Preconditions          | Steps                                                                 | Expected Result                          |
|--------|------------------------------|----------------|------------------------|-----------------------------------------------------------------------|------------------------------------------|
| TC-S01 | Successful Login             | LoginPage      | None                   | 1. Navigate to login page<br>2. Enter username 'standard_user'<br>3. Enter password 'secret_sauce'<br>4. Click login button | Redirected to products page              |
| TC-S02 | Logout                       | ProductsPage   | User logged in         | 1. Click menu button<br>2. Click logout link                          | Redirected to login page                 |

### Tier: Functional
| ID     | Title                        | Page Object(s)      | Preconditions          | Steps                                                                 | Expected Result                          |
|--------|------------------------------|---------------------|------------------------|-----------------------------------------------------------------------|------------------------------------------|
| TC-F01 | Add Single Product to Cart   | ProductsPage        | User logged in         | 1. Navigate to products page<br>2. Click 'Add to cart' on first product | Cart badge shows '1'                     |
| TC-F02 | View Cart                    | CartPage            | Product in cart        | 1. Click cart icon                                                    | Cart page displays added product         |
| TC-F03 | Remove Product from Cart     | CartPage            | Product in cart        | 1. Navigate to cart<br>2. Click 'Remove' on product                   | Product removed, cart empty              |
| TC-F04 | Complete Checkout            | CheckoutPage        | Product in cart        | 1. Click 'Checkout'<br>2. Fill first name, last name, zip<br>3. Click 'Continue'<br>4. Click 'Finish' | Checkout complete page shown             |
| TC-F05 | Browse Product Details       | ProductsPage        | User logged in         | 1. Click on product name/image                                        | Product details modal or page displayed  |

### Tier: Regression
| ID     | Title                        | Page Object(s)      | Preconditions          | Steps                                                                 | Expected Result                          |
|--------|------------------------------|---------------------|------------------------|-----------------------------------------------------------------------|------------------------------------------|
| TC-R01 | Invalid Login Credentials    | LoginPage           | None                   | 1. Enter invalid username/password<br>2. Click login                  | Error message 'Username and password do not match' |
| TC-R02 | Checkout with Empty Cart     | CartPage            | Cart empty             | 1. Navigate to cart<br>2. Click 'Checkout'                             | Error or redirect, no checkout allowed   |
| TC-R03 | Checkout Form Validation     | CheckoutPage        | At checkout step one   | 1. Leave fields empty<br>2. Click 'Continue'                           | Validation errors for required fields    |

### Tier: Edge Cases
| ID     | Title                        | Page Object(s)      | Preconditions          | Steps                                                                 | Expected Result                          |
|--------|------------------------------|---------------------|------------------------|-----------------------------------------------------------------------|------------------------------------------|
| TC-E01 | Add Multiple Products        | ProductsPage        | User logged in         | 1. Add several products to cart                                       | Cart badge updates correctly             |
| TC-E02 | Session Expiration           | Any                 | User logged in, idle   | 1. Wait for session timeout<br>2. Attempt action                      | Redirected to login page                 |

## 6. Test Data
- Username: standard_user
- Password: secret_sauce
- Invalid Username: invalid_user
- Invalid Password: wrong_password
- First Name: John
- Last Name: Doe
- Zip Code: 12345
- Expected Error: Username and password do not match any user in this service
- Product Names: Sauce Labs Backpack, Sauce Labs Bike Light, etc.

## 7. Selectors Reference
- Username field: [data-test="username"]
- Password field: [data-test="password"]
- Login button: [data-test="login-button"]
- Menu button: [data-test="open-menu"]
- Logout link: [data-test="logout-sidebar-link"]
- Add to cart buttons: [data-test="add-to-cart-sauce-labs-backpack"] (varies by product)
- Cart icon: [data-test="shopping-cart-link"]
- Cart badge: [data-test="shopping-cart-badge"]
- Remove buttons: [data-test="remove-sauce-labs-backpack"]
- Checkout button: [data-test="checkout"]
- Continue button: [data-test="continue"]
- Finish button: [data-test="finish"]
- First name: [data-test="firstName"]
- Last name: [data-test="lastName"]
- Zip: [data-test="postalCode"]
- Error message: [data-test="error"]

## 8. Known Risks & Gaps
- No third-party integrations or external redirects observed.
- All pages and flows fully explored.
- Session timeout behavior assumed based on typical web app patterns; may need verification.