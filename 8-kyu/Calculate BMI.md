# Calculate BMI

Write function bmi that calculates body mass index (bmi = weight / height2).

Exemple:

```python
if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"
```

---

### Solution 1:

Python:

```python
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5: return "Underweight"
    elif bmi <= 25.0: return "Normal"
    elif bmi <= 30.0: return "Overweight"
    else: return "Obese"
```

### Solution 2:

```python
def bmi(weight, height):
    bmi = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(bmi >= 30) + (bmi >= 25) + (bmi >= 18.5)]
```

JavaScript:

```javascript
function bmi(weight, height) {
  const bmi = weight/(height*height);
  if (bmi <= 18.5)
    return "Underweight";
  else if (bmi <= 25)
    return "Normal";
  else if (bmi <= 30)
    return "Overweight";
  else
    return "Obese"
}
```
