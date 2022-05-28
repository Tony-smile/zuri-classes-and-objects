class Student:
    # [assignment] Skeleton class. Add your code here
   
   
    def __init__(self, name, age, tracks, score):
        #ensures value imputed by user is string
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name Must be a string")

            #ensures age is an integer 
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError("Age Must be an integer")  

            #ensures track is in a list
        if isinstance(tracks, list):
            self.tracks = tracks
        else:
            raise ValueError("Tracks Must contain a list")

            #ensures scores is in float
        if isinstance(score, float):
            self.score = score
        else:
            raise ValueError(" Score Must be in float")
        
        print(f"A new student added, Welcome: {self.name} your Track is: {self.tracks}")

    def change_name(self, new_name : str):
        #ensures new name is a string
        if isinstance(new_name, str):
            print(f"{self.name} just changed name to {new_name}")
            self.name = new_name
        else:
            raise ValueError("Name must be a string")

    def change_age(self, new_age : int):

        #ensures new age is an integer 
        if isinstance(new_age, int):
            print( f"{self.name}  just updated age from {self.age} to: {new_age}")
            self.age = new_age
          
        else:
            raise ValueError("Age Must be an integer")    
        self.age = new_age
    def add_tracks(self, *tracks):

        #ensures new track is a list
        self.tracks += tracks
        print(f"{self.name} Added {tracks} to {self.tracks}")
    
    def get_score(self):
        print(f"{self.name} Score is : {self.score}" )

#Creating first student Bob
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Justin")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
print(Bob.tracks)
print(Bob.get_score())
print(Bob.age)
print(Bob.name
)
#creating second student Tony
Tony = Student(
    name="Tony",
    age=25,
    tracks=["FE", "BE", "UI/UX"],
    score=30.0
)

Tony.add_tracks("Full-stack")
print(Tony.tracks)
Tony.change_name("Chinedu")
Tony.change_age(26)
print(Tony.name.upper())

Bob.add_tracks("Full-stack", "Designer")
print(Bob.tracks)