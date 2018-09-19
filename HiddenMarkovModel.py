"""    Created by Monim on 9/11/2018.    """

input_initial_condition = []  # ['Rainy', 'Sunny']
input_initial_sequence = []  # ['Class', 'Sleep', 'Play']
input_start_probability = []  # [0.4, 0.6]
input_transition_probability = []  # [[0.8, 0.2], [0.4, 0.6]]
input_option_probability = []  # [[0.2, 0.3, 0.5], [0.4, 0.4, 0.2]]

input_test_sequence = []  # ['Class', 'Class', 'Play']

calculating_probability = []


def main():
    global input_option_probability, input_transition_probability
    # Input of Hidden Sequence
    hidden_sequence = int(input("Enter the number of Hidden Sequence: "))
    x = hidden_sequence

    print("Enter the name of " + str(x) + " Hidden sequences")
    for i in range(hidden_sequence):
        sequences = input()
        input_initial_condition.append(sequences)

    input_transition_probability = [[0] * hidden_sequence for i in range(hidden_sequence)]

    # Input of Observe Sequence
    observe_sequence = int(input("Enter the number of Observe Sequence: "))
    x = observe_sequence
    print("Enter the name of " + str(x) + " Observe sequences")
    for i in range(observe_sequence):
        sequences = input()
        input_initial_sequence.append(sequences)

    input_option_probability = [[0 * observe_sequence for i in range(observe_sequence)] for i in range(hidden_sequence)]

    # Input of Start Probability
    print("Enter the values of Start Probability")
    for i in input_initial_condition:
        start_prob = float(input("Enter value for " + i + ": "))
        input_start_probability.append(start_prob)

    # Input of Transition Probability
    print("Enter the values of Transition Probability")
    for i in range(len(input_initial_condition)):
        for j in range(len(input_initial_condition)):
            input_transition_probability[i][j] = \
                float(input("Enter value for " + input_initial_condition[i] + "->" + input_initial_condition[j] + ": "))

    # Input Value of Hidden Transition Probability
    print("Enter the values of Hidden Transition Probability")
    for i in range(len(input_initial_condition)):
        for j in range(len(input_initial_sequence)):
            print(input_initial_condition[i] + "->" + input_initial_sequence[j])
            input_option_probability[i][j] = \
                float(input("Enter value for " + input_initial_condition[i] + "->" + input_initial_sequence[j] + ": "))

    # Input of Test Sequence
    test_sequence = int(input("Enter the number of Test Sequence: "))
    x = test_sequence
    print("Enter the name of " + str(x) + " Test sequences")
    for i in range(test_sequence):
        sequences = input()
        input_test_sequence.append(sequences)

    calculate()


def get_probability(previous_probability, trans_probability, item_probability):
    return previous_probability * trans_probability * item_probability


def calculate():
    index = 0
    for test_value in input_test_sequence:

        if index == 0:
            for start in range(len(input_start_probability)):
                probability = get_probability(1, input_start_probability[start],
                                              input_option_probability[start][input_test_sequence.index(test_value)])
                calculating_probability.append(probability)
        else:
            compare(test_value)

        index += 1
    print(max(calculating_probability))


def compare(test_value):
    global calculating_probability
    temp = []
    for start in range(len(input_start_probability)):
        maximum = -1
        for value in range(len(calculating_probability)):
            probability = get_probability(calculating_probability[value],
                                          input_transition_probability[value][start],
                                          input_option_probability[start][input_test_sequence.index(test_value)])
            if probability > maximum:
                maximum = probability

        temp.append(maximum)

    calculating_probability.clear()
    calculating_probability = temp


# calculate()
main()
