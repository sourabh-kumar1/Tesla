import pygame
pygame.init()
window=pygame.display.set_mode((1200,400))
track=pygame.image.load('track3.png')
car=pygame.image.load('sktesla.png')
cat=pygame.transform.scale(car,(3,6))
car_x=155
car_y=300
focal_dis=25
direction='up'
drive=True
clock=pygame.time.Clock()
while True:
    #for event in pygame.event.get():
     #   if event.type==pygame.quit():
     #       drive=False
    clock.tick(60)
    cam_x=car_x + 15
    cam_y=car_y + 15
    up_px=window.get_at((cam_x,cam_y-focal_dis))[0]
    right_px=window.get_at((cam_x+ focal_dis,cam_y))[0]
    print(up_px,right_px)

    #change direction
    if direction =='up' !=255 and right_px ==255:
        direction='right'
        car=pygame.transform.rotate(car,-90)
        #drive
    if up_px==255:
        car_y=car_y-2
    elif direction=='right' and right_px==255:
        car_x=car_x+2
    window.blit(track,(0,0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y),5,5)
    pygame.display.update()


