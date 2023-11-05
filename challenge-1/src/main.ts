function decodeMessage(message: string) {
  const words: string[] = message.toLowerCase().split(' ');
  const wordCount: Map<string, number> = new Map();
  const result: string[] = [];

  for (const word of words) {
    if (!wordCount.has(word)) {
      wordCount.set(word, 1);
    } else {
      wordCount.set(word, (wordCount.get(word) || 0) + 1);
    }
  }

  for (const word of words) {
    const count = wordCount.get(word);

    if (!wordCount.has(word)) {
      result.push(`${word}${count}`);
      wordCount.delete(word);
    }
  }

  return result.join('');
}
