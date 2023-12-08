# Merge Sort Algorithm Implementation

This repository contains a Python implementation of the Merge Sort algorithm. Merge Sort is a divide-and-conquer sorting algorithm that divides an input array into two halves, recursively sorts each half, and then merges the sorted halves.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Function Descriptions](#function-descriptions)
- [Example](#example)
- [Performance](#performance)
- [Contributing](#contributing)
- [License](#license)

## Overview

Merge Sort is a comparison-based sorting algorithm with a time complexity of O(n log n). It is known for its stable nature and can efficiently handle large datasets.

This implementation consists of several functions:
- `mergeFunction`: Merges two sorted arrays into a single sorted array.
- `sortLeftArray`: Recursively sorts the left half of the input array.
- `sortRightArray`: Recursively sorts the right half of the input array.
- `mergeSort`: Merges two sorted arrays into a single sorted array.

## Usage

To use the Merge Sort algorithm, follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/excel-asaph/Merge-Sort-Algorithm-Implementation.git
cd Merge-Sort-Algorithm-Implementation
```

2. Open the Python interpreter or create a Python script in the same directory:

```bash
vi your-filename.py
```

3. Then, use the following code:

```python
from merge_sort import MergeSort

# Example input array
user_array = [your_array_of_values]

# Create an instance of the MergeSort class
merge_sort = MergeSort()

# Sort the array using Merge Sort
user_array = merge_sort(user_array)

# Print the sorted array
print("Sorted Array:", user_array)
```

4. Run the Python script:

```python
python3 your-filename.py
```

## Function Descriptions

### `mergeSort(array)`

Merges two sorted arrays into a single sorted array.

- **Arguments:**
  - `array` (list): The input list to be sorted.

- **Returns:**
  - `list`: A sorted list.

### `sortLeftArray(array)`

Recursively sorts the left half of the input array.

- **Arguments:**
  - `array` (list): The input list to be sorted.

- **Returns:**
  - `list`: A sorted list.

### `sortRightArray(array)`

Recursively sorts the right half of the input array.

- **Arguments:**
  - `array` (list): The input list to be sorted.

- **Returns:**
  - `list`: A sorted list.

### `mergeFunction(value1, value2)`

Merges two sorted arrays into a single sorted array.

- **Arguments:**
  - `value1` (list): The first sorted list.
  - `value2` (list): The second sorted list.

- **Returns:**
  - `list`: A merged and sorted list.

## Performance

The Merge Sort algorithm has a time complexity of O(n log n), making it efficient for large datasets. It performs well on both small and large arrays, and its stable nature makes it suitable for scenarios where maintaining the order of equal elements is essential.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



