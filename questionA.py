from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
import re

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

A3 = NFA(states = {'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10'},
		  initial_state='q0',
		  final_states = {'q10'},
		  input_symbols={'a','b', 'c'},
		  transitions = {
			  'q0': {'a': {'q0'}, 'b': {'q0', 'q1'}, 'c': {'q0'}},
			  'q1': {'a': {'q2'}, 'b': {'q1'}, 'c': {'q0'}},
			  'q2': {'a': {'q0'}, 'b': {'q3'}, 'c': {'q0'}},
			  'q3': {'a': {'q2'}, 'b': {'q1'}, 'c': {'q4'}},
			  'q4': {'a': {'q0'}, 'b': {'q5'}, 'c': {'q0'}},
			  'q5': {'a': {'q5'}, 'b': {'q5', 'q6'}, 'c': {'q5'}},
			  'q6': {'a': {'q7'}, 'b': {'q6'}, 'c': {'q5'}},
			  'q7': {'a': {'q5'}, 'b': {'q8'}, 'c': {'q5'}},
			  'q8': {'a': {'q7'}, 'b': {'q6'}, 'c': {'q9'}},
			  'q9': {'a': {'q5'}, 'b': {'q10'}, 'c': {'q5'}},
			  'q10': {'a': {'q10'}, 'b': {'q10'}, 'c': {'q10'}}
          })
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
										for s9 in alphabet:
											for s10 in alphabet:
												for s11 in alphabet:
													for s12 in alphabet:
														test.append(
															f"{s0}{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}{s9}{s10}{s11}{s12}")
														# for s13 in alphabet:
														# 	for s14 in alphabet:
														#
														# 		test.append(f"{s0}{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}{s9}{s10}{s11}{s12}{s13}{s14}")


	for word in test:
		if A3.accepts_input(word):
			#print(f"{s!r} → ACCEPTED")
			accepted.append(word)
		else:
			rejected.append(word)
			#print(f"{s!r} → REJECTED")



	# print(f"Accepted: {accepted}\n")
	# print(f"Rejected: {rejected}\n")

