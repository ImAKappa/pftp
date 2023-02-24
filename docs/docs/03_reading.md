# Reading Python Code 📔


To write, you must read. Let's practice reading Python code. For each example, explain in English what you _think_ the code does. Then type the code (do **not** copy-paste, it is essential that you develop muscle memory for writing Python) into the Thonny code editor (the top half of the app) and run it to see if you were right.

### Text

i. 

```python
print("the quick brown fox jumps over the lazy dog".title())
```

ii.

```python
print("the quick brown fox jumps over the lazy dog".upper())
```

iii.

```python
print("the quick brown fox jumps over the lazy dog".replace("dog", "frog"))
```

iv.

```python
print(f"323 + 456 is equal to {323 + 456}")
```

### Numbers and sequences

i. 

```python
print(-1 + -1 + -1 + 4)
```

ii.

```python
print(sum([-1, -1, -1]) + 4)
```

iii.

```python
print(sum([-1] * 3) + 4)
```

### Variables

i.

```python
age = 18
print(f"My age is {age}. In ten years I will be {age + 10}")
```

ii. 

```python
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour

print(f"There are {seconds_per_hour} seconds in one hour")
```

### Control Flow

i. 

```python
groceries = {
    "milk": "2 bags",
    "eggs": "1 carton",
    "strawberry shortcake": "1",
}

print("Honey, we need:")

for item, amount in groceries.items():
    print(f" {amount} {item}")
    if "cake" in item:
        print("(Keep it a surprise!)")
```

ii.

```python
age = 12
age_chant = 1

while age_chant < age:
    print(f"Are you {age_chant}?")
    age_chant = age_chant + 1

print(f"Happy Birthday! You are {age_chant}!")
```

### Functions

i. 

```python
def greet(name):
    print(f"Hello {name}!")

greet("world")
```

ii.

```python
def fahrenheit_to_celsius(F):
    return (F - 32) * (5 / 9)

print(f"100 Fahrenheit is {fahrenheit_to_celsius(100)} deg Celsius")
```