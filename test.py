import json

ZONENAME = 'ZONENAME'
DESCRIPTION = 'DESCRIPTION'
EXAMINATION = 'EXAMINATION'
COMPLETE = "COMPLETE"
CLEANED = "CLEANED"
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

complete_places = {
    "a1": False, "a2": False, "a3": False, "a4": False,
    "b1": False, "b2": False, "b3": False, "b4": False,
    "c1": False, "c2": False, "c3": False, "c4": False,
    "d1": False, "d2": False, "d3": False, "d4": False,
}

zonemap = {
    "a1": {
        ZONENAME: "West Black Market Stall",
        DESCRIPTION: "This stall sells various hazardous and experimental drugs. These have been outlawed for a reason",
        EXAMINATION: "The man running the stall is covered in cybernetic implants,\nwhich at a first glance have obviously been stolen from various SCP/D droids you recognise.",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2"
    },
    "a2": {
        ZONENAME: "Black Market Entrance",
        DESCRIPTION: "The entrance to the black market.\nYou wonder why such an obviously illegal area has not been raided or taken down by SCP/D law \nenforcement.",
        EXAMINATION: "Many intense and drudged looking people are entering and leaving the Black Market,\nsome of them look glance at you and,\nlikely under the assumption that you yourself are some sort of law enforcement,\nscoff at your existence.",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3"
    },
    "a3": {
        ZONENAME: "Center Black Market Stall",
        DESCRIPTION: "description",
        EXAMINATION: "examination",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4"
    },
    "a4": {
        ZONENAME: "South Black Market Stall",
        DESCRIPTION: "description",
        EXAMINATION: "examination",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: ""
    },
    "b1": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "b2": {
        ZONENAME: "Thin Walkway",
        DESCRIPTION: "A thin walkway filled with signs and conglomerate advertisements",
        EXAMINATION: "Many advertisements are showcasing the new Better Than Life Virtual Environment Simulation.\nThis only appeals to the lower class and people living in horrid situations.\nClassic.",
        COMPLETE: False,
        CLEANED: False,
        UP: "a2",
        DOWN: "",
        LEFT: "",
        RIGHT: "b3"
    },
    "b3": {
        ZONENAME: "Apartment",
        DESCRIPTION: "This is your apartment. It's filled with trash. You haven't decided to clean it yet.",
        EXAMINATION: "Nothing has changed about your apartment. Except you remember you should clean it someday.",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "",
        LEFT: "b2",
        RIGHT: ""
    },
    "b4": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c1": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c2": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c3": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c4": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
}

with open("test.json", 'w') as f:
    json.dump(zonemap, f)
with open("test2.json", 'w') as f:
    json.dump(complete_places, f)

f = open("test.json")
load = json.loads(f.read())
f2 = open("test2.json")
load2 = json.loads(f2.read())

print(load)
print(load2)