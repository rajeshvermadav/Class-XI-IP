statecapital = {"Andhra Pradesh":"Hyderbad", "Bihar":"Patna","Maharashtra":"Mumbai","Rajasthan":"Jaipur"}
print(statecapital)
statecapital["punjab"]= "Chandigarh"
print(statecapital)
print("Himachal" in statecapital)
print(len(statecapital))
del statecapital['Bihar']
print(statecapital)
print(statecapital.items())


