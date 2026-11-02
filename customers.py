# customers.py
# Author - Edwin Ross
# mod 11 lab dictionary

# Exercise 1 - One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


# exercise 2...


print("--- Exercise 2 ---")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


