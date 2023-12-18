import { readFileSync } from "node:fs";

interface Policy {
  minCount: number;
  maxCount: number;
  char: string;
}

function isValidPassword(policy: Policy, password: string): boolean {
  const { minCount, maxCount, char } = policy;
  const count: number = password.split(char).length - 1;
  return minCount <= count && count <= maxCount;
}

function findInvalidKey(data: string[]): string {
  const invalidKey: string[] = [];

  data.forEach((line: string): void => {
    const [policyStr, password] = line.split(":");
    const trimmedPassword: string = password.trim();

    const [counts, char] = policyStr.split(" ");
    const [minCount, maxCount] = counts.split("-").map(Number);

    const policy: Policy = { minCount, maxCount, char };

    if (!isValidPassword(policy, trimmedPassword)) {
      invalidKey.push(trimmedPassword);
    }
  });

  return invalidKey[41];
}

function main() {
  const data: string[] = readFileSync(
    "./data/encryption_policies.txt",
    "utf-8"
  ).split("\n");

  const invalidKey: string = findInvalidKey(data);

  if (invalidKey) {
    console.log(`The 42nd invalid key is: ${invalidKey}`);
  } else {
    console.log("There are fewer than 42 invalid keys.");
  }
}

main();
