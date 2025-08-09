def fizzBuzz(n: int):
    result = []
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            result.append('FizzBuzz')
        elif n % 3 == 0:
            result.append('Fizz')
        elif n % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(n))
    return result

def main():
        n = int(input("Введите значение n: "))
        fizz_buzz_result = fizzBuzz(n)
        print("Результат FizzBuzz:")
        for item in fizz_buzz_result:
            print(item)
if __name__ == "__main__":
     main()