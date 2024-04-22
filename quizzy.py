import streamlit as st
from PIL import Image

img = Image.open('ball.jpg')
st.image(img, caption='The epl ball')

img2 = Image.open('stadium.jpg')
st.sidebar.image(img2, caption='The arena')

# Title
st.title('Welcome to the Premier League Quiz')
st.subheader('Can you get a perfect score?')
st.subheader('Click the button to begin')

#Main game function

def premier_league_quiz():
    questions_answers = [
        ["1. Which player scored the fastest hat-trick in the Premier League?", "Sadio Mane"],
        ["2. Which player, with 653 games, has made the most Premier League appearances?", "Gareth Barry"],
        ["3. With 260 goals, who is the Premier League's all-time top scorer?", "Alan Shearer"],
        ["4. When was the inaugural Premier League season?", "1992-93"],
        ["5. Which team won the first Premier League title?", "Manchester United"],
        ["6. With 202 clean sheets, which goalkeeper has the best record in the Premier League?", "Petr Cech"],
        ["7. Which team has gone unbeaten in a 38-game season?", "Arsenal"],
        ["8. The fastest goal scored in Premier League history came in 7.69 seconds. Who scored it?", "Shane Long"]
    ]

    score = 0    #initialize game score to start from zero

    if st.button("Start Quiz"):
        st.session_state.quiz_started = True  #session state keeps the game from restarting when you click

    if st.session_state.get("quiz_started", False):
        for i in range(len(questions_answers)):
            qa = questions_answers[i]
            question_text = "Question " + str(i + 1) + ": " + qa[0]
            user_answer = st.text_input(question_text, key="answer_" + str(i))

           
            if user_answer.strip().lower() == qa[1].lower():
                if user_answer:
                    st.write("Correct!")
                    score += 1
            elif user_answer:
                st.write("Incorrect!")
                st.write("The correct answer is: " + qa[1])

                
    

        st.write("Quiz complete! You scored " + str(score) + "/" + str(len(questions_answers)) + ".")

# Run the app
if __name__ == "__main__":
    premier_league_quiz()