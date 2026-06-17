import requests
import streamlit as st
import json
import os

MEMORY_FILE = "memory.json"


def load_memory():

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as f:

            return json.load(f)

    return {}


def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:

        json.dump(memory, f, indent=4)


def career_agent(interest, skills):

    interest = interest.lower()

    skills = skills.lower()

    if "ai" in interest:

        return "Artificial Intelligence Internship"

    elif "java" in interest:

        return "Java Development Internship"

    elif "web" in interest:

        return "Web Development Internship"

    elif "python" in skills:

        return "Python Development Internship"

    else:

        return "Full Stack Development Internship"

def joke_agent():

    try:

        response = requests.get(
            "https://official-joke-api.appspot.com/random_joke",
            timeout=5
        )

        data = response.json()

        return data["setup"], data["punchline"]

    except:

        return None, None
    
memory = load_memory()

st.title("🤖 AI Internship Advisor Agent")

st.write("Multi-Agent AI System with Memory")

name = st.text_input("Enter your name")

interest = st.text_input("Enter your interests")

skills = st.text_input("Enter your skills")

if st.button("Get Recommendation"):

    if name in memory:

        st.success(f"Welcome back {name}!")

        st.info("Memory Agent remembers:")

        st.write(memory[name])

    else:

        recommendation = career_agent(interest, skills)

        st.success("Recommended Internship:")

        st.write(recommendation)

        memory[name] = recommendation

        save_memory(memory)

        st.info("Memory saved successfully!")
# Joke Agent

st.subheader("😂 Fun Fact Agent")

setup, punchline = joke_agent()

if setup:

    st.write(setup)

    st.write(punchline)

else:

    st.warning("Could not fetch joke from API.")

st.markdown("---")

st.subheader("Architecture")

st.code("""
User

↓

Career Agent
(Analyzes Interests + Skills)

↓

Internship Recommendation

↓

Memory Agent
(Saves Recommendation)

↓

Joke Agent
(Calls Public API)

↓

Displays Joke
""")