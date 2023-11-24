def is_valid_password(policy: tuple, password: int) -> int:
    min_count, max_count, char = policy
    count = password.count(char)
    return min_count <= count <= max_count


def find_invalid_key(data) -> list:
    invalid_keys = []

    for line in data:
        policy_str, password = line.split(':')
        password = password.strip()

        counts, char = policy_str.split(' ')
        min_count, max_count = map(int, counts.split('-'))

        policy = (min_count, max_count, char)

        if not is_valid_password(policy, password):
            invalid_keys.append(password)

    return invalid_keys


def main() -> None:
    with open('../data/encryption_policies.txt', 'r') as file:
        data = file.readlines()

    invalid_keys = find_invalid_key(data)

    if len(invalid_keys) >= 42:
        print(f"The 42nd invalid key is: {invalid_keys[41]}")
    else:
        print("There are fewer than 42 invali keys.")


if __name__ == "__main__":
    main()
