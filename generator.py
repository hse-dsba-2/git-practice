from string import ascii_letters
import random
if __name__ == "__main__":
    grades = open("grades.csv","w")
    for i in range(10):
        rand_int = [str(random.randrange(0, 11)) for i in range(10)]
        rand_seq = random.choices(ascii_letters, k=random.randrange(3, 10))
        grades.write("".join(rand_seq)+','+','.join(rand_int)+"\n")
    grades.close()
