def read_file_to_string(filename):
  """Reads the content of a file and returns it as a string.

  Args:
    filename: The name of the file to read.

  Returns:
    A string containing the content of the file.
  """
  try:
    with open(filename, 'r') as f:
      return f.read()
  except FileNotFoundError:
    return None  # Or raise an exception if you prefer

if __name__ == '__main__':
    # Example usage:
    file_content = read_file_to_string('prompt\COT_combine_system_prompt.txt')  # Replace 'your_file.txt' with the actual filename

    if file_content:
        print(file_content)
    else:
        print("File not found.")