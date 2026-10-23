from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------- DOCTORS ----------------

doctors = [
    {
        "name": "Dr. Rahul Sharma",
        "specialization": "General Physician",
        "fee": "₹500",
        "days": "Monday to Friday"
    },
    {
        "name": "Dr. Anjali Mehta",
        "specialization": "Cardiologist",
        "fee": "₹800",
        "days": "Monday to Saturday"
    },
    {
        "name": "Dr. Neha Kapoor",
        "specialization": "Dermatologist",
        "fee": "₹700",
        "days": "Monday to Friday"
    },
    {
        "name": "Dr. Amit Verma",
        "specialization": "Pediatrician",
        "fee": "₹600",
        "days": "Monday to Saturday"
    },
    {
        "name": "Dr. Priya Singh",
        "specialization": "Gynecologist",
        "fee": "₹750",
        "days": "Monday to Friday"
    },
    {
        "name": "Dr. Raj Malhotra",
        "specialization": "Orthopedic",
        "fee": "₹700",
        "days": "Monday to Saturday"
    },
    {
        "name": "Dr. Sneha Gupta",
        "specialization": "Neurologist",
        "fee": "₹900",
        "days": "Monday to Friday"
    },
    {
        "name": "Dr. Karan Joshi",
        "specialization": "ENT Specialist",
        "fee": "₹650",
        "days": "Monday to Friday"
    },
    {
        "name": "Dr. Pooja Agarwal",
        "specialization": "Dentist",
        "fee": "₹500",
        "days": "Monday to Saturday"
    },
    {
        "name": "Dr. Vivek Sharma",
        "specialization": "Ophthalmologist",
        "fee": "₹600",
        "days": "Monday to Friday"
    }
]


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CHATBOT ----------------

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    question = data.get("question", "").lower().strip()

    # OPD
    if "opd" in question or "out patient" in question:
        answer = (
            "OPD timing is 9:00 AM to 2:00 PM. "
            "Please visit the hospital during OPD hours."
        )

    # DOCTORS LIST
    elif (
        "doctor" in question
        or "doctors" in question
        or "specialist" in question
        or "specialization" in question
        or "specialisation" in question
    ):
        answer = "Available doctors and specializations:<br><br>"

        for i, doctor in enumerate(doctors, start=1):
            answer += (
                f"{i}. {doctor['name']} - "
                f"{doctor['specialization']} - "
                f"{doctor['fee']} - "
                f"Available {doctor['days']}<br>"
            )

    # GENERAL PHYSICIAN
    elif (
        "general physician" in question
        or "physician" in question
        or "fever" in question
        or "cold" in question
    ):
        answer = (
            "General Physician: Dr. Rahul Sharma<br>"
            "Consultation Fee: ₹500<br>"
            "Available Monday to Friday."
        )

    # CARDIOLOGIST
    elif (
        "cardiologist" in question
        or "cardiology" in question
        or "heart" in question
    ):
        answer = (
            "Cardiologist: Dr. Anjali Mehta<br>"
            "Consultation Fee: ₹800<br>"
            "Available Monday to Saturday."
        )

    # DERMATOLOGIST
    elif (
        "dermatologist" in question
        or "skin" in question
        or "dermatology" in question
    ):
        answer = (
            "Dermatologist: Dr. Neha Kapoor<br>"
            "Consultation Fee: ₹700<br>"
            "Available Monday to Friday."
        )

    # PEDIATRICIAN
    elif (
        "pediatrician" in question
        or "paediatrician" in question
        or "child doctor" in question
        or "children doctor" in question
    ):
        answer = (
            "Pediatrician: Dr. Amit Verma<br>"
            "Consultation Fee: ₹600<br>"
            "Available Monday to Saturday."
        )

    # GYNECOLOGIST
    elif (
        "gynecologist" in question
        or "gynaecologist" in question
        or "gynecology" in question
    ):
        answer = (
            "Gynecologist: Dr. Priya Singh<br>"
            "Consultation Fee: ₹750<br>"
            "Available Monday to Friday."
        )

    # ORTHOPEDIC
    elif (
        "orthopedic" in question
        or "orthopaedic" in question
        or "bone" in question
        or "joint" in question
    ):
        answer = (
            "Orthopedic: Dr. Raj Malhotra<br>"
            "Consultation Fee: ₹700<br>"
            "Available Monday to Saturday."
        )

    # NEUROLOGIST
    elif (
        "neurologist" in question
        or "neurology" in question
        or "brain" in question
    ):
        answer = (
            "Neurologist: Dr. Sneha Gupta<br>"
            "Consultation Fee: ₹900<br>"
            "Available Monday to Friday."
        )

    # ENT
    elif (
        "ent" in question
        or "ear" in question
        or "nose" in question
        or "throat" in question
    ):
        answer = (
            "ENT Specialist: Dr. Karan Joshi<br>"
            "Consultation Fee: ₹650<br>"
            "Available Monday to Friday."
        )

    # DENTIST
    elif (
        "dentist" in question
        or "dental" in question
        or "tooth" in question
        or "teeth" in question
    ):
        answer = (
            "Dentist: Dr. Pooja Agarwal<br>"
            "Consultation Fee: ₹500<br>"
            "Available Monday to Saturday."
        )

    # OPHTHALMOLOGIST
    elif (
        "ophthalmologist" in question
        or "ophthalmology" in question
        or "eye" in question
        or "vision" in question
    ):
        answer = (
            "Ophthalmologist: Dr. Vivek Sharma<br>"
            "Consultation Fee: ₹600<br>"
            "Available Monday to Friday."
        )

    # APPOINTMENT
    elif (
        "appointment" in question
        or "book" in question
        or "booking" in question
    ):
        answer = (
            "You can book a doctor appointment through our "
            "appointment service. Please select the required "
            "doctor and specialization."
        )

    # CANCEL APPOINTMENT
    elif (
        "cancel appointment" in question
        or "cancel booking" in question
        or "cancellation" in question
    ):
        answer = (
            "Your appointment cancellation request can be "
            "processed through the appointment service."
        )

    # RESCHEDULE
    elif (
        "reschedule" in question
        or "change appointment" in question
        or "change booking" in question
    ):
        answer = (
            "You can reschedule your appointment through the "
            "appointment service."
        )

    # FEE
    elif (
        "fee" in question
        or "fees" in question
        or "consultation fee" in question
        or "price" in question
        or "cost" in question
    ):
        answer = (
            "Consultation fees depend on the doctor and specialization. "
            "Ask for a specific specialist to see the consultation fee."
        )

    # EMERGENCY
    elif (
        "emergency" in question
        or "urgent" in question
    ):
        answer = (
            "Emergency department is available 24 hours. "
            "For a serious emergency, please contact emergency staff immediately."
        )

    # REGISTRATION COUNTER
    elif (
        "registration" in question
        or "counter" in question
        or "reception" in question
    ):
        answer = (
            "Registration counter is open from 8:00 AM to 4:00 PM."
        )

    # ADDRESS / LOCATION
    elif (
        "address" in question
        or "location" in question
        or "where is hospital" in question
        or "hospital location" in question
    ):
        answer = (
            "Hospital address: Main Hospital Road, City.<br>"
            "Please contact the hospital reception for exact directions."
        )

    # CONTACT
    elif (
        "contact" in question
        or "phone" in question
        or "number" in question
    ):
        answer = (
            "For hospital contact information, please contact "
            "the hospital reception."
        )

    # HOSPITAL SERVICES
    elif (
        "service" in question
        or "services" in question
        or "facility" in question
        or "facilities" in question
    ):
        answer = (
            "Hospital services include:<br>"
            "• OPD consultation<br>"
            "• Doctor appointments<br>"
            "• Emergency services<br>"
            "• Registration<br>"
            "• Consultation services<br>"
            "• General hospital support"
        )

    # HELP
    elif (
        "help" in question
        or "hi" in question
        or "hello" in question
        or "what can you do" in question
    ):
        answer = (
            "I can provide information about:<br>"
            "• Doctors and specializations<br>"
            "• Consultation fees<br>"
            "• OPD timings<br>"
            "• Doctor availability<br>"
            "• Appointments<br>"
            "• Emergency services<br>"
            "• Registration counter<br>"
            "• Hospital address and services"
        )

    # DEFAULT
    else:
        answer = (
            "Sorry, I didn't understand. "
            "Please ask about doctors, specializations, "
            "appointments, OPD, fees, emergency, registration "
            "or hospital services."
        )

    return jsonify({"answer": answer})


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)