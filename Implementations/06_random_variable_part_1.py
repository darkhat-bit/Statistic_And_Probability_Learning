import numpy as np

# Server Outage Scenario
server_states = {
    "offline": 0,
    "degraded": 1,
    "operational": 2
}

state_probs = {
    "offline": 0.1,
    "degraded": 0.2,
    "operational": 0.7
}

states_list = list(server_states.keys())
values_list = list(server_states.values())
probs_list = list(state_probs.values())

simulated_Y = np.random.choice(values_list, size=1000, p=probs_list)

print("Sample outcomes (first 20):", simulated_Y[:20])
print("Mapping used:", server_states)
print()

# Token Prediction Random Variable
vocab_mapping = {
    "AI": 1,
    "is": 2,
    "the": 3,
    "future": 4
}

token_probs = {
    "AI": 0.4,
    "is": 0.3,
    "the": 0.2,
    "future": 0.1
}

words_list = list(vocab_mapping.keys())
values_list = list(vocab_mapping.values())
probs_list = list(token_probs.values())

predicted_W = np.random.choice(values_list, size=1, p=probs_list)
predicted_word = words_list[values_list.index(predicted_W[0])]


print("Random variable value chosen:", predicted_W[0])
print("Corresponding word:", predicted_word)

