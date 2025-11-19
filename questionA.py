from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
import re
import itertools

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

A4 = NFA(states = {'q0','q1','q2','q3','q4','q5',
				   'q01','q11','q21','q31','q41',
				   'q02','q12','q22','q32','q42',
				   'q03','q13','q23','q33',
				   'q04','q14','q24',
				   'q05','q15',
				   'q06',
				   },
		  initial_state='q0',
		  final_states = {'q06','q15','q24','q33','q42','q5',},
		  input_symbols={'a','b', 'c'},
		  transitions = {
			  # [x]babcb
			  'q0': {'a': {'q01'}, 'b': {'q01', 'q1'}, 'c': {'q01'}},
			  'q01': {'a': {'q01'}, 'b': {'q02'}, 'c': {'q01'}},
			  'q02': {'a': {'q03'}, 'b': {'q02'}, 'c': {'q01'}},
			  'q03': {'a': {'q01'}, 'b': {'q04'}, 'c': {'q01'}},
			  'q04': {'a': {'q03'}, 'b': {'q02'}, 'c': {'q05'}},
			  'q05': {'a': {'q01'}, 'b': {'q06'}, 'c': {'q01'}},
			  'q06': {'a': {'q02'}, 'b': {'q02'}, 'c': {'q01'}},

			  # b[x]abcb
			  'q1': {'a': {'q11','q2'}, 'b': {'q11'}, 'c': {'q11'}},
			  'q11': {'a': {'q12'}, 'b': {'q11'}, 'c': {'q11'}},
			  'q12': {'a': {'q12'}, 'b': {'q13'}, 'c': {'q11'}},
			  'q13': {'a': {'q12'}, 'b': {'q11'}, 'c': {'q14'}},
			  'q14': {'a': {'q12'}, 'b': {'q15'}, 'c': {'q11'}},
			  'q15': {'a': {'q12'}, 'b': {'q11'}, 'c': {'q11'}},

			  # ba[x]bcb
			  'q2': {'a': {'q21'}, 'b': {'q21','q3'}, 'c': {'q21'}},
			  'q21': {'a': {'q21'}, 'b': {'q22'}, 'c': {'q21'}},
			  'q22': {'a': {'q21'}, 'b': {'q22'}, 'c': {'q23'}},
			  'q23': {'a': {'q21'}, 'b': {'q24'}, 'c': {'q21'}},
			  'q24': {'a': {'q21'}, 'b': {'q22'}, 'c': {'q23'}},

			  # bab[x]cb
			  'q3': {'a': {'q31'}, 'b': {'q31'}, 'c': {'q31', 'q4'}},
			  'q31': {'a': {'q31'}, 'b': {'q31'}, 'c': {'q32'}},
			  'q32': {'a': {'q31'}, 'b': {'q33'}, 'c': {'q32'}},
			  'q33': {'a': {'q31'}, 'b': {'q31'}, 'c': {'q32'}},
			  # babcb[x]b
			  'q4': {'a': {'q41'}, 'b': {'q41','q5'}, 'c': {'q41'}},
			  'q41': {'a': {'q41'}, 'b': {'q42'}, 'c': {'q41'}},
			  'q42': {'a': {'q41'}, 'b': {'q42'}, 'c': {'q41'}},
			  # babcb[x]
			  'q5': {'a': {'q5'}, 'b': {'q5'}, 'c': {'q5'}},
          })


def check_pattern(text: str) -> bool:
	"""
    Ground Truth: Checks if 'babcb' is split by a filler block 'x'.

    Logic:
    1. The pattern 'babcb' (length 5) exists in the string.
    2. It is split at exactly one point.
    3. The split contains a block 'x' of filler characters ([a-c]).
    4. The length of 'x' is (total_string_length - 5).

    Matches:
    xbabcb, bxabcb, baxbcb, babxcb, babcxb, babcbx
    """
	word_len = len(text)
	target_pattern = "babcb"
	pat_len = len(target_pattern)

	filler_len = word_len - pat_len

	# If the string is too short to contain the pattern, fail immediately
	if filler_len < 0:
		return False

	# Create the regex for x.
	# If filler_len is 5, this becomes "[a-c]{5}"
	x_regex = f"[a-c]{{{filler_len}}}"

	# We generate the 6 variations dynamically:
	# 1. x + babcb
	# 2. b + x + abcb
	# 3. ba + x + bcb
	# ...etc
	options = []
	for i in range(pat_len + 1):
		prefix = target_pattern[:i]
		suffix = target_pattern[i:]
		options.append(f"{prefix}{x_regex}{suffix}")

	# Join them with OR (|)
	full_regex = f"^({'|'.join(options)})$"

	# Example of what full_regex looks like for len 10:
	# ^([a-c]{5}babcb|b[a-c]{5}abcb|ba[a-c]{5}bcb|...)$

	return bool(re.match(full_regex, text))


if __name__ == "__main__":
	test = []
	accepted = []
	rejected = []

	alphabet = ['a', 'b', 'c']
	WORD_LENGTH = 12

	# 1. EFFICIENT GENERATION
	# 3^10 is 59,049 combinations. This is fast enough for Python.
	print(f"Generating all strings of length {WORD_LENGTH}...")

	# itertools.product creates the Cartesian product (equivalent to nested loops)
	# repeat=WORD_LENGTH sets the length of the string
	test = [''.join(p) for p in itertools.product(alphabet, repeat=WORD_LENGTH)]

	true_positive = 0
	false_positive = 0
	true_negative = 0
	false_negative = 0

	print(f"Testing {len(test)} strings...")

	for word in test:
		# Ensure A4 is defined in your environment
		# If A4 is meant to be your NFA object:
		try:
			nfa_accepts = A4.accepts_input(word)
		except NameError:
			print("Error: 'A4' object is not defined. Please import your NFA.");
			break

		regex_accepts = check_pattern(word)

		if nfa_accepts:
			accepted.append(word)
			if regex_accepts:
				true_positive += 1
			else:
				print(f"False Positive: {word}")
				false_positive += 1  # NFA said Yes, Regex said No
		else:
			rejected.append(word)
			if regex_accepts:
				#print(f"False Negative: {word}")
				false_negative += 1  # NFA said No, Regex said Yes
			else:
				true_negative += 1

	print(f"\n--- Results for Length {WORD_LENGTH} ---")
	print(f"Total Accepted by NFA: {len(accepted)}")
	print(f"Total Rejected by NFA: {len(rejected)}")

	# Calculation with Zero Division Safety
	total_acc = len(accepted) if len(accepted) > 0 else 1
	total_rej = len(rejected) if len(rejected) > 0 else 1

	tp_rate = (true_positive / total_acc) * 100
	fp_rate = (false_positive / total_acc) * 100
	tn_rate = (true_negative / total_rej) * 100
	fn_rate = (false_negative / total_rej) * 100

	print(f"\nTrue Positive (Agreement on Accept): {tp_rate:.4f}%")
	print(f"False Positive (NFA Accepted, Regex Rejected): {fp_rate:.4f}%")
	print(f"True Negative (Agreement on Reject): {tn_rate:.4f}%")
	print(f"False Negative (NFA Rejected, Regex Accepted): {fn_rate:.4f}%")