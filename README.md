# Harambee Arms

## Project Description

Harambee Arms is a web application where users can browse and purchase firearms and firearms accessories. The application provides an intuitive and secure platform for gun enthusiasts in Kenya to explore and buy products online.

## Problem Statement

### Problem

In Kenya, gun enthusiasts face challenges in finding and purchasing firearms and accessories due to limited access to physical stores and the lack of a centralized platform for browsing a wide range of products. These challenges make it difficult for customers to make informed decisions and for sellers to reach a broader audience.

### Solutions

Harambee Arms aims to solve these problems by providing an intuitive and secure web application for browsing and purchasing firearms and accessories. The key solutions include:

- **Centralized Product Listings**:
  - **View Available Guns**: Users can view a comprehensive list of all available guns and accessories, complete with detailed information and images.
  - **Product Details**: Detailed product pages provide specifications, descriptions, and images to help customers make informed decisions.

- **User-Friendly Shopping Experience**:
  - **Add to Cart**: Users can easily add guns and accessories to their shopping cart.
  - **Purchase Guns**: A streamlined checkout process allows users to purchase products online securely.

- **Enhanced User Interaction**:
  - **User Authentication**: Secure registration and login functionality ensure that only authorized users can make purchases.
  - **User Profile Management**: Users can manage their profiles, view purchase history, and update personal information.

- **Advanced Search and Management Features**:
  - **Search and Filter**: Users can search for guns by name, category, or brand, and filter results by type, caliber, or price.
  - **Wishlist**: Users can save guns to their wishlist for quick access later.
  - **Admin Dashboard**: Admin users can add, update, or delete products from the inventory, and view/manage orders efficiently.

By addressing these key areas, Harambee Arms enhances the shopping experience for gun enthusiasts in Kenya, providing a reliable and comprehensive platform for all their firearm and accessory needs.

## Models and Relationships

### Models

#### Customer

| Column     | Data Type and Constraints                      |
|------------|------------------------------------------------|
| id         | Integer, primary_key                           |
| name       | String(unique=True, nullable=False)           |
| wallet     | Float                                          |
| admin      | Boolean                                        |
| username   | String(unique=True, nullable=False)           |
| password   | String(nullable=False)                         |
| created_at | DateTime                                      |
| updated_at | DateTime                                      |

**Relationships**:
- One-to-many with Order (a customer can have many orders)
- Many-to-many with Items through OrderItems

#### Item

| Column     | Data Type and Constraints                      |
|------------|------------------------------------------------|
| id         | Integer                                        |
| title      | String(unique=True, nullable=False)           |
| image_url  | String                                         |
| description| String                                         |
| category   | String(nullable=False)                         |
| price      | Integer                                        |

**Relationships**:
- One-to-many with OrderItem
- Many-to-many with Customers through OrderItems

#### Order

| Column     | Data Type and Constraints                      |
|------------|------------------------------------------------|
| id         | Primary Key(Integer)                           |
| customer_id| Foreign Key(Integer)                           |
| total      | Float                                          |
| created_at | DateTime                                      |
| updated_at | DateTime                                      |

**Relationships**:
- Many-to-one with Customer
- One-to-many with OrderItem

#### OrderItem

| Column     | Data Type                                      |
|------------|------------------------------------------------|
| id         | Integer                                        |
| quantity   | Integer                                        |
| order_id   | ForeignKey(Order.id)                          |
| item_id    | ForeignKey(Items)                             |
| created_at | DateTime                                      |
| updated_at | DateTime                                      |

**Relationships**:
- Many-to-one with Order
- Many-to-one with Item

### Views

- **Home Page**: List all guns and accessories with search and filter options.
- **Product Detail Page**: Details of a specific gun or accessory and an "Add to Cart" button.
- **Cart Page**: List of items in the cart with the ability to update quantity or remove items.
- **Checkout Page**: Form to enter payment and shipping details.
- **User Profile Page**: User's purchase history and option to update profile information.
- **Admin Dashboard**: Interface for managing gun and accessory inventory and viewing orders (for admin users).


## Technologies Used

- **Frontend**: React.js
- **Backend**: Flask
- **Database**: SQLAlchemy
- **Styling**: CSS/TailwindCSS
- **Forms**: Formik
- **Authentication**: JSON Web Tokens (JWT)




## Setup

### Prerequisites

- Python 3.8+
- Node.js 14+
- A package manager (pip, npm)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iankuria668/harambee-arms-group-10-project.git
   cd harambee-arms-group-10-project.git

2. Set up the backend:

   ```bash
      cd server
      export FLASK_APP=app.py
      export FLASK_RUN_PORT=5555
      python app.py

3. Set up the frontend
   ```bash
      cd client
      npm install

## Contributors

- [Sharon](https://github.com/B-Sharon)
- [Ian](https://github.com/iankuria668)
- [Charles](https://github.com/Chalo101)
- [Maria](https://github.com/mwanjiru12)
- [Lee]


## License
This project is licensed under the MIT License

Copyright 2024 HARAMBEE ARMS

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



