def get_user_input(prompt_message):
    """
    Takes input from the user with a given prompt message.

    Parameters:
    - prompt_message (str): The message to display to the user while asking for input.

    Returns:
    - str: The input entered by the user.
    """
    user_input = input(prompt_message)
    return user_input

# Example usage
str = get_user_input("Query: ")

