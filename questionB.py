from automata.fa.nfa import NFA

A_r = NFA(
    states = {'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11'},
    initial_state='q0',
    final_states = {'q11'},
    input_symbols={'a','b', 'c'},
    transitions = {
        # cb U (aa)*
        'q0': {'': {'q1', 'q9'}},

       	# cb: 'c' --> '' --> 'b'
        'q1': {'c': {'q2'}},       # 'c'
        'q2': {'': {'q3'}},        # ''
        'q3': {'b': {'q4'}},       # 'b'
        'q4': {'': {'q11'}},       # Jumps to accept state


        # (aa)*: '' --> 'a' --> '' --> 'a' --> ''

        'q9': {'': {'q5', 'q10'}},

        # 'a' --> '' --> 'a'
        'q5': {'a': {'q6'}},       # 'a'
        'q6': {'': {'q7'}},        # ''
        'q7': {'a': {'q8'}},       # 'a'

        # * Loop Back
        'q8': {'': {'q5', 'q10'}},

        'q10': {'': {'q11'}},      # Jump to accept state, since * loop finished.


        'q11': {}, # accept state
    }
)
