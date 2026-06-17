import json
import os
import requests

MEMORY_FILE = "memory.json"


# ==========================
# Load Memory
# ==========================

def load_memory():

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as f:

            return json.load(f)

    return {}


# ==========================
# Save Memory
# ==========================

def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:

        json.dump(memory, f, indent=4)


# ==========================
# Career Agent
# ==========================

def career_agent(interest, skills):

    interest = interest.lower()

    skills = skills.lower()

    if "ai" in interest:

        return "Artificial Intelligence Internship"

    elif "web" in interest:

        return "Web Development Internship"

    elif "python" in skills:

        return "Python Development Internship"

    elif "design" in interest:

        return "UI/UX Internship"
    
    elif "java" in interest:

        return "Java Development Internship"

    else:

        return "Full Stack Development Internship"


# ==========================
# Memory Agent
# ==========================

def memory_agent(name, recommendation, memory):

    memory[name] = recommendation

    save_memory(memory)


# ==========================
# Quote Agent (API)
# ==========================

def quote_agent():

    try:

        url = "https://official-joke-api.appspot.com/random_joke"

        response = requests.get(url)

        data = response.json()

        print("\n😂 Fun Fact Agent Activated")

        print("\n" + data["setup"])

        print(data["punchline"])

    except Exception as e:

        print("\nAPI could not be reached.")

        print(e)

# ==========================
# Main Program
# ==========================

memory = load_memory()

print("\n===================================")

print(" AI Internship Advisor Agent ")

print("===================================\n")

name = input("Enter your name: ")

# Check Memory

if name in memory:

    print(f"\nWelcome back {name}!")

    print("\nMemory Agent says:")

    print("I remember your recommendation:")

    print(memory[name])

else:

    print("\nCareer Agent Activated\n")

    interest = input("Enter your interests: ")

    skills = input("Enter your skills: ")

    recommendation = career_agent(interest, skills)

    print("\nRecommended Internship:")

    print(recommendation)

    # Save using Memory Agent

    memory_agent(name, recommendation, memory)

    print("\nMemory Saved Successfully!")

# API Agent

print("\nQuote Agent Activated")

quote_agent()

print("\nThank you for using the AI Agent!")