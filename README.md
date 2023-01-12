This is a package from Pranav Amlekar that helps you to create various permutations of cases (Camel case and snake case) for bag of words.

Use the following command to install the package :

pip install git+https://github.com/pranava777/create_bag_of_words.git

How to use ?

1. Import the Bow class using following code :

from create_bag_of_words import Bow

2. Declare the list of input bag of words and separator of the substring :

input_bow = ["Head and neck Cancer", "cervical cancer"]
separator = " "

3. Make the object of Bow class and call the get_bag_of_words() method of the class :

obj = Bow(input_bow, separator)
output = obj.get_bag_of_words()

4. Print the output :

print(output)