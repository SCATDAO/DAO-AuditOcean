import json
import matplotlib.pyplot as plt
import numpy as np

def visualize_histogram(datum):

    data = datum['array']

    flattened_data = np.concatenate(data)

    print(flattened_data)

    # Calculate the maximum value from the flattened array
    max_value = np.amax(flattened_data)

    # Create a histogram with a sufficient number of bins
    bins = np.arange(max_value + 2)
    hist, _ = np.histogram(flattened_data, bins=bins)

    # Normalize the histogram
    hist = hist / flattened_data.size

    # Plot the histogram
    plt.bar(np.arange(max_value + 1), hist, edgecolor='white')

    # Adding labels and title
    plt.xlabel('Index')
    plt.ylabel('Frequency')
    plt.title('Index Distribution ' + str(datum['iterations']) + " Iterations" )

    # Displaying the plot
    plt.show()



with open('arrayData.json') as file:
         data = json.load(file)
        
         visualize_histogram(data)

         



