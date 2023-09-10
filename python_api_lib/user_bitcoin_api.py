import requests

class UserBitcoinAPI:
    # Set the base URL for all the Endpoints Requests
    BASE_URL = "https://8j5baasof2.execute-api.us-west-2.amazonaws.com/production"

    def __init__(self) -> None:
        pass

    #ENDPOINTS REQUEST FUNCTIONS

    def create_user(self, username, password):
        """
        Create a new user.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user (must be maximum 7 characters long).

        Returns:
            dict: The endpoint response JSON data.
        """
        if len(password) > 7:
            raise ValueError("Invalid pasword length. Passowrd must be máximum 7 characters long.")

        url = f"{self.BASE_URL}/users/new"
        user_data = {"Username": username, "Password": password}
        headers = {"Content-Type": "application/json"}  # Set the request headers
        
        try:
            response = requests.post(url, json=user_data, headers=headers)
            response.raise_for_status()  # Raise an exception if response has an HTTP error status code
        except requests.exceptions.RequestException as ex:
            raise Exception(f"Failed to create new user: {ex}")
        
        return response.json()

    def login(self, username, password):
        """
        Log in with a username and password.

        Args:
            username (str): The username of the user.
            password (str): The user's password.

        Returns:
            dict: The endpoint response JSON data.
        """

        url = f"{self.BASE_URL}/users/login"
        login_data = {"Username": username, "Password": password}
        headers = {"Content-Type": "application/json"}  # Set the request headers
        
        try:
            response = requests.post(url, json=login_data, headers=headers)
            response.raise_for_status() # Raise an exception if response has an HTTP error status code
        except requests.exceptions.RequestException as ex:
            raise Exception(f"Failed to log in: {ex}")
        
        return response.json()

    def get_user_token(self, username, password):
        """
        Get user token

        Args:
            username (str): The username of the user.
            password (str): The user's password.

        Returns:
            str: The user's token; to be used in further requests
        """ 
        try:
            user_token = self.login(username,password)["Token"]
        except Exception as ex:
            raise Exception(f"Failed to get token. Check for username and/or password: {ex}")

        return user_token

    def get_user(self, username, format_type, token):
        """
        Get user data (UserID, UserName, AmountofBitcoins) in the specified format type: html or tsv.

        Args:
            username (str): The username of the user.
            format (str): The desired format ('html' or 'tsv').
            token (str): The user's token for authentication.

        Returns:
            str: The user data in the specified format.
        """        
        
        if format_type not in ("html", "tsv"):
            raise ValueError("Invalid format type. Use 'html'or 'tsv'")
        
        url = f"{self.BASE_URL}/users/{username}.{format_type}"
        headers = {"Content-Type": "application/json", "Token": token}  # Include "Token" in the request headers
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception response has an HTTP error status code
        except requests.exceptions.RequestException as ex:
            raise Exception(f"Failed to get user info or user not found: {ex}")
        
        return response.text
    
    def get_user_id(self, username, token=None, password=None):
        """
        Get the user ID for a given username.

        Args:
            username (str): The username of the user.
            token (str, optional): The user's token for authentication.
            password (str, optional): The user's password for authentication.
            ***You must use eather a token or a password

        Returns:
            str: The user ID.
        """
        
        if token is not None:
            # Pass and go directly to "Get the user id" below
            pass
        elif password is not None:
            # Use password to get_user_token; use this token in "Get the user id" below
            token = self.get_user_token(username, password)

        else:
            raise ValueError("You must provide either a token or a password for authentication")

        # Get the user id
        user_data = self.get_user(username,"tsv", token)
        #Convert the tsv into a list of six values (2 rows x 3 columns), and the fourth value [3] is the user id
        user_id = user_data.split()[3] 

        return user_id

    def get_user_bitcoins(self, username, token=None, password=None):
        """
        Get the user's amount of available Bitcoins.

        Args:
            username (str): The username of the user.
            token (str, optional): The user's token for authentication.
            password (str, optional): The user's password for authentication.
            ***You must use eather a token or a password

        Returns:
            str: The user´s amount of available Bitcoins in float format.
        """
        
        if token is not None:
            # Use this token. Go to "Get the amount of user's bitcoins" below
            pass
        elif password is not None:
            # Use password to get_user_token; use this token in "Get the amount of user's bitcoins" below
            token = self.get_user_token(username, password)
            
        else:
            # If niether token nor password are provided, rise a ValueError
            raise ValueError("You must provide either a token or a password for authentication")

        # Get the amount of user's bitcoins
        user_data = self.get_user(username,"tsv", token)
        #Convert the tsv into a list of six values (2 rows x 3 columns), and the last value [5] is the amount of bitcoins
        user_bitcoins = float(user_data.split()[5]) 
        return user_bitcoins
 
    def update_user(self, new_password, token):
        """
        Update a user´s password. 
        You must have the token of the user.

        Args:
            new_password (str): The new password (max 7 characters).
            token (str): The user's token for authentication.

        Returns:
            dict: The endpoint response JSON data.
        """

        if len(new_password) > 7:
            raise ValueError("Invalid pasword length. Passowrd must be máximum 7 characters long.")

        url = f"{self.BASE_URL}/users/update"
        update_data = {"new_password": new_password}
        headers = {"Content-Type": "application/json", "Token": token}  # Set the request headers
        
        try:
            response = requests.patch(url, json=update_data, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as ex:
            raise Exception(f"Failed to update user: {ex}")

        return response.json()
    
    def bitcoin_transfer(self, origin_token, dest_user, amount):
        """
        Transfer bitcoins between known users. 
        You must have the token of the origin user, and the username of the destination user

        Args:
            origin_token (str): Sender's token.
            dest_user (str): Destination username
            amount (int): Amount of bitcoins to be transfered

        Returns:
            dict: The endpoint response JSON data.
        """
        
        url = f"{self.BASE_URL}/users/transfer"
        transfer_data = {"To": dest_user, "Amount": amount}
        headers = {"Content-Type": "application/json", "Token": origin_token}  # Include only the origin user token in the request headers
        
        try:
            response = requests.post(url, json=transfer_data, headers=headers)
            response.raise_for_status() # Raise an exception if response has an HTTP error status code
        except requests.exceptions.RequestException as ex:
            raise Exception(f"Bitcoin transfer failed: {ex}")

        return response.json()