bg1X = 0
bg1Y = 0
bg2X = 1080
bg2Y = 0
window = 0
bgColorList = [[255, 255, 255], [255, 0, 0], [255, 127, 0], [255, 255, 0], [0, 255, 0], [0, 0, 255], [0, 0, 128], [180, 85, 162]]
bgColor = 0
startLevelY = 300
startLevelSize = 80
startColorY = 450
startColorSize = 30
level = 1
sumScore = 0
bestScore = 1
playerY = 270
obs1X = 1000


def setup():
    global bg, player1, obstacle1
    size(1080, 540)
    bg = loadImage("background.png")
    player1 = loadImage("p1.jpg")
    obstacle1 = loadImage("1.png")
    
def draw():
    global bg, bg1X, bg1Y, bg2X, bg2Y, window, bgColorList, bgColor, startLevelY, startLevelSize, startColorY, startColorSize, level, sumScore, playerY
    # print(bgColor)
    background(bgColorList[bgColor][0], bgColorList[bgColor][1], bgColorList[bgColor][2])
    if window == 0:
        start()
    elif window == 1:
        game()
        
        
        
def start():
    global bg, bg1X, bg1Y, bg2X, bg2Y, window, bgColorList, bgColor, startLevelY, startLevelSize, startColorY, startColorSize, level, sumScore, bestScore
    
    
    # Title
    textSize(70)
    textAlign(CENTER)
    fill(0)
    text("Title", width/2, 200)
    
    # Score
    textSize(30)
    fill(0)
    textAlign(LEFT)
    text("Best Score: {}".format(bestScore), 30, 50)
    text("Score: {}".format(sumScore), 30, 80)
    
    
    
    # Level Button
    for i in range(3):
        rectMode(CENTER)
        fill(255)
        rect(360+180*i, startLevelY, startLevelSize, startLevelSize)
        textSize(30)
        textAlign(CENTER)
        fill(0)
        text("Level\n{}".format(i+1), 360+180*i, 290)
    
    # Background Color
    for i in range(8):
        rectMode(CENTER)
        fill(bgColorList[i][0], bgColorList[i][1], bgColorList[i][2])
        rect(700+40*i, startColorY, startColorSize, startColorSize)
    
    if mousePressed:
        # Background Color Change
        if startColorY-startColorSize/2<=mouseY<=startColorY+startColorSize/2:
            for i in range(8):
                if 700+40*i-startColorSize/2<=mouseX<=700+40*i+startColorSize/2:
                    bgColor = i
        # Level Select
        if startLevelY-startLevelSize/2<=mouseY<=startLevelY+startLevelSize/2:
            # print(11)
            for i in range(3):
                if 360+180*i-startLevelSize/2<=mouseX<=360+180*i+startLevelSize/2:
                    window = 1
                    level = i+1
    

    
def game():
    global bg, bg1X, bg1Y, bg2X, bg2Y, window, bgColorList, bgColor, level, player1, playerY, obstacle1, obs1X
    imageMode(CORNER)
    image(bg, bg1X, bg1Y)
    image(bg, bg2X, bg2Y)
    text(level, width/2, height/2)
    bg1X -= 5
    bg2X -= 5
    if bg1X <= -1080:
        bg1X = 1080
    if bg2X <= -1080:
        bg2X = 1080
    
    imageMode(CENTER)
    image(player1, 100, playerY, 60, 100)
    
    if keyPressed:
        if keyCode == UP:
            playerY -= 4
        elif keyCode == DOWN:
            playerY += 4
    
    if obs1X>= -50:    
        image(obstacle1, obs1X, height/2, 50, 50)
        obs1X -= 8
    
    
    
    
