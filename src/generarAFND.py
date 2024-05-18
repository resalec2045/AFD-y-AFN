from automathon import NFA

## Epsilon Transition is denoted by '' -> Empty string
q = {'q1', 'q2', 'q3', 'q4'}
sigma = {'0', '1'}
delta = {
    'q1' : {
            '0' : {'q1'},
            '1' : {'q1', 'q2'}
            },
    'q2' : {
            '0' : {'q3'},
            '' : {'q3'}
            },
    'q3' : {
            '1' : {'q4'},
            },
    'q4' : {
            '0' : {'q4'},
            '1' : {'q4'},
            },
}
initial_state = 'q1'
f = {'q4'}

automata = NFA(q, sigma, delta, initial_state, f)

# If you want to add custom styling, you can use the following
automata.view(
    file_name="models/COSO2",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)