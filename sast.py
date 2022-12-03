import openai
import os
import sys
from typing import List

# Set the API key to the value of the second command line argument,
# the OPENAI_API_KEY environment variable, or a default value if
# neither the command line argument nor the environment variable
# is provided.
openai_api_key = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("OPENAI_API_KEY", "default_api_key")

# Set the API key for the openai module.
openai.api_key = openai_api_key

# The directory that contains the code files to be analyzed.
# Set the directory to the first command line argument or a default
# value of "./" if no command line argument is provided.
directory = sys.argv[1] if len(sys.argv) > 1 else "./"


def check_vulnerabilities(filename: str) -> List[str]:
    # Check if the file has a code file extension.
    if os.path.splitext(filename)[1] in (".py", ".go", ".js", ".php"):
        # Read the code from the file.
        with open(filename, encoding='utf-8') as f:
            code = f.read()
        PROMPT = f"Please provide only a list of vulnerabilities and the line in which it manifests itself in the following code:\n{code}"
        MAX_TOKENS = 4000 - len(PROMPT)
        # Use GPT-3 to detect vulnerabilities in the code.
        # maybe codex?
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=PROMPT,
            temperature=0.5,
            max_tokens=MAX_TOKENS,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # Extract the list of vulnerabilities from the GPT-3 response.
        vulnerabilities = response["choices"][0]["text"].strip().split("\n")

        # Print the list of vulnerabilities detected in the code.
        print(f"Vulnerabilities in {filename}:")
        for vulnerability in vulnerabilities:
            print(f"- {vulnerability}")


# Recursively read all of the files in the specified directory and its subdirectories.
for root, dirs, files in os.walk(directory):
    for filename in files:
        check_vulnerabilities(os.path.join(root, filename))
