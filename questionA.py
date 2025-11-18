from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

A1 = DFA(states = {'q0','q1','q2','q3','q4','q5','q6'},
		  initial_state='q0',
		  final_states = {'q5'},
		  input_symbols={'a','b', 'c'},
		  transitions = {

			  'q0': {'a':'q6', 'b':'q1', 'c':'q6'},
			  'q1': {'a':'q2', 'b':'q6', 'c':'q6'},
			  'q2': {'a':'q6', 'b':'q3', 'c':'q6'},
			  'q3': {'a':'q6', 'b':'q6', 'c':'q4'},
			  'q4': {'a':'q6', 'b':'q5', 'c':'q6'},
			  'q5': {'a':'q5', 'b':'q5', 'c':'q5'},
			  'q6': {'a':'q6', 'b':'q6', 'c':'q6'},
          })

A2 = DFA(states = {'q0','q1','q2','q3','q4','q5'},
		  initial_state='q0',
		  final_states = {'q5'},
		  input_symbols={'a','b', 'c'},
		  transitions = {
			  'q0': {'a':'q0', 'b':'q1', 'c':'q0'},
			  'q1': {'a':'q2', 'b':'q1', 'c':'q0'},
			  'q2': {'a':'q0', 'b':'q3', 'c':'q0'},
			  'q3': {'a':'q2', 'b':'q1', 'c':'q4'},
			  'q4': {'a':'q0', 'b':'q5', 'c':'q0'},
			  'q5': {'a':'q5', 'b':'q5', 'c':'q5'},
          })

# A3 = NFA(states = {},
# 		  initial_state=,
# 		  final_states = {},
# 		  input_symbols={'a','b', 'c'},
# 		  transitions = {
#           })
#
# A4 = NFA(states = {},
# 		  initial_state=,
# 		  final_states = {},
# 		  input_symbols={'a','b', 'c'},
# 		  transitions = {
#           })


if __name__ == "__main__":

	string = "babcb"

	test = []
	accepted = []
	rejected = []

	alphabet = ['a', 'b', 'c']
	for s0 in alphabet:
		for s1 in alphabet:
			for s2 in alphabet:
				for s3 in alphabet:
					for s4 in alphabet:
						for s5 in alphabet:
							for s6 in alphabet:
								for s7 in alphabet:
									for s8 in alphabet:
										test.append(f"{s0}{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}")


	for word in test:
		if A1.accepts_input(word):
			#print(f"{s!r} → ACCEPTED")
			accepted.append(word)
		else:
			rejected.append(word)
			#print(f"{s!r} → REJECTED")

	# print(f"Accepted: {accepted}\n")
	# print(f"Rejected: {rejected}\n")

 	# Test for q1 (i)
	# correct = 0
	# for word in accepted:
	# 	if string == word[0:len(string)]:
	# 		correct += 1
	# print(f"{(correct / len(accepted)) * 100}% of the accepted list, contains {string}")
	#
	# correct = 0
	# for word in rejected:
	# 	if string == word[0:len(string)]:
	# 		correct += 1
	# print(f"{(correct / len(rejected)) * 100}% of the rejected list, contains {string}")


	# Test for Q2 (ii)
	# correct = 0
	# for word in accepted:
	# 	if string in word:
	# 		correct += 1
	#
	# print(f"{(correct / len(accepted) ) * 100}% of the accepted list, contains {string}")
	#
	# correct = 0
	# for word in rejected:
	# 	if string in word:
	# 		print("Rejected: "+word)
	# 		correct += 1
	#
	# print(f"{(correct / len(rejected)) * 100}% of the rejected list, contains {string}")
