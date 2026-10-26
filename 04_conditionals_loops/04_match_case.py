command = input("Command (start/stop/halt/other): ")

match command:
    case "start":
        print("Starting")
    case "stop" | "halt":
        print("Stopping")
    case _:
        print("Unknown command")