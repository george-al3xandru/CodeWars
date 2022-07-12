# Grasshopper - Terminal game combat function

Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.

---

### Solution 1:

```python
def combat(health, damage):
    new_health = health - damage
    return new_health if new_health > 0 else 0
```

Solution 2:

```python
def combat(health, damage):
    return max(health - damage, 0)
```
