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
			c_states.add(new_state) # adds states for NFA C

			# adds final states for NFA C
			if a_state in A.final_states and b_state in B.final_states:
				c_final_states.add(new_state)

			c_transitions[new_state] = {}

			symbol_list = list(c_input_symbols) + [''] # Converts symbols into a list and add adds '' - epsilon

			for symbol in symbol_list:
				next_states = set()

				# Adds transition from a_state to the next_a state given a symbol
				if a_state in A.transitions and symbol in A.transitions[a_state]:
					for next_a in A.transitions[a_state][symbol]:
						next_state = f"{next_a}a{b_state}b" # change a, keep b
						next_states.add(next_state)

				# Adds transition from b_state to the next_b state given a symbol
				if b_state in B.transitions and symbol in B.transitions[b_state]:
					for next_b in B.transitions[b_state][symbol]:
						next_state = f"{a_state}a{next_b}b" # keep a, change b
						next_states.add(next_state)

				if next_states:
					c_transitions[new_state][symbol] = next_states


	# Construct the NFA
	C = NFA(
		states=c_states,
		initial_state=f"{A.initial_state}a{B.initial_state}b",
		final_states=c_final_states,
		input_symbols=c_input_symbols,
		transitions=c_transitions
	)

	return C

