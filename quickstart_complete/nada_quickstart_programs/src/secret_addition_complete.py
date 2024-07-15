from nada_dsl import *

def nada_main():
    # Define the party
    party1 = Party(name="Party1")

    # Define the secret integers as inputs from Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform multiplication of the secret integers
    new_int = my_int1 * my_int2

    # Output the result to Party1
    return [Output(new_int, "my_output", party=party1)]

# No explicit function like create_nada_program is needed; the nada_main function is directly used.
