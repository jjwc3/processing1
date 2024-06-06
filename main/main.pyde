window = 0
level = 1
sumScore = 0
bestScore = 1

# start
bgColorList = [[255, 255, 255], [255, 0, 0], [255, 127, 0], [255, 255, 0], [0, 255, 0], [0, 0, 255], [0, 0, 128], [180, 85, 162]]
bgColor = 0

#game
bg1X = 0
bg2X = 1080
playerY = 270
playerNum = 0
spawnInterval = 1000
obstaclesList = []
gameOver = False


def setup():
    global bg, player, obstacleImg, lastSpawnTime
    size(1080, 540)
    bg = loadImage("sky1.png")
    player = []
    for i in range(1, 13):
        player.append(loadImage("p{}.png".format(i)))
    obstacleImg = []
    for i in range(1, 4):
        obstacleImg.append(loadImage("obs{}.png".format(i)))
        
    lastSpawnTime = millis()
        
def draw():
    global window
    if window == 0:
        start()
    elif window == 1:
        game()
        
        
        
def start():
    global window, bgColorList, bgColor, level, sumScore, bestScore
    background(bgColorList[bgColor][0], bgColorList[bgColor][1], bgColorList[bgColor][2])
    
    # Title
    textSize(70)
    textAlign(CENTER)
    if bgColor in [0,3,4]:
        fill(0)
    else:
        fill(255)
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
        rect(360+180*i, 300, 80, 80)
        textSize(30)
        textAlign(CENTER)
        fill(0)
        text("Level\n{}".format(i+1), 360+180*i, 290)
    
    # Background Color
    for i in range(8):
        rectMode(CENTER)
        fill(bgColorList[i][0], bgColorList[i][1], bgColorList[i][2])
        rect(700+40*i, 450, 30, 30)
    
    if mousePressed:
        # Background Color Change
        if startColorY-startColorSize/2<=mouseY<=startColorY+startColorSize/2:
            for i in range(8):
                if 700+40*i-startColorSize/2<=mouseX<=700+40*i+startColorSize/2:
                    bgColor = i
        # Level Select
        if startLevelY-startLevelSize/2<=mouseY<=startLevelY+startLevelSize/2:
            for i in range(3):
                if 360+180*i-startLevelSize/2<=mouseX<=360+180*i+startLevelSize/2:
                    window = 1
                    level = i+1
    

    
def game():
    global bg, bg1X, bg2X, window, level, playerY, player, playerNum, obstacleImg, obstaclesList, lastSpawnTime, spawnInterval, gameOver
    # Background
    imageMode(CORNER)
    image(bg, bg1X, 0, 1080, 675)
    image(bg, bg2X, 0, 1080, 675)
    if not gameOver:
        bg1X -= 5
        bg2X -= 5
        if bg1X <= -1080:
            bg1X = 1080
        if bg2X <= -1080:
            bg2X = 1080
    
    # Player
    if not gameOver:
        playerNum = millis()/100%12
    imageMode(CENTER)
    image(player[playerNum], 100, playerY, 60, 100)
    if not gameOver and keyPressed:
        if keyCode == UP and playerY>50:
            playerY -= 8
        elif keyCode == DOWN and playerY<490:
            playerY += 8

    # Obstacles
    if not gameOver and millis() - lastSpawnTime > spawnInterval:
        obstaclesList.append([int(random(0,3)), width+50, random(50, 490)])
        lastSpawnTime = millis()
    
    for i in obstaclesList:
        i[1] -= 10
        image(obstacleImg[i[0]], i[1], i[2], 50*obstacleImg[i[0]].width/obstacleImg[i[0]].height, 50)
    
    obstaclesList = [i for i in obstaclesList if i[1] > -obstacleImg[i[0]].width] # Show Obstacles When they are in screen
    
    #Game Over
    if gameOver:
        filter(GRAY)
        textSize(70)
        fill(0)
        text("Game Over", width/2, height/2)
        
        
    
    
