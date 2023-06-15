import random
a = int(input("enter a random number to activate the invisible magic spinner"))
division1_golf_colleges = [
    "University of Alabama",
    "Arizona State University",
    "University of Arkansas",
    "Auburn University",
    "Baylor University",
    "University of California, Berkeley",
    "University of California, Los Angeles (UCLA)",
    "University of Colorado Boulder",
    "Duke University",
    "University of Florida",
    "Florida State University",
    "University of Georgia",
    "Georgia Tech",
    "University of Illinois at Urbana-Champaign",
    "Indiana University Bloomington",
    "University of Iowa",
    "University of Kansas",
    "University of Kentucky",
    "Louisiana State University (LSU)",
    "University of Louisville",
    "University of Maryland",
    "University of Miami",
    "University of Michigan",
    "Michigan State University",
    "University of Minnesota",
    "University of Mississippi (Ole Miss)",
    "University of Missouri",
    "University of Nebraska-Lincoln",
    "University of Nevada, Las Vegas (UNLV)",
    "University of New Mexico",
    "University of North Carolina at Chapel Hill",
    "Northwestern University",
    "University of Notre Dame",
    "Ohio State University",
    "University of Oklahoma",
    "Oklahoma State University",
    "University of Oregon",
    "Oregon State University",
    "University of Pennsylvania",
    "University of South Carolina",
    "University of Southern California (USC)",
    "University of South Florida",
    "Stanford University",
    "Syracuse University",
    "University of Tennessee",
    "Texas A&M University",
    "Texas Christian University (TCU)",
    "University of Texas at Austin",
    "Texas Tech University",
    "University of Utah",
    "Vanderbilt University",
    "University of Virginia",
    "Virginia Tech",
    "Wake Forest University",
    "Washington State University",
    "University of Washington",
    "West Virginia University",
    "University of Wisconsin-Madison",
    "Yale University"
]

division2_golf_colleges = [
    "Adelphi University",
    "Anderson University (SC)",
    "Arkansas Tech University",
    "Barry University",
    "Barton College",
    "Belmont Abbey College",
    "Bentley University",
    "Brevard College",
    "California State University, Chico",
    "California State University, East Bay",
    "California State University, Monterey Bay",
    "Carson-Newman University",
    "Central Missouri State University",
    "Chaminade University",
    "Coker University",
    "Colorado School of Mines",
    "Concordia University (OR)",
    "Cumberland University",
    "Dominican University of California",
    "East Central University",
    "Flagler College",
    "Florida Southern College",
    "Georgia Southwestern State University",
    "Grand Valley State University",
    "Hawaii Pacific University",
    "Henderson State University",
    "Indianapolis (University of)",
    "Johnson & Wales University (FL)",
    "King University",
    "Lake Erie College",
    "Lee University",
    "Lewis University",
    "Limestone College",
    "Lincoln Memorial University",
    "Lynn University",
    "Malone University",
    "Mansfield University",
    "McKendree University",
    "Mercyhurst University",
    "Metropolitan State University of Denver",
    "Midwestern State University",
    "Minnesota State University, Mankato",
    "Missouri Western State University",
    "Molloy College",
    "Montevallo (University of)",
    "Newberry College",
    "Northeastern State University",
    "Northern Michigan University",
    "North Greenville University",
    "Northwest Missouri State University",
    "Nova Southeastern University",
    "Ohio Dominican University",
    "Oklahoma Baptist University",
    "Palm Beach Atlantic University",
    "Pfeiffer University",
    "Point Loma Nazarene University",
    "Queens University of Charlotte",
    "Regis University",
    "Rockhurst University",
    "Rollins College",
    "Saint Leo University",
    "Saint Martin's University",
    "San Francisco State University",
    "Seton Hill University",
    "Shorter University",
    "Sonoma State University",
    "Southern Arkansas University",
    "Southwestern Oklahoma State University",
    "St. Cloud State University",
    "St. Edward's University",
    "St. Mary's University (TX)",
    "Tarleton State University",
    "Texas A&M International University",
    "Tiffin University",
    "Trevecca Nazarene University",
    "University of Central Missouri",
    "University of Colorado, Colorado Springs",
    "University of Findlay",
    "University of Indianapolis",
    "University of Minnesota, Crookston",
    "University of Missouri-St. Louis",
    "University of Montevallo",
    "University of Mount Olive",
    "University of Nebraska at Kearney",
    "University of North Georgia",
    "University of Sioux Falls",
    "University of Southern Indiana",
    "University of Tampa",
    "University of West Florida",
    "University of Wisconsin-Parkside",
    "Upper Iowa University",
    "Valdosta State University",
    "Walsh University",
    "Wayne State College (NE)",
    "West Texas A&M University",
    "West Virginia Wesleyan College",
    "Western New Mexico University",
    "Wingate University",
    "Winona State University",
    "Young Harris College"
]

division3_golf_colleges = [
    "Amherst College",
    "Babson College",
    "Bard College",
    "Bates College",
    "Bowdoin College",
    "Brandeis University",
    "California Institute of Technology (Caltech)",
    "Carnegie Mellon University",
    "Claremont McKenna College",
    "Colby College",
    "Colby-Sawyer College",
    "Colorado College",
    "Connecticut College",
    "DePauw University",
    "Dickinson College",
    "Emory University",
    "Franklin & Marshall College",
    "Grinnell College",
    "Hamilton College",
    "Haverford College",
    "Johns Hopkins University",
    "Kenyon College",
    "Lafayette College",
    "Macalester College",
    "Middlebury College",
    "New York University (NYU)",
    "Oberlin College",
    "Occidental College",
    "Pomona College",
    "Rhodes College",
    "Sewanee: The University of the South",
    "Swarthmore College",
    "Trinity College",
    "Tufts University",
    "University of Chicago",
    "University of Puget Sound",
    "University of Redlands",
    "University of Rochester",
    "University of St. Thomas",
    "University of the South",
    "Vassar College",
    "Washington and Lee University",
    "Wellesley College",
    "Wesleyan University",
    "Whitman College",
    "Whittier College",
    "Williams College",
    "Wittenberg University",
    "Wooster College"
]

computerlist = []
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your golfing skills are poor")
elif computer == 2:
    print("Your golfing skills are average")
elif computer == 3: 
    print("Your golfing skills are execptional")

driver = int(input("enter a number to activate the magic spinner to decide your driving distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("You drive 250 yards on average")
elif computer == 2:
    print("You drive about 280 yards")
elif computer == 3:
    print("You drive about 300 yards")

driveraccuarcy = int(input("enter a number to activate the magic spinner to decide your driving accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is very poor with your driver")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your driving accuracy is execptional")

putting = int(input("enter a number to activate the magic spinner to decide your putting skill"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your putting is poor")
elif computer == 2:
    print("Your putting is average")
elif computer == 3:
    print("Your putting is exceptional")

wedgesdist = int(input("enter a number to activate the magic spinner to decide your wedge distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

wedgeacc = int(input("enter a number to activate the magic spinner to decide your wedge accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

ninedist = int(input("enter a number to activate the magic spinner to decide your 9iron distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

nineacc = int(input("enter a number to activate the magic spinner to decide your 9iron accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

eightdist = int(input("enter a number to activate the magic spinner to decide your 8iron distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

eightacc = int(input("enter a number to activate the magic spinner to decide your 8iron accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

sevendist = int(input("enter a number to activate the magic spinner to decide your 7iron distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

sevenacc = int(input("enter a number to activate the magic spinner to decide your 7iron accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

sixdist = int(input("enter a number to activate the magic spinner to decide your 6iron distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

nineacc = int(input("enter a number to activate the magic spinner to decide your 6iron accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

fivedist = int(input("enter a number to activate the magic spinner to decide your 5iron distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

fiveacc = int(input("enter a number to activate the magic spinner to decide your 5iron accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

threewddist = int(input("enter a number to activate the magic spinner to decide your 3 wood distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

threewdacc = int(input("enter a number to activate the magic spinner to decide your 3 wood accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

fivehybdist = int(input("enter a number to activate the magic spinner to decide your 5hybrid distance"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your distance is poor")
elif computer == 2:
    print("Your distance is average")
elif computer == 3:
    print("Your distance is exceptional")

fivehybacc = int(input("enter a number to activate the magic spinner to decide your 5hybrid accuracy"))
computer = random.randint(1,3)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("Your accuracy is poor")
elif computer == 2:
    print("Your accuracy is average")
elif computer == 3:
    print("Your accuracy is exceptional")

hs = int(input("did you play on varsity in high school: enter a random number"))
computer = random.randint(1,2)
computerlist.append(computer)
print(computerlist)

if computer == 1:
    print("NO")
elif computer == 2:
    print("YES")

c = int(input("did you make it to college: enter a random number"))
computer = random.randint(1,10)
computerlist.append(computer)
print(computerlist)
if computer == 1:
    print("You did not make it to college golf: Your carrer ends")
elif computer > 1:
    print("You made it to college golf")
    division = int(input("which division did you go to? 1, 2, or 3? Enter a random number"))
    computed = random.randint(1,3)
    computerlist.append(computed)
    print(computerlist)
if computed == 1:
    print("You made division 1 golf")
    college = random.choice(division1_golf_colleges)
    print("Your college is: ", college)
if computed == 2:
    print("You made division 2 golf")
    college = random.choice(division2_golf_colleges)
    print("Your college is: ", college)
if computed == 3:
    print("You made division 3 golf")
    college = random.choice(division3_golf_colleges)
    print("Your college is: ", college)
elif computer == 5:
    print("you made it to LIV golf")

elif computer == 10:
    print("You made it to the PGA tour")
