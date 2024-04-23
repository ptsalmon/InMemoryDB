## Instructions

This database supports the following functions:

- `begin_transaction()`: Starts a new transaction.
- `put(key, value)`: Creates a new key with the provided value or updates the value of an existing key within the transaction.
- `get(key)`: Returns the value associated with the key or `None` if the key doesn't exist.
- `commit()`: Applies changes made within the transaction to the main state.
- `rollback()`: Aborts all changes made within the transaction and reverts to the state before the transaction started.

### Running the Code

To run the code, simply execute the `main.py` file using a Python interpreter.

```bash
python main.py
```


### Assignment Feedback

I think it would be easier to provide students with a stub file already containing the InMemoryDB class with function headers, but leave the definitions blank and let the students implement them. This would make it much easier to grade because you could create standardized test cases formatted for the stub file. This would make grading faster and make the assignment more scalable.