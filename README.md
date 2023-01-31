# tech201_datatypes_and_operators
tech201_datatypes_and_operators


## numeric data types 

- integers are whole numbers 
- floats are decimal numbers, There is no limit to the size of a decimal in python but python will round things up
- complex numbers not used very much 
- Long data types are whole numbers, both positive and negative, that have many place values

- string text of any type,  can use single quotes `''`  or double quotes `""`
- boolean is a true or false statement 

## operators 

### arithmetician operators
`+, -, *, /`

### comparison operators
`>, <, ==, !=, <=, >=,`

escape characters `\` allows us to use singles quote sin a string. 
`escape_example = 'I said \'Wow\''`

`reverse_quote = "I said 'Wow!'"
print(reverse_quote)` this is the one pople tend to use


everyone starts with 0 in code not 1

h e l l o    w o r l d !

1 2 3 4   5  6 7 8 9 10 11
`Hw = "Hello world!"`

`print(Hw[7:])  orld!`

`print(Hw[-5:])  orld!`

`print(Hw[:5])  Hello`

`print(Hw[0:5])  Hello`

## Methods

strip- removes all white space form the end of a string. `print(len(white_space.strip()))`

example_text = "Here's some text with lots of text"

# count a substring within a string

`printexample_text.count("text"))` looks at how many times something is said in a string
`print(example_text.lower())` makes everything lower case
`print(example_text.upper())` makes everything upper case

`print(example_text.replace("with" , ","))` this replaces a word with a specific text 


### concatenation 
`a = "here "`
`b = "more "`
`c = "much more"`

`print(a + b + c)`
this will print (here more much more)

### casting

converts one data type into another `print(str(x) + str(y) + z)`
int to string `print(int(int_string))`
`print(type(int(int_string)))`


F-strings (formatted strings) they allow us to use methods/evaluations too can use f string to specify decimal places and how much to round it up by
`name = "Lassie"`
`years = 7`
`height_cm = 60.2`

`print(f"{name} is {years} years old and {height_cm} cm tall")`

this will print out pi to three decimal places 
`pi = 3.14159265359`
`print(f"PI to three decimal places: {pi:.3f}")`


`score = 16`
`max_score = 26`

`print(f"You scored {score/max_score}") # 0.6153846153846154`

`print(f"You scored {score/max_score:%}")`
this allows you to get a percentage back 


### boolean 
boolean is a true or false statement
`a = 5`
`b = 7`
`print(a > b)` #false
`print(a < b)` #true

`hi = "Hello world!"`

`print(hi.isalpha())` this checks if everything is alpha numeric
`print(hi.islower())` checks if the statement is lower case
`print(hi.endswith("world!"))` checks if the statement ends with world!
`print(hi.startswith("H"))` checks if the statement starts with H



### none is n object type null in alot of other languages 

if you ask python whether non is true or false you always get back false. if you check whether something is == to none it is still false. none is not true or false it just exists.

it can be used as a placeholder for a variable. `print(x is None)` best practice for checking if something is None `<class 'NoneType'>`

