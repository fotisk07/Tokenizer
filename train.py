from minitoken import BasicTokenizer


tokenizer = BasicTokenizer()

# Train the tokenizer on some text
contents = open("tests/taylorswift.txt", "r", encoding="utf-8").read()
tokenizer.train(contents,300 ,verbose=True)
tokenizer.save("tay")
