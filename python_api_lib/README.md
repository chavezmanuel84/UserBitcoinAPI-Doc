# User Bitcoin API Library 🟡🟠🔴

Welcome to the User Bitcoin API Python Library. This library allows you to easily interact with the User Bitcoin API. You can use it to create users, log in, retrieve user data, update passwords, and transfer bitcoins between users.

## Usage

To use the library, follow these steps:

1. Import the `UserBitcoinAPI` class from the library.

```python
   from user_bitcoin_api import UserBitcoinAPI
   ```

2. Create an instance of the class.

```python
myapi = UserBitcoinAPI()
```
   
3. Use the provided methods to interact with the API.

### Creating a New User

```python
response = myapi.create_user("username", "password")
print(response)
```

### Logging In

```python
response = myapi.login("username", "password")
print(response)
```

## Getting User Information

### Get Users ID, Username and Amount of Bitcoins in tsv format 

```python
user_id = myapi.get_user("username", "tsv", "user_token")
print(user_id)
```
### Get Users ID, Username and Amount of Bitcoins in html format 

```python
user_id = myapi.get_user("username", "html", "user_token")
print(user_id)
```
## Getting Specific user Information

### Get the user's ID
```python
user_id = myapi.get_user_id("username", token="user_token")
print(user_id)
```
### or
```python
user_id = myapi.get_user_id("username", password="user_password")
print(user_id)
```
### Get the user´s Amount of Bitcoins
```python
user_bitcoins = myapi.get_user_bitcoins("username", token="user_token")
print(user_bitcoins)
```
### or
```python
user_id = myapi.get_user_bitcoins("username", password="user_password")
print(user_bitcoins)
```

### Updating User Password

```python
response = myapi.update_user("new_password", "user_token")
print(response)
```

### Bitcoin Transfer

```python
response = myapi.bitcoin_transfer("origin_token", "destination_username", amount)
print(response)
```

You can explore more in the library's source code and/or by reading the docstrings.
