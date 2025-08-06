def vacuum_cleaner(location, status):
    actions = []
    
    if location == "A":
        if status["A"] == "Dirty":
            actions.append("Clean A")
            status["A"] = "Clean"
        actions.append("Move Right to B")
        location = "B"
        
        if status["B"] == "Dirty":
            actions.append("Clean B")
            status["B"] = "Clean"
            
    elif location == "B":
        if status["B"] == "Dirty":
            actions.append("Clean B")
            status["B"] = "Clean"
        actions.append("Move Left to A")
        location = "A"
        
        if status["A"] == "Dirty":
            actions.append("Clean A")
            status["A"] = "Clean"
    
    return actions, status

# Example: Initial setup
initial_location = "A"
room_status = {"A": "Dirty", "B": "Dirty"}

# Run the vacuum cleaner
steps, final_status = vacuum_cleaner(initial_location, room_status)

# Output the result
print("Actions taken:")
for step in steps:
    print("-", step)

print("\nFinal Room Status:")
print(final_status)
