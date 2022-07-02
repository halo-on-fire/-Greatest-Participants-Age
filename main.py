participants = []
numberOfParticipants = int(input("Enter number of participants: "))

for i in range(numberOfParticipants):
    participant = {}
    participantName = input("Enter participant's Name: ")
    participantAge = int(input("Enter participant's Age: "))
    participant['name'] = participantName
    participant['age'] = participantAge
    participants.append(participant)
    
print(participants)
    
BiggerAge = max(participants, key = lambda x:x['age'])
print(BiggerAge)