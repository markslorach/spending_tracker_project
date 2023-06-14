# MoneyMate Spending Tracker

This is a simple spending tracker application that allows users to track their expenses. It allows you to create, edit, and remove merchants and tags for categorising your transactions. You can assign tags and merchants to each transaction along with the amount spent. The app provides a comprehensive view of all your transactions, including the amount, merchant, and tag, as well as a total for all transactions.

## Getting Started

To run the app, follow these steps:

1. Open your terminal.
2. Ensure you have PostgreSQL installed.
3. Run the following commands in the terminal:

```
dropdb money_tracker
psql -d money_tracker -f db/money_tracker.sql
python3 console.py
flask run
```

## Prerequisites

Make sure you have the following software installed on your system:

- PostgreSQL: You can download and install PostgreSQL from the official website.

## Usage

Once the application is up and running, you can access it through your web browser on `http://localhost:5000` The main features of the application include:

- **Merchants:** You can create, edit, and remove merchants that represent places or businesses where you made your purchases, such as Tesco, Amazon, or ScotRail.

- **Categories:** You can create and edit tags to categorise your spending. For example, you could have tags like groceries, entertainment, or transport.

- **Transactions:** You can create transactions by assigning a merchant, tag, and the amount spent. Transactions allow you to keep a record of your expenses.

- **Transaction View:** The application provides a comprehensive view of all your transactions. You can see the amount spent, the associated merchant and tag, and a total for all transactions.

## Inspired by

This application takes inspiration from popular online and mobile banking apps such as Starling, Mettle and Monzo.

## Authors

This application was developed by Mark Slorach for CodeClan’s full stack solo project.

## Screenshots

![Transactions](/static/images/screenshot_1.png)

![Transactions](/static/images/screenshot_2.png)
