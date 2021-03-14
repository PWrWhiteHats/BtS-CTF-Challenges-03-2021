## SOLUTION

This challenge is AI-releted and it is based on the fact that cats and dogs are acting as binary data. In other words, the sequence of cats and dogs forms a message. Dogs are 1 and cats are 0.
What need to be done is to find a trained model to classify all these feline and canine faces. Worst case, you could train a model yourself. Then, after reducing each image to a 0 or a 1, they needed to turn that sequence of bytes into a string. 
Script `solver.py` will find the flag in given images.