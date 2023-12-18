class MiniCompiler {
  private numericValue: number = 0;
  private output: string = "";

  constructor(program: string) {
    this.compile(program)
  }

  private compile(program: string): void {
    for (const symbol of program) {
      if (symbol === "#") {
        this.numericValue += 1;
      } else if (symbol === "@") {
        this.numericValue -= 1;
      } else if (symbol === "*") {
        this.numericValue *= this.numericValue;
      } else if (symbol === "&") {
        this.output += this.numericValue.toString();
      }
    }
  }

  public getOut(): string {
    return this.output;
  }
}

const solution = new MiniCompiler("&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&");
console.log(solution.getOut())