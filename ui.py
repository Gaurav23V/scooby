import api
import db
import uuid
import time
import sys
from colorama import init, Fore, Style
from datetime import datetime

# Initialize colorama
init()

def type_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def print_session_header():
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Session Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Type 'see ya scooby' to end the session{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n")

def conversation_loop():
    session_id = str(uuid.uuid4())
    print_session_header()

    try:
        while True:
            # Get user input with blue color
            user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}")
            if user_input.lower() == 'see ya scooby':
                print(f"{Fore.GREEN}Scooby: Goodbye! Have a great day!{Style.RESET_ALL}")
                break

            # Store user message
            db.store_message(session_id, "user", user_input)

            # Get conversation history
            conversation_history = db.get_session_history(session_id)

            # Get streaming response
            sys.stdout.write(f"{Fore.GREEN}Scooby: {Style.RESET_ALL}")
            sys.stdout.flush()

            response_stream = api.get_streaming_response(user_input, conversation_history)
            full_response = ""

            # Display streaming response
            for chunk in response_stream:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    sys.stdout.write(content)
                    sys.stdout.flush()
                    full_response += content
                    time.sleep(0.02)
            print()  # New line after response

            # Store assistant's response
            db.store_message(session_id, "assistant", full_response)

    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}Scooby: Interrupt received. Exiting...{Style.RESET_ALL}")