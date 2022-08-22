coding = False

def coding_club_pitch(coding):
    if not coding:
        print("Don't worry, no experience is needed.")
        coding += 1
        coding_club_pitch(coding)
    else:
        print("Join the coding club!")
        print("Thurs and Fri in Room 752.")

coding_club_pitch(coding)


