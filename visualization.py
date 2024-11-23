import json
import pandas as pd
import matplotlib.pyplot as plt

with open('experimentTimes.json', 'r') as file:
    data = json.load(file)


js_times = pd.DataFrame(data['javascript'])
wasm_times = pd.DataFrame(data['wasm'])


merged_data = pd.merge(js_times, wasm_times, on='n', suffixes=('_js', '_wasm'))


print(merged_data)


plt.figure(figsize=(12, 6))
plt.plot(merged_data['n'], merged_data['time_js'], label='JavaScript', marker='o')
plt.plot(merged_data['n'], merged_data['time_wasm'], label='WebAssembly', marker='o')

plt.title('Fibonacci Execution Time Comparison')
plt.xlabel('Fibonacci Number (n)')
plt.ylabel('Execution Time (ms)')
plt.xticks(merged_data['n'])  
plt.legend()
plt.grid()
plt.yscale('log')  
plt.show()
