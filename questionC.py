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


# def nfa_shuffle(A: NFA, B: NFA) -> NFA:
# 	"""Return an NFA that recognises the shuffled language of the input NFAs."""
#
# 	return C


