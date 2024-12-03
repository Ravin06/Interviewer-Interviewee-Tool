import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def elaborate_comments(input_text):
    elaborated_text = input_text

    if "skills" in input_text.lower():
        elaborated_text = f"Improvement Opportunity: It seems that skills were a concern. The applicant can improve by enhancing both technical and soft skills."
    elif "experience" in input_text.lower():
        elaborated_text = f"Improvement Opportunity: Experience appears to be a factor. The applicant could improve by gaining more hands-on experience in his specific role."
    elif "availability" in input_text.lower():
        elaborated_text = f"Improvement Opportunity: Availability may have been an issue. The applicant could improve by being more flexible with their schedule and showing readiness for varied shifts or on-call tasks."
    elif "fit" in input_text.lower():
        elaborated_text = f"Improvement Opportunity: Cultural fit could be a challenge. The applicant might improve by aligning more with the values and culture of the organization."
    else:
        elaborated_text = f"Improvement Opportunity: The applicant can enhance their profile by addressing areas such as skills, experience, and team dynamics, which could make them a better fit for this role."

    return elaborated_text


def display_reason():
    selected_reason = reason_combobox.get()
    comments = comments_textbox.get("1.0", "end").strip()

    if selected_reason == "6) Other":
        if not comments:
            message_label.config(text="Response is required for 'Other'.")
            return

        elaborated_feedback = elaborate_comments(comments)
        response_text = reasons_dict.get(selected_reason, "We are not hiring at this time.")
        message_label.config(text=f"{response_text}\n\nElaborated Feedback: {elaborated_feedback}")
        return

    response_text = reasons_dict.get(selected_reason, "We are not hiring at this time.")
    additional_comments = f"\nAdditional Comments: {comments}" if comments else ""
    message_label.config(text=response_text + additional_comments)

reasons_dict = {
    "1) Too many applicants": "We have received too many applications for this position.",
    "2) Internal hiring": "We have decided to hire internally for this position.",
    "3) Skills did not match": "The skills of the applicants did not match our requirements.",
    "4) Position no longer needed": "We no longer need to fill this position.",
    "5) Busy schedule": "We are too busy to conduct interviews at this time.",
    "6) Other": "Additional details below:"
}

root = ttk.Window(themename="superhero")
root.title("Reason for Not Hiring")
root.geometry("700x600")
root.resizable(True, True)

header_label = ttk.Label(root, text="Select the Reason for Not Hiring", font=("Roboto", 16), anchor="center")
header_label.pack(pady=15)

reason_combobox = ttk.Combobox(
    root,
    values=list(reasons_dict.keys()),
    state="readonly",
    font=("Roboto", 12),
    bootstyle="info"
)
reason_combobox.set("Select a reason")
reason_combobox.pack(pady=15)

comments_label = ttk.Label(root, text="Additional Comments (Optional):", font=("Roboto", 12), anchor="w")
comments_label.pack(pady=10, padx=20, anchor="w")

comments_textbox = ttk.Text(root, height=8, width=60, font=("Roboto", 12))
comments_textbox.pack(pady=5, padx=20)

submit_button = ttk.Button(root, text="Submit", command=display_reason, bootstyle="primary")
submit_button.pack(pady=15)

message_label = ttk.Label(root, text="", font=("Roboto", 12), wraplength=650, justify="center")
message_label.pack(pady=10)

root.mainloop()
