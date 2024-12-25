from rich import print
import api
import db
import uuid

def conversation_loop():
    # Generate a unique session ID for this conversation
    session_id = str(uuid.uuid4())
    print("[bold blue]Starting new conversation session...[/bold blue]")

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'see ya scooby':
                print("Scooby: Goodbye!")
                break

            # Store user message
            db.store_message(session_id, "user", user_input)

            # Get conversation history
            conversation_history = db.get_session_history(session_id)

            # Get response from API with history
            response = api.get_response(user_input, conversation_history)

            # Store assistant's response
            db.store_message(session_id, "assistant", response)

            print(f"Scooby: {response}")

    except KeyboardInterrupt:
        print("\nScooby: Interrupt received. Exiting...")
    finally:
        # Clean up resources if needed
        pass