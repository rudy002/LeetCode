function sumZero(n: number): number[] {
  const result: number[] = [];

  if (n % 2 === 1) result.push(0);

  for (let i = 1; i <= Math.floor(n / 2); i++) {
    result.push(-i, i);
  }

  return result;
}
