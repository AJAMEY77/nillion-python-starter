from nada_dsl import *

def nada_main():
    # Define the party
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define the secret integers as inputs from Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Define the secret integer as input from Party2
    modulus = SecretInteger(Input(name="modulus", party=party2))

    # Perform addition of the secret integers
    sum_result = my_int1 + my_int2

    # Compute the result modulo the secret integer
    result_modulus = sum_result % modulus

    # Output the result to Party1
    return [Output(result_modulus, "result_modulus", party=party1)]

# No explicit function like create_nada_program is needed; the nada_main function is directly used.
