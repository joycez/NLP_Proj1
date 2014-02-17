from lm import *

def main():
	lm = LangModel("sample.lm", 2)
	print lm.prob_bigram("God", "saw");

if __name__ == "__main__":
	main()