from rich import print
import api

def conversation_loop():
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'see ya scooby':
                print("Scooby: Goodbye!")
                break
            # Send user input to API and get response
            response = api.get_response(user_input)
            print(f"Scooby: {response}")
    except KeyboardInterrupt:
        print("Scooby: Interrupt received. Exiting...")
    finally:
        # Clean up resources
        pass