import requests
import json
import numpy as np

# Generate large matrices
matrix_size = 10
matrix1 = np.random.rand(matrix_size, matrix_size).tolist()
matrix2 = np.random.rand(matrix_size, matrix_size).tolist()

# Endpoint URL
url = "http://localhost:8000/tasks"

# Define the payload
payload = {
    "A": {"matrix": matrix1},
    "B": {"matrix": matrix2}
}

# Send burst of requests
num_requests = 1
for _ in range(num_requests):
    response = requests.post(url, json=payload)
    print(response.status_code)
    print(response.json())  # Print the response for debugging

