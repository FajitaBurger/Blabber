#!/usr/bin/python
import sentence_generator



def main(): 
    test = sentence_generator.sentence_generator("txt", 4)
    test.generate_sentence(1000)

if __name__ == "__main__":
    main()
