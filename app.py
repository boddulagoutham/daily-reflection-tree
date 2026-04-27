def daily_reflection():
    q1 = input("Were all planned tasks completed today? (yes/no): ").lower()

    if q1 == "yes":
        q2 = input("Did it feel meaningful and satisfying? (yes/no): ").lower()
        if q2 == "yes":
            return "Effective and fulfilling day. Keep it up!"
        else:
            return "Tasks done but not satisfying. Align with purpose."

    else:
        reason = input("Main reason? (time/motivation/distraction): ").lower()

        if reason == "time":
            q4 = input("Did you plan your day? (yes/no): ").lower()
            if q4 == "yes":
                return "Unexpected events affected you. Add buffer time."
            else:
                return "Lack of planning. Use time-blocking."

        elif reason == "motivation":
            q5 = input("Were goals clear? (yes/no): ").lower()
            if q5 == "yes":
                return "Possible burnout. Take breaks."
            else:
                return "Unclear goals. Define them better."

        elif reason == "distraction":
            q6 = input("Type? (internal/external): ").lower()
            if q6 == "internal":
                return "Improve focus with deep work."
            else:
                return "Optimize environment."

print(daily_reflection())
