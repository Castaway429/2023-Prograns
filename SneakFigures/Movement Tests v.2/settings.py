import pygame

#20 spaces in the rows
level_map = [
'                              ',
'              XXX           XX',
'         XXX                 X',
'   XXXXX     XXX             X',
'X           XXXXX           XX',
'XX         X     X       X    ',
'   X   X          X     XXX   ',
'P XX   XXX             XXXXX  ',
'XXXX  XXXXXXX   XXXX XXXXXXXX ',
'XXXXKKXXXXXXXKKKXXXXKXXXXXXXX ',
'XXXXKKXXXXXXXKKKXXXXKXXXXXXXX ',
'XXXXKKXXXXXXXKKKXXXXKXXXXXXXX ',
'XXXXKKXXXXXXXKKKXXXXKXXXXXXXX ',
]

tile_size = 64

screen_width = 1200
screen_height = 600

#len(level_map) * tile_size