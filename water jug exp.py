def water_jug(jug1_capacity, jug2_capacity, target):
    jug1 = 0
    jug2 = 0

    while True:
        print(f"Jug1: {jug1} | Jug2: {jug2}")

        if jug1 == target or jug2 == target:
            print(f"\nTarget {target} reached!")
            break

        # Fill jug1
        if jug1 == 0:
            jug1 = jug1_capacity
        # Pour from jug1 to jug2
        elif jug2 != jug2_capacity:
            transfer = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer
            jug2 += transfer
        # Empty jug2
        else:
            jug2 = 0

# Example usage
water_jug(jug1_capacity=4, jug2_capacity=3, target=2)
