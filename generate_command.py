classes_file = open("classes.txt", "r")

classes = []
for line in classes_file:
    classes += [c.strip() for c in line.split(",")]

classes_file.close()

classes += ["archery", "biking through snow", "riding a bike", "riding mountain bike", "brushing teeth",
            "catching or throwing frisbee", "crawling baby", "dunking basketball", "golf driving", "hula hooping",
            "contact juggling", "juggling balls", "knitting", "making pizza", "mopping floor", "playing drums",
            "playing piano", "playing volleyball", "punching bag", "riding or walking with horse", "scuba diving",
            "skiing", "skiing crosscountry", "skiing slalom", "kicking soccer ball", "shooting goal",
            "swimming breast stroke", "throwing discus", "dribbling basketball", "playing basketball",
            "shooting basketball", "blowing out candles", "canoeing or kayaking", "clean and jerk", "cutting pineapple",
            "cutting watermelon", "filling eyebrows", "hammer throw", "javelin throw", "juggling soccer ball",
            "long jump", "marching", "playing cello", "playing flute", "playing tennis", "pole vault",
            "punching person", "rock climbing", "shot put", "skipping rope", "squat", "swing dancing",
            "trimming or shaving beard", "bench pressing", "bowling", "catching or throwing baseball",
            "climbing a rope", "diving cliff", "getting a haircut", "high jump", "jetskiing", "jumping into pool",
            "lunge", "massaging persons head", "playing cricket", "playing guitar", "playing violin", "pull ups",
            "push up", "salsa dancing", "skateboarding", "skydiving", "surfing water", "tai chi", "walking the dog"]

command = "python3 download.py --classes "

for c in classes:
    command += "\'{}\' ".format(c)

command = command.strip()


with open("download.sh", "w") as download_script:
    download_script.write(command)
