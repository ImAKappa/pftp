# 🧮 Calculator

Using Python as a very infinitely-extensible calculator

## Date & Time Calculations

Number of business days between two dates

> Source: [NumPy business day](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html)

```python
np.busday_count('2023-06-10', '2023-06-30', holidays=['2023-06-13', '2023-06-20']) + 1
```

