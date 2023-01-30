# # # Single_quotes = 'Look! single quotes'
# # # Double_quotes = "Look! double quotes"
# # #
# # # print(Single_quotes)
# # # print(Double_quotes)
# # #
# # # # string_faliure = 'I said 'wow!''
# # #
# # # escape_example = 'I said \'Wow\''
# # #
# # # print(escape_example)
# # #
# # # quote_in_quote = 'I said "wow!"'
# # # print(quote_in_quote)
# # # reverse_quote = "I said 'Wow!'"
# # # print(reverse_quote)
# # Hw = "Hello world!"
# # print(Hw[7:]) # orld!
# # print(Hw[-5:]) # orld!
# # print(Hw[:5]) # Hello
# # print(Hw[0:5]) # Hello
# #
# # white_space = "lot's of space at the end                        "
# # print(len(white_space)) # 49
# # print(len(white_space.strip()))
# #
# # example_text = "Here's some text with lots of text"
# #
# # # count a substring within a string
# #
# # print(example_text.count("text"))
# #
# # print(example_text.lower())
# # print(example_text.upper())
# # print(example_text.replace("with", ","))
#
# a = "here "
# b = "more "
# c = "much more"
#
# print(a + b + c)
#
#x = 2
#y = 5.4
#z = " there's a number 25.4 unless we put a space!"

#print(x + y + z)
#
#print(str(x) + ", " + str(y) + z)
# int_string = "6"
# print(int(int_string))
# print(type(int(int_string)))

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall")
# name = "Snoopy"
# years = 52
# print(f"{name.upper()} is {years * 7} years old in dog years")

pi = 3.14159265359
print(f"PI to three decimal places: {pi:.3f}")
print(f"PI to three decimal places: {pi:.5f}")

score = 16
max_score = 26
print(f"You scored {score/max_score}") # 0.6153846153846154
print(f"You scored {score/max_score:.0%}")