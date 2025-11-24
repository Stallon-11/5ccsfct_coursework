from automata.fa.nfa import NFA

def nfa_pumped(A: NFA) -> NFA:
	"""Return an NFA that recognises the pumped language of the input NFA."""

	B_transitions = {}

	# Add '0' self loops for every state.
	for state in A.states:
		existing_state_transition = A.transitions.get(state, {}) # for each state, it gets the state transition.

		# Adds the existing transitions to the new transitions.
		new_state_transition = {}
		for symbol, next_state in existing_state_transition.items():
			new_state_transition[symbol] = set(next_state)

		# if '0' transition does not exist, and add an empty set
		if '0' not in new_state_transition:
			new_state_transition['0'] = set()

		new_state_transition['0'].add(state) # if '0' self loop in this state

		B_transitions[state] = new_state_transition # updates the existing transition to the new transition.

	B = NFA(
		states=A.states,
		initial_state=A.initial_state,
		final_states=A.final_states,
		input_symbols=A.input_symbols,
		transitions=B_transitions
	)

	return B



def nfa_shuffle(A: NFA, B: NFA) -> NFA:
	"""Return an NFA that recognises the shuffled language of the input NFAs."""
	c_states = set()
	c_final_states = set()
	c_input_symbols = A.input_symbols.union(B.input_symbols)

	c_transitions = {}


	for a_state in A.states:
		for b_state in B.states:

			new_state = f"{a_state}a{b_state}b"
			c_states.add(new_state)

			if a_state in A.final_states and b_state in B.final_states:
				c_final_states.add(new_state)

			c_transitions[new_state] = {}

			symbol_list = list(c_input_symbols) + ['']

			for symbol in symbol_list:
				next_states = set()

				if a_state in A.transitions and symbol in A.transitions[a_state]:
					for next_a in A.transitions[a_state][symbol]:
						next_state = f"{next_a}a{b_state}b"
						next_states.add(next_state)

				if b_state in B.transitions and symbol in B.transitions[b_state]:
					for next_b in B.transitions[b_state][symbol]:
						next_state = f"{a_state}a{next_b}b"
						next_states.add(next_state)

				if next_states:
					c_transitions[new_state][symbol] = next_states


	# 4. Construct the NFA
	C = NFA(
		states=c_states,
		initial_state=f"{A.initial_state}a{B.initial_state}b",
		final_states=c_final_states,
		input_symbols=c_input_symbols,
		transitions=c_transitions
	)

	return C


if __name__ == '__main__':

	A =NFA(
		states={'p','q'},
		initial_state='p',
		final_states={'q'},
		input_symbols={'0','1'},
		transitions= {
			'p': {'0': {'p'}, '1': {'p', 'q'}},
			'q': {'0': {'q'}, '1': {'q'}}
		}
	)

	B = NFA(
		states={'p', 'q', 'r'},
		initial_state='p',
		final_states={'r'},
		input_symbols={'0', '1'},
		transitions={
			'p': {'0': {'p'}, '1': {'q'}},
			'q': {'0': {'r'}, '1': {'p'}},
			'r': {'0': {'q'}, '1': {'r'}},
		}
	)

	C = nfa_shuffle(A,B)
	#C.show_diagram(path="nfs.png")

	nfa_c = f"""
	NFA C:
	States: {C.states},
	initial State: {C.initial_state},
	final States: {C.final_states},
	input Symbols: {C.input_symbols},
	transitions: {C.transitions} 
	"""
	print(nfa_c)

	test = []

	symbols = ['0','1']
	accepted_a = []
	accepted_b = []


	for s1 in symbols:
		for s2 in symbols:
			for s3 in symbols:
				for s4 in symbols:
					for s5 in symbols:
						for s6 in symbols:
							for s7 in symbols:
								for s8 in symbols:
									for s9 in symbols:
										for s10 in symbols:
											for s11 in symbols:
												for s12 in symbols:
													for s13 in symbols:
														for s14 in symbols:
															for s15 in symbols:
																for s16 in symbols:
																	test.append(f"{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}{s9}{s10}{s11}{s12}{s13}{s14}{s15}{s16}")

	# Keep s if A accepts OR B accepts
	for word in test:
		if A.accepts_input(word):
			accepted_a.append(word)
		if B.accepts_input(word):
			accepted_b.append(word)

	print(f"Strings accepted by A: {len(accepted_a)}")
	print(f"Strings accepted by B: {len(accepted_b)}")

	accepted_shuffles = []
	rejected_shuffles = []

	# Let's test just the first 100 combinations to save time/memory
	# (Checking ALL combinations of valid strings might be huge)
	count = 0
	limit = 1000000000

	for a in accepted_a:
		for b in accepted_b:
			if count >= limit: break

			# --- FIXED SHUFFLE LOGIC ---
			# Zip takes one char from a, one from b, pairs them, and we join them.
			# a: "111..."
			# b: "000..."
			# result: "101010..."

			# 1. Ensure they are same length for a perfect zip (they are, both 7)
			interleaved = "".join(i + j for i, j in zip(a, b))

			# 2. Check the NFA
			if C.accepts_input(interleaved):
				accepted_shuffles.append(interleaved)
			else:
				rejected_shuffles.append(interleaved)

			count += 1
		if count >= limit: break

	print(f"\nTested {count} shuffles.")
	print(f"Accepted by C: {len(accepted_shuffles)}")
	print(f"Rejected by C: {len(rejected_shuffles)}")

	if len(rejected_shuffles) > 0:
		print(f"First rejected string: {rejected_shuffles[0]}")
	else:
		print("SUCCESS! All valid perfect shuffles were accepted.")
