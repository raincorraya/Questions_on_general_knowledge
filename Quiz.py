import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from tkinter import PhotoImage
from PIL import Image, ImageTk

quiz_data = [
    {
        "question": "What is the capital city of France?",
        "choices": ["Paris", "London", "Madrid", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "In which year did World War II end?",
        "choices": ["1943", "1944", "1945", "1946"],
        "answer": "1945"
    },
    {
        "question": "Who wrote “Romeo and Juliet”?",
        "choices": ["Charles Dickens", "William Wordsworth", "William Shakespeare", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Saturn", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter"
    },
    {
        "question": "Which ocean is the largest?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the currency of Japan?",
        "choices": ["Yuan", "Euro", "Yen", "Dollar"],
        "answer": "Yen"
    },
    {
        "question": "Who is known as the “Father of Modern Physics”?",
        "choices": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Nikola Tesla"],
        "answer": "Albert Einstein"
    },
    {
        "question": "What is the capital of Australia?",
        "choices": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "answer": "Canberra"
    },
    {
        "question": "In which year did the Titanic sink?",
        "choices": ["1909", "1910", "1911", "1912"],
        "answer": "1912"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the longest river in the world?",
        "choices": ["Nile River", "Amazon River", "Mississippi River", "Yangtze River"],
        "answer": "Amazon River"
    },
    {
        "question": "Who was the first President of the United States?",
        "choices": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
        "answer": "George Washington"
    },
    {
        "question": "Which element has the chemical symbol “O”?",
        "choices": ["Oxygen", "Gold", "Silver", "Uranium"],
        "answer": "Oxygen"
    },
    {
        "question": "What is the national sport of Canada?",
        "choices": ["Baseball", "Soccer", "Ice Hockey", "Lacrosse"],
        "answer": "Ice Hockey"
    },
    {
        "question": "Which country is known as the “Land of the Rising Sun”?",
        "choices": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["1", "2", "3", "4"],
        "answer": "2"
    },
    {
        "question": "Who wrote “To Kill a Mockingbird”?",
        "choices": ["Harper Lee", "Mark Twain", "John Steinbeck", "J.D. Salinger"],
        "answer": "Harper Lee"
    },
    {
        "question": "Which planet is known as the “Red Planet”?",
        "choices": ["Jupiter", "Saturn", "Mars", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "answer": "Blue Whale"
    },
    {
        "question": "Who developed the theory of relativity?",
        "choices": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Nikola Tesla"],
        "answer": "Albert Einstein"
    },
    {
        "question": "What is the capital of China?",
        "choices": ["Shanghai", "Beijing", "Hong Kong", "Tokyo"],
        "answer": "Beijing"
    },
    {
        "question": "Who is the author of the “Harry Potter” series?",
        "choices": ["J.R.R. Tolkien", "George R.R. Martin", "J.K. Rowling", "C.S. Lewis"],
        "answer": "J.K. Rowling"
    },
    {
        "question": "What is the largest desert in the world?",
        "choices": ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Antarctica"],
        "answer": "Antarctica"
    },
    {
        "question": "Who painted “Starry Night”?",
        "choices": ["Pablo Picasso", "Vincent van Gogh", "Claude Monet", "Salvador Dalí"],
        "answer": "Vincent van Gogh"
    },
    {
        "question": "In which year did the Berlin Wall fall?",
        "choices": ["1987", "1988", "1989", "1990"],
        "answer": "1989"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "choices": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "What is the currency of South Africa?",
        "choices": ["Rand", "Peso", "Euro", "Dollar"],
        "answer": "Rand"
    },
    {
        "question": "Who was the first woman to win a Nobel Prize?",
        "choices": ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Florence Nightingale"],
        "answer": "Marie Curie"
    },
    {
        "question": "What is the capital of Brazil?",
        "choices": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "answer": "Brasília"
    },
    {
        "question": "Who is known as the “Queen of Pop”?",
        "choices": ["Madonna", "Beyoncé", "Lady Gaga", "Rihanna"],
        "answer": "Madonna"
    },
    {
        "question": "Which continent is known as the “Dark Continent”?",
        "choices": ["Asia", "Africa", "Europe", "Antarctica"],
        "answer": "Africa"
    },
    {
        "question": "What is the largest island in the world?",
        "choices": ["Madagascar", "Borneo", "Greenland", "New Guinea"],
        "answer": "Greenland"
    },
    {
        "question": "Who wrote “The Great Gatsby”?",
        "choices": ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "William Faulkner"],
        "answer": "F. Scott Fitzgerald"
    },
    {
        "question": "What is the speed of light?",
        "choices": ["Approximately 299,792 meters per second", "Approximately 299,792 kilometers per hour",
                    "Approximately 299,792 kilometers per second", "Approximately 299,792 miles per hour"],
        "answer": "Approximately 299,792 kilometers per second"
    },
    {
        "question": "Which country is known as the “Land of the Midnight Sun”?",
        "choices": ["Norway", "Finland", "Sweden", "Iceland"],
        "answer": "Norway"
    },
    {
        "question": "Who discovered penicillin?",
        "choices": ["Alexander Fleming", "Louis Pasteur", "Jonas Salk", "Edward Jenner"],
        "answer": "Alexander Fleming"
    },
    {
        "question": "What is the currency of Russia?",
        "choices": ["Ruble", "Euro", "Dollar", "Pound"],
        "answer": "Ruble"
    },
    {
        "question": "In which year did the first moon landing occur?",
        "choices": ["1967", "1968", "1969", "1970"],
        "answer": "1969"
    },
    {
        "question": "Who was the first woman in space?",
        "choices": ["Sally Ride", "Valentina Tereshkova", "Mae Jemison", "Peggy Whitson"],
        "answer": "Valentina Tereshkova"
    },
    {
        "question": "What is the capital of India?",
        "choices": ["Mumbai", "Delhi", "Bangalore", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which planet is known as the “Blue Planet”?",
        "choices": ["Venus", "Mars", "Earth", "Neptune"],
        "answer": "Earth"
    },
    {
        "question": "Who painted “The Last Supper”?",
        "choices": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "In which year did the United Nations (UN) come into existence?",
        "choices": ["1939", "1944", "1945", "1950"],
        "answer": "1945"
    },
    {
        "question": "What is the currency of Japan?",
        "choices": ["Yen", "Yuan", "Euro", "Dollar"],
        "answer": "Yen"
    },
    {
        "question": "Who was the first man to step on the moon?",
        "choices": ["Neil Armstrong", "Buzz Aldrin", "Michael Collins", "Alan Shepard"],
        "answer": "Neil Armstrong"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "choices": ["Tomato", "Avocado", "Onion", "Lemon"],
        "answer": "Avocado"
    },
    {
        "question": "In which year did the American Civil War end?",
        "choices": ["1862", "1863", "1864", "1865"],
        "answer": "1865"
    },
    {
        "question": "Who wrote “The Communist Manifesto”?",
        "choices": ["Karl Marx", "Friedrich Engels", "Vladimir Lenin", "Joseph Stalin"],
        "answer": "Karl Marx"
    },
    {
        "question": "What is the capital of South Korea?",
        "choices": ["Seoul", "Busan", "Incheon", "Daegu"],
        "answer": "Seoul"
    },
    {
        "question": "What is the largest continent by land area?",
        "choices": ["Africa", "Asia", "North America", "South America"],
        "answer": "Asia"
    },
    {
        "question": "Which river is the longest river in Asia?",
        "choices": ["Yangtze", "Yellow River", "Ganges", "Indus"],
        "answer": "Yangtze"
    },
    {
        "question": "Which Asian country is known as the Land of the Rising Sun?",
        "choices": ["Japan", "South Korea", "China", "Vietnam"],
        "answer": "Japan"
    },
    {
        "question": "Which Asian country is the largest by population?",
        "choices": ["India", "China", "Indonesia", "Pakistan"],
        "answer": "China"
    },
    {
        "question": "What is the capital city of Thailand?",
        "choices": ["Bangkok", "Hanoi", "Jakarta", "Kuala Lumpur"],
        "answer": "Bangkok"
    },
    {
        "question": "Which Asian city is known as the City of Love?",
        "choices": ["Tokyo", "Singapore", "Kuala Lumpur", "Paris"],
        "answer": "Paris"
    },
    {
        "question": "What is the tallest mountain in Asia?",
        "choices": ["Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer": "Everest"
    },
    {
        "question": "What is the currency of South Korea?",
        "choices": ["Yuan", "Won", "Yen", "Dollar"],
        "answer": "Won"
    },
    {
        "question": "Which Asian country is known as the Land of Smiles?",
        "choices": ["China", "Japan", "Thailand", "India"],
        "answer": "Thailand"
    },
{
    "question": "What is the largest island in Japan?",
    "choices": ["Honshu", "Hokkaido", "Kyushu", "Shikoku"],
    "answer": "Honshu"
},
{
    "question": "Which Asian country is famous for the Angkor Wat temple complex?",
    "choices": ["Thailand", "Vietnam", "Cambodia", "Indonesia"],
    "answer": "Cambodia"
}

]

score = 0
current_question = 0

def Show_Qns():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])  # Changed "Question" to "question"
    for i in range(4):
        choice_BTNS[i].config(text=question["choices"][i], state="normal")
    next_btn.config(state="disabled")

def check_answer(choice):
    global score
    question = quiz_data[current_question]
    selected_choice = question["choices"][choice]
    if selected_choice == question["answer"]:
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green", background="black")
        # Load and display an image for correct feedback
        correct_image = resize_image(r"C:\Users\User\Pictures\x\usetldr_10384376_u_10691787_image_format_X0ntv9GLhYlFDZn.png", 40, 40)  # Update with your image file path
        feedback_label.config(image=correct_image, compound="left")
        feedback_label.image = correct_image
        for button in choice_BTNS:
            button.config(state="disabled")
        next_btn.config(state="normal")
    else:
        feedback_label.config(text="Incorrect!", foreground="red", background="black")
        # Load and display an image for incorrect feedback
        incorrect_image = resize_image(r"C:\Users\User\Pictures\x\usetldr_10384376_u_10691787_image_format_fzAZLzv1wyhqoIy.png", 40, 40)  # Update with your image file path
        feedback_label.config(image=incorrect_image, compound="left")
        feedback_label.image = incorrect_image  # Keep a reference to the image to prevent garbage collection
        for button in choice_BTNS:
            button.config(state="disabled")
        next_btn.config(state="normal")


def Next_Question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        Show_Qns()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

    # Load and resize the image for the next button
    next_btn_image = resize_image(r"C:\Users\User\Pictures\x\70.png", 40, 40)  # Adjust width and height as needed
    next_btn.config(image=next_btn_image, compound=tk.LEFT)  # Position the image to the left of the text
    next_btn.image = next_btn_image  # Keep a reference to the image to prevent garbage collection

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)

root = tk.Tk()
root.title("Quiz APP")
root.geometry("1200x673")
style = Style(theme='flatly')

image_path = PhotoImage(file=r"C:\Users\User\Pictures\config\usetldr_10384376_u_10691787_image_format_sKWEfP2KHNqiKxy.png")  # Update with your image file path
bg_image = tk.Label(root, image=image_path)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)

style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

qs_label = ttk.Label(
    root,
    anchor='center',
    wraplength=500,
    padding=10
)
qs_label.place(x=50, y=50 )  # Adjust x and y coordinates as needed

choice_BTNS = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.place(x=70, y=180 + i * 50)  # Adjust x and y coordinates as needed
    choice_BTNS.append(button)

# Load image for displaying the scoreboard
image_scoreboard = PhotoImage(file=r"C:\Users\User\Pictures\x\2.0.png")
scoreboard_label = tk.Label(root, image=image_scoreboard)
scoreboard_label.place(x=1000, y=500)  # Adjust x and y coordinates as needed

feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.place(x=20, y=590)  # Adjust x and y coordinates as needed
next_btn = ttk.Button(
    root,
    text="Next",
    command=Next_Question,
    state="disabled"
)
next_btn.place(x=570, y=500)  # Adjust x and y coordinates as needed

# Load and resize the image for the next button
next_btn_image = resize_image(r"C:\Users\User\Pictures\x\70.png", 40, 40)  # Adjust width and height as needed
next_btn.config(image=next_btn_image, compound=tk.LEFT)  # Position the image to the left of the text
next_btn.image = next_btn_image  # Keep a reference to the image to prevent garbage collection

next_btn.place(x=570, y=500)  # Adjust x and y coordinates as needed

# Adjusting the score label to appear on the scoreboard image
score_label = ttk.Label(
    root,
    anchor='center',
    text="Score: 0/{}".format(len(quiz_data)),
    padding=10
)
score_label.place(x=1003, y=509)  # Adjust x and y coordinates as needed to position it on the scoreboard image

Show_Qns()

root.mainloop()