import argparse
import ollama
import pyperclip
from pathlib import Path

prompt_path = Path('env/prompt.txt')
sys_prompt = prompt_path.read_text()

def read_code_clip():
    return pyperclip.paste()

def explain_code(code):
    response = ollama.chat(
        model= 'deepseek-coder:latest',
        messages=[
            {
                'role': 'system', 
                'content': sys_prompt
            },
            {
                'role':'user',
                'content': f'Explain the code \n\n{code}'
            }
        ],
        
    )
    return response['message']['content']



def main():
    parser = argparse.ArgumentParser(description="Coding assistant for VS Code.")
    parser.add_argument("--clipboard", action="store_true", help="Use clipboard as code input")
    args = parser.parse_args()
    
    code = read_code_clip()

    print(explain_code(code))


if __name__ == "__main__":
    main()