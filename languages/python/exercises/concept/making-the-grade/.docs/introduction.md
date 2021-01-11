## loops

## Loops in Python

There are 2 general ways in Python to loop or `iterate` through objects.

- `while` loop (_indefinite_, or _uncounted_)
- `for` loop (_definite_, or _counted_)


## While

The number of iterations is unspecified.  Instead, the contained code block is executed each time the condition is met.

```python
# The code will continue to execute as long as the condition is met.
while <condition_to_evaluate>:
    <code_block_to_execute>
```

The condition is evaluated in a `boolean context` (_it needs to return True, truthy, False, or falsey values_) and the loop advances and executes the code in the indented block - or "body" of the loop. Looping continues until the condition is no longer met, at which point the loop exits.

```python
>>> number = 5
>>> while number >= 1:
...    print(number)
...    number -= 1
... print("DANCE PARTY")
... print("♪┏(・o･)┛♪┗ ( ･o･) ┓♪")
...
5
4
3
2
1
DANCE PARTY
♪┏(・o･)┛♪┗ ( ･o･) ┓♪
```

## For

The number of iterations is based on objects with a specific _length_. The Loop will execute until the object being iterated through is exhausted. The object in this case could be the indexes in any iterable type like `list`, `string`, `bytes`, `tuple`, `set`, or `dict` -- or the values in the build-in `range()` object.

```python
for item in countable_object:
    set_of_statements
```

```python
>>> numbers = [1, 2, 3, 4, 5]

>>> for number in numbers:
         print(number)
#=> 1
#=> 2
#=> 3
#=> 4
#=> 5
```

## Breaking from loops

Where you have a large set of objects that you want to loop through but would like to stop the loop execution when a certain condition is met, the `break` statement comes to the rescue.

```python
list_of_items = [1, 2, 3, 4, 5, 6, 7, 8]
for item in list_of_items:
    if item > 5:
        break
    print(item)
# => 1
# => 2
# => 3
# => 4
# => 5
```

## Continuing in loops

You will have important objects as well as non important ones. When you want to skip over the objects that you don't need to process you use the `continue` statement.

Example: you want to process only odd numbers in a loop and not the event numbers.

```python
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in all_numbers:
    if num % 2 == 0:
        continue
    print(num)
# => 1
# => 3
# => 5
# => 7
```
