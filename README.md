# openai-SAST

openai-SAST is a static analysis tool that uses the OpenAI API to detect vulnerabilities in code files. It currently supports Python, Go, JavaScript, and PHP code files, but can be easily extended to support other languages.

## Installation

Before using openai-SAST, you need to install its dependencies. The required dependencies are specified in the `requirements.txt` file. You can install these dependencies using `pip`:

```
pip install -r requirements.txt
```

Alternatively, you can install the dependencies using `conda`:

```
conda install --file requirements.txt
```

## Usage

To use openai-SAST, you need an API key for the OpenAI API. You can provide the API key as the second command line argument when running the `openai-SAST.py` script:

```
python openai-SAST.py <directory> <api_key>
```

Alternatively, you can set the `OPENAI_API_KEY` environment variable with your API key and run the script without providing the key as a command line argument:

```
export OPENAI_API_KEY=<api_key>
python openai-SAST.py <directory>
```

The `<directory>` argument specifies the directory that contains the code files to be analyzed. If no directory is specified, the current directory (`.`) will be used.

## Output

openai-SAST will recursively read all of the code files in the specified directory and its subdirectories and use the OpenAI API to detect vulnerabilities in the code. The detected vulnerabilities will be printed to the console in the following format:

```
Vulnerabilities in <filename>:
- <vulnerability> on line <line_number>
- <vulnerability> on line <line_number>
- ...
```

## Limitations

Currently, openai-SAST only detects vulnerabilities and does not provide any information on how to fix them. Additionally, it is only as accurate as the OpenAI model it uses, so false positives and false negatives may occur. It is recommended to manually review the detected vulnerabilities to verify their accuracy. 
